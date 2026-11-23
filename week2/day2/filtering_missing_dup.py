import pandas as pd

data = '../../data/Indian_Web_Series_2014_2025_Episodes_Clean.csv'

df = pd.read_csv(data)
raw = df.copy()

#1. Netflix series only.
raw_nextflix = raw[raw['network_service'] == 'Netflix']
#print(raw_nextflix)

#2. Crime or Thriller (primary_genre) on Prime Video, starting in 2020 or later.
raw_output = raw[((raw['primary_genre'] == 'Crime') | (raw['primary_genre'] =='Thriller')) & (raw['network_service'] == 'Prime Video') & (raw['start_year'] >= 2020)]
#print(raw_output)

#3. Episodes rated 9.0 or higher with at least 1,000 votes. Then say why the votes condition matters.
raw_episode_votes = df[(df['imdb_rating'] >= 9) & (df['imdb_votes'] >= 1000)]
#print(raw_episode_votes)

#4. Season finales that scored below their season average. Use rating_drop_from_season_avg, and check whether a positive value means below or above before you filter.
raw_season_average = df[(df['episode_position_type'] == 'Series Finale') & (df['rating_drop_from_season_avg']< 0)]
#print(raw_season_average)

#5. Series whose all_genres contains “Horror”. Use .str.contains
raw_series = df[df['all_genres'].str.contains('Horror')]
#print(raw_series)

#6. Rewrite #2 with .query(). Then say which version you find easier to read.
raw_query = raw.query('(primary_genre in ["Crime", "Thriller"]) and network_service == "Prime Video" and start_year >= 2020')
#print(raw_query)

#7. Use .isin() for [“ZEE5”, “SonyLIV”, “Voot”], then do the opposite with ~
raw_isin = df[df['network_service'].isin(['ZEE5', 'SonyLIV', 'Voot'])]
print(raw_isin)