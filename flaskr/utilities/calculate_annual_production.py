import pandas as pd


class PopulateAnnualData:

    def __init__(self, url):
        self.url = url

    def read_file(self):
        # create dataframe from the Excel file
        df = pd.read_excel(self.url)
        return df

    def calculate_annual_data(self):

        # read Excel file
        df = self.read_file()
        # create new dataframe with oil, gas and brine which is grouped by API well number
        annual_data = df.groupby("API WELL  NUMBER")[["OIL", "GAS", "BRINE"]].sum()
        annual_data.index.rename("api_well_number", inplace=True)
        annual_data.columns = annual_data.columns.str.lower()
        return annual_data



