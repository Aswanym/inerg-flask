import pandas as pd
import sqlite3
from flask import (
    Blueprint, request
)
from decouple import config

bp = Blueprint('annual_data', __name__)


@bp.route('/data')
def get_data():
    well_number = request.args.get('well')
    q = request.args.get('q')

    if q:
        df = pd.read_excel(config("PATH_TO_EXCEL_FILE"))

        quarter = list(map(int, q.split(',')))
        filtered_df = df[(df['API WELL  NUMBER'] == int(well_number)) & (df['QUARTER 1,2,3,4'].isin(quarter))]
        nw = filtered_df.groupby("API WELL  NUMBER")[["OIL", "GAS", "BRINE"]].sum()

        oil = int(nw['OIL'].iloc[0])
        gas = int(nw['GAS'].iloc[0])
        brine = int(nw['BRINE'].iloc[0])

        res = {"oil": oil,
               "gas": gas,
               "brine": brine}
    else:

        # Connect to SQLite database
        conn = sqlite3.connect(config("DB_LOCATION"))
        cursor = conn.cursor()

        # Retrieve data for the given well number

        query = f"SELECT oil, gas, brine FROM annual_production " \
                f"WHERE api_well_number='{well_number}'"
        cursor.execute(query)
        result = cursor.fetchone()

        # Close the connection
        conn.close()

        # Return the result in JSON format
        if result:
            res = {"oil": result[0], "gas": result[1], "brine": result[2]}

    return res
