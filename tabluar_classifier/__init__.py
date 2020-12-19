import os
import pandas as pd


def load_titanic():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    train_path = current_dir + "/titanic/train.csv"
    test_path = current_dir + "/titanic/test.csv"
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    return train_df, test_df
