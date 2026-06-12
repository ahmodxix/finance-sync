from yahooquery import Ticker
import requests

URL = "https://savefinancedata-aely4ywg2a-uc.a.run.app"

stocks = [
    "AAPL","MSFT","NVDA","TSLA",
    "AMZN","GOOG","META"
]

ticker = Ticker(stocks)

payload = {
    "esg": {},
    "institution_ownership": {},
    "fund_ownership": {},
    "major_holders": {},
    "insider_transactions": {}
}

try:
    payload["esg"] = ticker.esg_scores
except:
    pass

try:
    payload["institution_ownership"] = \
        ticker.institution_ownership
except:
    pass

try:
    payload["fund_ownership"] = \
        ticker.fund_ownership
except:
    pass

try:
    payload["major_holders"] = \
        ticker.major_holders
except:
    pass

try:
    payload["insider_transactions"] = \
        ticker.insider_transactions
except:
    pass

r = requests.post(URL, json=payload)

print(r.status_code)
print(r.text)
