# ticker_price.py

import requests

# Replace this with your actual Alpha Vantage API key
API_KEY = "8TOZKZ3I2543J6F9"

def get_stock_price(ticker):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    try:
        price = data["Global Quote"]["05. price"]
        return f"The current price of {ticker} is ${price}"
    except KeyError:
        return "Error fetching stock price. Please check the ticker or try again later."

# Run a test
if __name__ == "__main__":
    print(get_stock_price("TSLA"))