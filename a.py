import pandas as pd
import numpy as np

def load_and_clean_data(data_path):
    df = pd.read_csv(data_path)
    df = df.dropna()
    return df