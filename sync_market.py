from yahooquery import Ticker
import requests

URL = "https://savefinancedata-aely4ywg2a-uc.a.run.app"

stocks = [
    "AAPL","MSFT","NVDA","TSLA",
    "AMZN","GOOG","META"
]

crypto = [
    "BTC-USD",
    "ETH-USD",
    "BNB-USD",
    "SOL-USD"
]

indices = [
    "^GSPC",
    "^DJI",
    "^IXIC",
    "^NSEI",
    "^BSESN"
]

payload = {
    "stocks": {},
    "crypto": {},
    "indices": {},
    "market_news": []
}

# STOCKS
ticker = Ticker(stocks)

for s, v in ticker.price.items():
    payload["stocks"][s] = v

# CRYPTO
ct = Ticker(crypto)

for s, v in ct.price.items():
    payload["crypto"][s] = v

# INDICES
it = Ticker(indices)

for s, v in it.price.items():
    payload["indices"][s] = v

# NEWS
try:
    news = ticker.news()
    payload["market_news"] = news
except:
    pass

r = requests.post(URL, json=payload, timeout=120)

print(r.status_code)
print(r.text)
