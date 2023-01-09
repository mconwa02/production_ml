import pandas as pd


def format_df_column_names(df: pd.DataFrame):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("/", "_")
    return df


def transpose_and_format_df(df: pd.DataFrame):
    df = df.copy().transpose()
    first_row = df[:1].values[0]
    df.columns = first_row
    df.drop(index="country", inplace=True)
    return format_df_column_names(df)
