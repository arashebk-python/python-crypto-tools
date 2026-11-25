import requests

def get_crypto_price(crypto_id, currency='usd'):
    """Fetches the current price of a cryptocurrency from CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[crypto_id][currency]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("--- Crypto Price Checker ---")
    coin = input("Enter crypto name (e.g., bitcoin, ethereum, solana): ").lower()
    price = get_crypto_price(coin)
    
    if isinstance(price, float):
        print(f"Current price of {coin.capitalize()}: ${price:,}")
    else:
        print(price)
