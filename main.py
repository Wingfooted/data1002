import pandas as pd
import datetime

df = pd.read_csv("raw_ohlcv_data.csv")

stocks = {"WTI": "West Texas Intermediate",
          "XOM": "Exxon Mobil",
          "CVX": "Chevron Corporation",
          "SHEL": "Shell",
          "LMT": "Lockheed Martin",
          "MA": "Mastercard",
          "JPM": "JP Morgan",
          "KO": "Coca-Cola Co"
          }

# defining values to keep in the data set
# these are set manually / predefined
tickers = [ticker for ticker, _ in stocks.items()]
start_date = pd.to_datetime(datetime.date(2015, 1, 1))

df['date'] = pd.to_datetime(df["date"])
df = df[df['date'] > start_date]
df = df[df['act_symbol'].isin(tickers)]

# now to moddify data columns
# columns wanted:
# spread, high-low
# close
# volume

drop_columns = ["open", "high", "low", "close"]
df["spread"] = df["high"] - df["low"]
df["price"] = df["close"]
# in finance, the close price often encapsulates the events of the trading day most. It is most reflective of the trading day
df = df.drop(drop_columns, axis=1)

# now to turn data into a long format
#
# this will be done by creating a sub dataframe for the ticker (iterated from tickers) and appending it to the long df

wide_df = pd.DataFrame()
wide_df["date"] = df["date"]
wide_df = wide_df.drop_duplicates() # this makes date a valid index

final_columns = ["volume", "spread", "price"]
final_columns_drop = ['act_symbol', 'volume', 'spread', 'price']
# this is important to drop because you want table meta data to be descriptive in the wide format
# additionally act_symbol will be encoded in the wide title format of volume, spread and price

for ticker in tickers:

    long_df = df
    shortened = long_df[long_df['act_symbol'] == ticker]

    # renaming columns of shortened df
    for col in final_columns:
        shortened[f"{ticker}_{col}"] = shortened[col].copy()

    shortened.drop(final_columns_drop, inplace=True, axis=1)
    print(shortened.head())
    print(wide_df.head())
    wide_df = wide_df.merge(shortened, on=["date"])

# reset index
df = df.reset_index(drop=True)

# tests
if __name__ == '__main__':
    print(wide_df.head)
    print(wide_df.info)
    wide_df.to_csv("market_data.csv")
