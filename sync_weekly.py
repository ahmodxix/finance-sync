from yahooquery import Ticker
import requests
import json

URL = "https://savefinancedata-aely4ywg2a-uc.a.run.app"

stocks = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "AMZN",
    "GOOG",
    "META"
]

ticker = Ticker(stocks)

payload = {
    "esg": {},
    "institution_ownership": {},
    "fund_ownership": {},
    "major_holders": {},
    "insider_transactions": {}
}

# ESG
try:
    payload["esg"] = ticker.esg_scores
except Exception as e:
    print("esg error:", e)

# Helper function
def safe_convert(data):
    try:

        if hasattr(data, "reset_index"):
            data = data.reset_index()

        if hasattr(data, "to_dict"):
            data = data.to_dict(orient="records")

        return data

    except Exception as e:
        print("convert error:", e)
        return []

# Institution Ownership
try:
    payload["institution_ownership"] = safe_convert(
        ticker.institution_ownership
    )
except Exception as e:
    print("institution_ownership error:", e)

# Fund Ownership
try:
    payload["fund_ownership"] = safe_convert(
        ticker.fund_ownership
    )
except Exception as e:
    print("fund_ownership error:", e)

# Major Holders
try:
    payload["major_holders"] = safe_convert(
        ticker.major_holders
    )
except Exception as e:
    print("major_holders error:", e)

# Insider Transactions
try:
    payload["insider_transactions"] = safe_convert(
        ticker.insider_transactions
    )
except Exception as e:
    print("insider_transactions error:", e)

# TEST JSON FIRST
json.dumps(payload)

print("JSON OK")

r = requests.post(
    URL,
    json=payload,
    timeout=120
)

print("STATUS:", r.status_code)
print(r.text)
