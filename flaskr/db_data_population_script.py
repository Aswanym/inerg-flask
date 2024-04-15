# script that load the calculated annual data into a local sqlite database.

import sqlite3
from utilities.calculate_annual_production import PopulateAnnualData
from decouple import config

url = config("PATH_TO_EXCEL_FILE")

try:
    print("starting db connection...")
    conn = sqlite3.connect(config("DB_LOCATION"))
    pad = PopulateAnnualData(url)
    annual_data = pad.calculate_annual_data()
    annual_data.to_sql("annual_production", conn, if_exists="replace")
    print("data got inserted.")
except Exception:
    print("something went wrong in data insertion to db.")
