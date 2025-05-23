# ticker_news.py
import requests

API_KEY = "8TOZKZ3I2543J6F9"

def get_stock_news(ticker):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        articles = data["feed"][:3]  # Get the top 3 news articles
        news_list = []
        for article in articles:
            title = article["title"]
            url = article["url"]
            news_list.append(f"- {title}\n  {url}")
        
        return "\n".join(news_list)
    except KeyError:
        return "Error fetching news. Try again later or check the ticker."

# Run a test
if __name__ == "__main__":
    print(get_stock_news("TSLA"))