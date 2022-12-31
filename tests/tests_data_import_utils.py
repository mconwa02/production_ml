from pathlib import Path

import pandas as pd

from components.data_import.utils import read_from_csv_and_write_to_parquet


def test_read_csv_write_parquet():
    test_path = Path.cwd().joinpath("data")
    actual = read_from_csv_and_write_to_parquet(test_path, "cust_data")
    expected = pd.DataFrame(
        data={"customer": ["A", "B", "C"], "products": [11, 1, 13]}
    )
    pd.testing.assert_frame_equal(actual, expected)
