import requests

def get_prices(coins, vs_currency="usd"):
    """
    Fetch current prices of coins from CoinGecko API
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={vs_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching prices:", e)
        return {}
