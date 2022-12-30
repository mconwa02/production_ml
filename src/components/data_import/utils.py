from pathlib import Path

import pandas as pd

from logging_config import main_logger

logger = main_logger()


def read_from_csv_and_write_to_parquet(path: Path, file_name: str):
    logger.info(f"Reading in {file_name}.csv")
    df = pd.read_csv(path.joinpath(file_name + ".csv"))
    df.to_parquet(path.joinpath(file_name + ".pq"))
