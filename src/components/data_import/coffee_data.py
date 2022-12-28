from pathlib import Path

from components.data_import.utils import read_csv_write_parquet

DATA_PATH = Path(r"C:\dev\data\prod_ml\coffee-dataset")
print(DATA_PATH)

coffee_tables = {
    "Coffee_domestic_consumption": "coffee_domestic_consumption",
    "Coffee_export": "coffee_export",
    "Coffee_green_coffee_inventorie": "coffee_green_coffee_inventorie",
    "Coffee_import": "coffee_import",
    "Coffee_importers_consumption": "coffee_importers_consumption",
    "Coffee_production": "coffee_production",
    "Coffee_re_export": "coffee_re_export",
}


def main():
    for name in coffee_tables.keys():
        read_csv_write_parquet(DATA_PATH, name)


if __name__ == "__main__":
    main()
