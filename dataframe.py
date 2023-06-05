import pandas as pd

class Get_Dataframe:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def get_dataframe(self):
        df = pd.read_csv(self.csv_path)
        return df