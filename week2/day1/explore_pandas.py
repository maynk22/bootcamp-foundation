import pandas as pd

csv_file = '../../data/Indian_Web_Series_2014_2025_Episodes_Clean.csv'

df = pd.read_csv(csv_file)

df_loc_label = df.loc[1:5, 'series_title']
df_loc_conditional = df.loc[(df['rating_drop_from_season_avg']> 0.5)]

df_iloc = df.iloc[1:5, 1:5]
# print("top 5 rows", df.head())
# print("last 5 rows", df.tail(5))
# print("info about data", df.info())
# print("description of data", df.describe())
# print("shape of dataframe", df.shape)
# print("data types of each column", df.dtypes)

# print(df_loc_label)
# print(df_loc_conditional)

print(df_iloc)
