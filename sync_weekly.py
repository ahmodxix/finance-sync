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
    data = ticker.institution_ownership

    if hasattr(data, "to_dict"):
        data = data.to_dict()

    payload["institution_ownership"] = data

except Exception as e:
    print("institution_ownership", e)




try:
    data = ticker.fund_ownership

    if hasattr(data, "to_dict"):
        data = data.to_dict()

    payload["fund_ownership"] = data

except Exception as e:
    print("fund_ownership", e)




try:
    data = ticker.major_holders

    if hasattr(data, "to_dict"):
        data = data.to_dict()

    payload["major_holders"] = data

except Exception as e:
    print("major_holders", e)




try:
    data = ticker.insider_transactions

    if hasattr(data, "to_dict"):
        data = data.to_dict()

    payload["insider_transactions"] = data

except Exception as e:
    print("insider_transactions", e)

r = requests.post(URL, json=payload)

print(r.status_code)
print(r.text)
