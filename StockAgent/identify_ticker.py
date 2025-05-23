# identify_ticker.py

# This is a simple dictionary that maps company names to their stock tickers.
TICKER_MAP = {
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "palantir": "PLTR",
    "apple": "AAPL",
    "google": "GOOGL"
}

def identify_ticker(company_name):
    company_name = company_name.lower().strip()
    return TICKER_MAP.get(company_name, "Ticker Not Found")

# Run a test
if __name__ == "__main__":
    print(identify_ticker("Tesla"))  # Output: TSLA