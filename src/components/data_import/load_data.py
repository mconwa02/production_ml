from pathlib import Path

from components.data_import.utils import read_from_csv_and_write_to_parquet
from components.schemas.table_schemas import ImportTables

DATA_PATH = Path(r"C:\dev\data\prod_ml\coffee-dataset")


def load_coffee_data():
    """
     Reading in CSV files of six kaggle coffee dataset, writing to parquet
     files and assigning to dataframe.

    return: tuple of six pandas data frames
    """
    domestic_consumption_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, ImportTables.DOMESTIC_CONSUMPTION.value
    )
    export_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, ImportTables.EXPORT.value
    )
    green_coffee_inventorie_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, ImportTables.INVENTORY.value
    )
    importers_consumption_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, ImportTables.DOMESTIC_CONSUMPTION.value
    )
    production_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, ImportTables.PRODUCTION.value
    )
    re_export_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, ImportTables.EXPORT.value
    )

    return (
        domestic_consumption_df,
        export_df,
        green_coffee_inventorie_df,
        importers_consumption_df,
        production_df,
        re_export_df,
    )


if __name__ == "__main__":
    load_coffee_data()
