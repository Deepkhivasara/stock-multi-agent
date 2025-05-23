# ticker_price_change.py

import requests
from datetime import datetime, timedelta

API_KEY = "8TOZKZ3I2543J6F9"

def get_price_change(ticker, days):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        time_series = data["Time Series (Daily)"]
        dates = sorted(time_series.keys(), reverse=True)

        today = dates[0]
        past_date = dates[days]

        today_price = float(time_series[today]["4. close"])
        past_price = float(time_series[past_date]["4. close"])
        change = today_price - past_price
        percent_change = (change / past_price) * 100

        return (
            f"{ticker} price {days} days ago was ${past_price:.2f}, "
            f"now it's ${today_price:.2f}. Change: ${change:.2f} ({percent_change:.2f}%)"
        )
    except Exception as e:
        return f"Error fetching or processing data: {str(e)}"

# Run a test
if __name__ == "__main__":
    print(get_price_change("TSLA", 7))