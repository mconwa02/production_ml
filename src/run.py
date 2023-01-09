from components.data_import.load_data import load_coffee_data
from components.format_data.common import transpose_and_format_df

(
    dom_df,
    ex_df,
    green_df,
    impo_df,
    import_df,
    prod_df,
    expo_df,
) = load_coffee_data()

print(dom_df.head())
print(dom_df.columns)

ex_df_2 = ex_df.pipe(transpose_and_format_df)
green_df_2 = green_df.pipe(transpose_and_format_df)
impo_df_2 = impo_df.pipe(transpose_and_format_df)
import_df_2 = import_df.pipe(transpose_and_format_df)
expo_df_2 = expo_df.pipe(transpose_and_format_df)


# todo join dataframes by country, aka create 55 df for each country
for col in ex_df_2.columns:
    df = ex_df_2[[col]] + green_df_2[[col]]  # some countries missing
print()
