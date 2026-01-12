import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Carica il dataset delle vendite da CSV
    """
    return pd.read_csv(path)
