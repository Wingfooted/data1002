import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def descriptive_statistics(df, test_cols):
    cols = df.columns.tolist()
    vectors = {
        col: np.array(df[col].tolist())
        for col in cols
        if col in test_cols
    }
    data_dict = {
            col: [np.mean(v), np.std(v), np.median(v), np.max(v), np.min(v)] # STATISTICS WE WANT
            for col, v in
            vectors.items()
    }
    index = ["Mean", "Standard Deviation", "Max", "Min", "Mode"]
    return pd.DataFrame(data_dict, index=index)


def completeness_statistics(df):
    total_entries = len(df)
    first_date = pd.to_datetime(df.iloc[0,0])
    last_date = pd.to_datetime(df.iloc[-1,0])
    df = pd.to_datetime(df['date'])

    def trading_days(start, end):
        # calculates numbre of trading days (trading only happens mon - fri)
        delta = datetime.timedelta(days=1)
        trading_days_count = 0
        current = start
        while current < end:
            if current.weekday() >= 5:
                pass  # (weekend)
            elif current.weekday() < 5:
                # week day
                trading_days_count += 1
            current += delta

        return trading_days_count

    num_trading_days = trading_days(first_date, last_date)
    percentage_completeness = str((total_entries / num_trading_days ) * 100 ) + "%"

    # test 2

    return percentage_completeness


def plots(df, ncols=2):
    plottable = [col
        for col in df.columns.tolist()
        if "volume" in col
    ]
    vectors = [
            np.array(df[col].tolist())
            for col in
            plottable
        ]
    n = len(vectors)
    nrows = (n+ncols-1)//ncols

    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 5, nrows * 4))
    axes = axes.flatten()

    for index, vector in enumerate(vectors):
        res = stats.probplot(vector, dist="norm", plot=axes[index])
        axes[index].set_title(f'Q-Q Plot {plottable[index]}')
        axes[index].get_lines()[1].set_color('red')

    for j in range(len(vectors), len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()
    plt.savefig("qqplots.py")


if __name__ == '__main__':
    df = pd.read_csv("market_data.csv")
#    print(completeness_statistics(df))
    #plots(df)
    descriptive_statistics_columns = df.columns.tolist()

    del descriptive_statistics_columns[0]  # this removes the date column
#    print(descriptive_statistics_columns)
    ds_df = descriptive_statistics(df, descriptive_statistics_columns)
    print(ds_df.head())

    print("sucsess")
