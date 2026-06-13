from yahooquery import Ticker
import requests

URL = "https://savefinancedata-aely4ywg2a-uc.a.run.app"

stocks = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "AMZN",
    "GOOG",
    "META",
    "NFLX",
    "AMD",
    "PLTR",
    "JPM",
    "BAC",
    "KO",
    "PEP",
    "NKE",
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
]

crypto = [
    "BTC-USD",
    "ETH-USD",
    "BNB-USD",
    "SOL-USD",
    "XRP-USD",
    "DOGE-USD",
    "ADA-USD",
]

indices = [
    "^GSPC",
    "^DJI",
    "^IXIC",
    "^NSEI",
    "^BSESN",
]

payload = {
    "stocks": {},
    "crypto": {},
    "indices": {},
    "market_news": []
}

# STOCKS
stock_ticker = Ticker(stocks)

for symbol, data in stock_ticker.price.items():
    payload["stocks"][symbol] = data

# CRYPTO
crypto_ticker = Ticker(crypto)

for symbol, data in crypto_ticker.price.items():
    payload["crypto"][symbol] = data

# INDICES
index_ticker = Ticker(indices)

for symbol, data in index_ticker.price.items():
    payload["indices"][symbol] = data

# NEWS
try:
    news = stock_ticker.news()

    cleaned_news = []

    for item in news[:50]:
        cleaned_news.append({
            "title": item.get("title", ""),
            "publisher": item.get("publisher", ""),
            "link": item.get("link", ""),
            "published": item.get("providerPublishTime", 0),
            "thumbnail": item.get("thumbnail", {})
        })

    payload["market_news"] = cleaned_news

except Exception as e:
    print("News Error:", e)

r = requests.post(
    URL,
    json=payload,
    timeout=120
)

print("STATUS:", r.status_code)
print(r.text)
