from yahooquery import Ticker
import requests

FINANCE_FUNCTION_URL = \
    "https://savefinancedata-aely4ywg2a-uc.a.run.app"

stocks = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "AMZN",
    "GOOG",
    "META"
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
    "company_profiles": {},
    "summary": {}
}

# STOCKS
stock_ticker = Ticker(stocks)

prices = stock_ticker.price

for symbol in stocks:
    payload["stocks"][symbol] = prices.get(symbol, {})

# COMPANY PROFILES
profiles = stock_ticker.asset_profile

for symbol in stocks:
    payload["company_profiles"][symbol] = \
        profiles.get(symbol, {})

# SUMMARY
summary = stock_ticker.summary_detail

for symbol in stocks:
    payload["summary"][symbol] = \
        summary.get(symbol, {})

# CRYPTO
crypto_ticker = Ticker(crypto)

crypto_prices = crypto_ticker.price

for symbol in crypto:
    payload["crypto"][symbol] = \
        crypto_prices.get(symbol, {})

# INDICES
index_ticker = Ticker(indices)

index_prices = index_ticker.price

for symbol in indices:
    payload["indices"][symbol] = \
        index_prices.get(symbol, {})

# SEND TO FIREBASE

response = requests.post(
    FINANCE_FUNCTION_URL,
    json=payload,
    timeout=60
)

print("STATUS:", response.status_code)
print(response.text)
