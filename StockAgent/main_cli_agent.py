# main_cli_agent.py

from ticker_analysis import analyze_stock
from ticker_price import get_stock_price
from ticker_price_change import get_price_change
from ticker_news import get_stock_news
from identify_ticker import identify_ticker

def respond_to_query(user_input):
    user_input = user_input.lower()

    # Very basic keyword detection
    if "tesla" in user_input:
        company = "Tesla"
    elif "nvidia" in user_input:
        company = "Nvidia"
    elif "palantir" in user_input:
        company = "Palantir"
    elif "apple" in user_input:
        company = "Apple"
    else:
        return "I don't recognize the company."

    ticker = identify_ticker(company)

    if "price" in user_input and "change" in user_input:
        return get_price_change(ticker, 7)
    elif "price" in user_input:
        return get_stock_price(ticker)
    elif "news" in user_input or "happening" in user_input:
        return get_stock_news(ticker)
    elif "why" in user_input or "analysis" in user_input:
        return analyze_stock(ticker, 7)
    else:
        return "Sorry, I didn't understand the query."

# Run test loop
if __name__ == "__main__":
    print("💬 Stock ChatBot (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        print("Bot:", respond_to_query(query))