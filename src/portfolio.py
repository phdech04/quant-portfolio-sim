import pandas as pd
import os

def merge_price_files(folder_path, tickers, price_column='Close/Last'):
    """
    Merges multiple CSV files containing stock prices into a single DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    tickers (list): A list of stock tickers to include in the merged DataFrame.
    price_column (str): The name of the column containing the price data.

    Returns:
      DataFrame with Date index and each stock as a column.
    """
    merged_df = pd.DataFrame()

    for ticker in tickers:
        file_path = os.path.join(folder_path, f'{ticker}.csv')
        df = pd.read_csv(file_path, parse_dates=['Date'], usecols=['Date', price_column])
        df= df.rename(columns={price_column: ticker})
        df[ticker]= df[ticker].replace('[\$,]', '', regex=True).astype(float)

        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on='Date', how='outer')

    merged_df = merged_df.set_index('Date').sort_index()  
    
    return merged_df

def calculate_daily_returns(prices):
    """
    Calculates daily percentage returns for each asset.

    Parameters:
    - price: DataFrame with asset prices.

    Returns:
    - DataFrame of daily returns.
    """
    daily_ret = prices.pct_change().dropna()
    return daily_ret

def calculate_cumulative_returns(daily_returns_df):
    """
    Calculates daily percentage returns for each asset.

    Parameters:
    - price_df (DataFrame): DataFrame with asset prices.

    Returns:
    - DataFrame of daily returns.
    """
    cumulative_returns = (1 + daily_returns_df).cumprod() 
    return cumulative_returns
    