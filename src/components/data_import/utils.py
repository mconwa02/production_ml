from pathlib import Path

import pandas as pd


def read_csv_write_parquet(path: Path, file_name: str):
    df = pd.read_csv(path.joinpath(file_name + ".csv"))
    df.to_parquet(path.joinpath(file_name.lower() + ".pq"))
