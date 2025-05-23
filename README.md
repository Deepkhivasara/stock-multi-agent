# 📊 Stock Multi-Agent System

This project is built as part of an internship task to develop a multi-agent system for stock analysis using Python.

## 🚀 Features

- Identify stock ticker from company name
- Fetch current stock price
- Calculate price change over time
- Fetch recent stock-related news
- Analyze price movement using news + data

## 🧠 Subagents

| Subagent Name         | Functionality                         |
|-----------------------|----------------------------------------|
| `identify_ticker`     | Converts "Tesla" → "TSLA"              |
| `ticker_price`        | Gets current price from Alpha Vantage |
| `ticker_price_change` | Calculates change in price over days  |
| `ticker_news`         | Gets recent news from Alpha Vantage   |
| `ticker_analysis`     | Combines price + news for insight     |
