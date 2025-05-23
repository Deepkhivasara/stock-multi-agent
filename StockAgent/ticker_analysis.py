# ticker_analysis.py

from ticker_price_change import get_price_change
from ticker_news import get_stock_news

def analyze_stock(ticker, days=7):
    # Get price change info
    price_info = get_price_change(ticker, days)
    
    # Get recent news
    news_info = get_stock_news(ticker)
    
    # Combine and summarize
    analysis = (
        f"📈 Price Summary:\n{price_info}\n\n"
        f"📰 News Summary (top 3 headlines):\n{news_info}\n\n"
        f"💡 Analysis:\nBased on the recent price movement and news, "
        f"the stock '{ticker}' might be reacting to the above events. "
        f"For deeper insights, consider reading the full articles."
    )
    return analysis

# Run a test
if __name__ == "__main__":
    print(analyze_stock("TSLA", 7))