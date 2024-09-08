import pandas as pd
import warnings
import datetime

warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)

df = pd.read_csv("raw_ohlcv_data.csv")

stocks = {"WTI": "West Texas Intermediate",
          "XOM": "Exxon Mobil",
          "CVX": "Chevron Corporation",
          "LMT": "Lockheed Martin",
          "SPY": "Standard and Poor 500",
          "XOP": "S&P500 - Oil & Gas Exploration & Production",
          "SOYB": "Bloomberg Soybean Subindex",
          "RJA": "Element rogers international commodity agriculture ETN",
          "XLF": "Financial Sector Performance in the SNP 500",
          "XAR": "S&P 500 - Aerospace & Defence ETF",
          "XLB": "S&P 500 - Healthcare"
          }

tickers = [ticker for ticker, _ in stocks.items()]
start_date = pd.to_datetime(datetime.date(2000, 1, 1))

df['date'] = pd.to_datetime(df["date"])
df = df[df['date'] > start_date]
df = df[df['act_symbol'].isin(tickers)]

drop_columns = ["open", "high", "low", "close"]
df["spread"] = df["high"] - df["low"]
df["price"] = df["close"]
df = df.drop(drop_columns, axis=1)

wide_df = pd.DataFrame()
wide_df["date"] = df["date"]
wide_df = wide_df.drop_duplicates()
final_columns = ["volume", "spread", "price"]  # desired columns
final_columns_drop = ['act_symbol', 'volume', 'spread', 'price']  # columns to drop

for ticker in tickers:
    long_df = df
    shortened = long_df[long_df['act_symbol'] == ticker]
    for col in final_columns:
        shortened[f"{ticker}_{col}"] = shortened[col].copy()

    shortened.drop(final_columns_drop, inplace=True, axis=1)
    wide_df = wide_df.merge(shortened, on=["date"])

wide_df = wide_df.set_index('date')
wide_df = wide_df.reset_index()
wide_df = wide_df.set_index('date')
wide_df.to_csv("market_data.csv")

if __name__ == '__main__':
    print(wide_df.head)
    cols = wide_df.columns.tolist()
    for c in cols:
        print(c)
    wide_df.to_csv("market_data.csv")
