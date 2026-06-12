from yahooquery import Ticker
import requests

URL = "https://savefinancedata-aely4ywg2a-uc.a.run.app"

stocks = [
    "AAPL","MSFT","NVDA","TSLA",
    "AMZN","GOOG","META"
]

ticker = Ticker(stocks)

payload = {
    "recommendations": {},
    "financials": {},
    "earnings": {},
    "options": {},
    "sec_filings": {}
}

try:
    payload["recommendations"] = \
        ticker.recommendation_trend
except:
    pass

try:
    payload["earnings"] = \
        ticker.earnings
except:
    pass

try:
    payload["financials"] = \
        ticker.summary_detail
except:
    pass

try:
    payload["sec_filings"] = \
        ticker.sec_filings
except:
    pass

r = requests.post(URL, json=payload)

print(r.status_code)
print(r.text)
