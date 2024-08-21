import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

def fetch_crypto_usd_data(coin_id, days=365):
    end_date = int(datetime.now().timestamp())
    start_date = int((datetime.now() - timedelta(days=days)).timestamp())
    
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?vs_currency=usd&from={start_date}&to={end_date}"
    
    response = requests.get(url)
    data = response.json()
    
    print(f"API Response status code for {coin_id}: {response.status_code}")
    
    df = pd.DataFrame(data['prices'], columns=['timestamp', f'{coin_id}_price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.date
    df = df.set_index('date')
    
    print(f"Dataframe shape for {coin_id}: {df.shape}")
    
    return df

def calculate_volatility(df):
    print("Columns in the merged dataframe:", df.columns)
    
    # Calculate daily returns
    df['stx_return'] = df['stacks_price'].pct_change()
    df['btc_return'] = df['bitcoin_price'].pct_change()
    df['stx_btc_return'] = df['stx_return'] - df['btc_return']
    
    # Calculate daily volatility
    df['daily_volatility'] = df['stx_btc_return'].rolling(window=30).std() * np.sqrt(365)
    
    print(f"Dataframe with calculations:\n{df.head()}")
    print(f"STX/BTC returns description:\n{df['stx_btc_return'].describe()}")
    print(f"Daily volatility description:\n{df['daily_volatility'].describe()}")
    
    # Calculate average volatility and standard deviation
    avg_volatility = df['daily_volatility'].mean()
    std_volatility = df['daily_volatility'].std()
    
    return avg_volatility, std_volatility

# Fetch data
stx_df = fetch_crypto_usd_data('stacks')
btc_df = fetch_crypto_usd_data('bitcoin')

# Merge dataframes
df = pd.merge(stx_df, btc_df, left_index=True, right_index=True, how='inner')

# Calculate volatility
avg_vol, std_vol = calculate_volatility(df)

print(f"Average daily volatility of STX relative to BTC: {avg_vol:.4f}")
print(f"Standard deviation of STX/BTC volatility: {std_vol:.4f}")