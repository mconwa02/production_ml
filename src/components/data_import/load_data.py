from pathlib import Path

from components.data_import.utils import read_from_csv_and_write_to_parquet
from components.format_data.common import format_df_column_names
from components.schemas.table_schemas import (
    DOMESTIC_CONSUMPTION_SCHEMA,
    EXPORT_SCHEMA,
    IMPORT_SCHEMA,
    IMPORTERS_CONSUMPTION_SCHEMA,
    INVENTORIE_SCHEMA,
    PRODUCTION_SCHEMA,
    RE_EXPORT_SCHEMA,
    Tables,
)

DATA_PATH = Path(r"C:\dev\data\prod_ml\coffee-dataset")


def load_coffee_data():
    """
     Reading in CSV files of seven kaggle coffee dataset, writing to parquet
     files and assigning to dataframe. Also validates the dataframe schemas.

    return: tuple of seven pandas data frames
    """
    domestic_consumption_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.DOMESTIC_CONSUMPTION.value
    )
    export_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.EXPORT.value
    )
    green_coffee_inventorie_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.INVENTORY.value
    )
    importers_consumption_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.IMPORTERS_CONSUMPTION.value
    )
    import_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.IMPORT.value
    )
    production_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.PRODUCTION.value
    )
    re_export_df = read_from_csv_and_write_to_parquet(
        DATA_PATH, Tables.RE_EXPORT.value
    )

    DOMESTIC_CONSUMPTION_SCHEMA.validate(domestic_consumption_df)
    EXPORT_SCHEMA.validate(export_df)
    INVENTORIE_SCHEMA.validate(green_coffee_inventorie_df)
    IMPORTERS_CONSUMPTION_SCHEMA(importers_consumption_df)
    IMPORT_SCHEMA(import_df)
    PRODUCTION_SCHEMA.validate(production_df)
    RE_EXPORT_SCHEMA.validate(re_export_df)

    domestic_consumption_df.pipe(format_df_column_names)
    export_df.pipe(format_df_column_names)
    green_coffee_inventorie_df.pipe(format_df_column_names)
    importers_consumption_df.pipe(format_df_column_names)
    import_df.pipe(format_df_column_names)
    production_df.pipe(format_df_column_names)
    re_export_df.pipe(format_df_column_names)

    return (
        domestic_consumption_df,
        export_df,
        green_coffee_inventorie_df,
        importers_consumption_df,
        import_df,
        production_df,
        re_export_df,
    )


if __name__ == "__main__":
    load_coffee_data()
