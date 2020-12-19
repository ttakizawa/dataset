import os
import pandas as pd


def load_conversion():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + "/conversion/data.csv"
    return pd.read_csv(path)
