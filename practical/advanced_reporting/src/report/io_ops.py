import pandas as pd
import yaml


def read_csv(path, sep=","):
    df = pd.read_csv(path, sep=sep, quotechar='"', encoding='utf-8')
    return df

def read_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)