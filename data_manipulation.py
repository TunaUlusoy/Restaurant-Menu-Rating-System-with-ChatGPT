import pandas as pd

class DataManipulation:
    def __init__(self, csv_path, sep):
        self.csv_path = csv_path
        self.sep = sep

    def get_reviews(self):
        df = pd.read_csv(self.csv_path, sep=self.sep) 
        df.drop("Liked", axis=1, inplace=True)
        
        return df[:len(df)//20]
