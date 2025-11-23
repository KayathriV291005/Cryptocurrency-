import requests
import pandas as pd
from datetime import datetime

# Coins to track
coins = ["bitcoin", "ethereum", "dogecoin", "litecoin", "ripple", 
         "cardano", "solana", "binancecoin", "polkadot", "shiba-inu"]
vs_currency = "usd"

def get_coin_data(coins, vs_currency="usd"):
    """
    Fetch current price, 24h change, market cap from CoinGecko API
    """
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={vs_currency}&ids={','.join(coins)}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return []

# Fetch coin data
coin_data = get_coin_data(coins, vs_currency)

if coin_data:
    print("------ Current Crypto Data ------")
    data_list = []
    for coin in coin_data:
        name = coin["name"]
        price = coin["current_price"]
        change_24h = coin["price_change_percentage_24h"]
        market_cap = coin["market_cap"]

        print(f"{name}: Price=${price}, 24h Change={change_24h:.2f}%, Market Cap=${market_cap}")
        
        data_list.append({
            "Coin": name,
            "Price (USD)": price,
            "24h Change (%)": change_24h,
            "Market Cap (USD)": market_cap,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    print("----------------------------------\n")

    # Save to Excel
    df = pd.DataFrame(data_list)
    df.to_excel("Crypto_Data.xlsx", index=False)
    print("Data saved to Crypto_Data.xlsx successfully!")

else:
    print("Failed to fetch coin data.")
