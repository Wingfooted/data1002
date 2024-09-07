import pandas as pd

markets = pd.read_csv("market_data.csv")
temp = pd.read_csv("data_temp.csv")

markets['date'] = pd.to_datetime(markets['date'])
markets['Year'] = markets['date'].dt.year
markets['Month'] = markets['date'].dt.strftime('%b')
markets_avg = markets.groupby(['Year', 'Month']).mean().reset_index()

merged_df = pd.merge(temp, markets_avg, on=['Year', 'Month']) 
# this drops all year-month pairings that do not exist within the dataframes
# ie, if one dataframe is longer than the other, the total length is the determined by the shoretet DF

merged_df.to_csv("integrated_data_set.csv")
