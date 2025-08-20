#Utility functions for students marks project

import pandas as pd 

def load_data(filepath):
     """load marks data from CSV"""
     return pd.read_csv(filepath)

     def calculate_average(df):
        """calculate average marks of all subject"""
        df["average"] = df[["math","science","english"]].mean(axs=1)
        return df

        