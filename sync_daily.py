from yahooquery import Ticker
import requests
import json
import math

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
    "recommendations": {},
    "financials": {},
    "earnings": [],
    "sec_filings": []
}


def clean_data(obj):

    if isinstance(obj, dict):
        return {
            str(k): clean_data(v)
            for k, v in obj.items()
        }

    elif isinstance(obj, list):
        return [
            clean_data(x)
            for x in obj
        ]

    elif isinstance(obj, tuple):
        return str(obj)

    elif isinstance(obj, float):

        if math.isnan(obj):
            return None

        if math.isinf(obj):
            return None

        return obj

    return obj


def safe_convert(data):

    try:

        if hasattr(data, "reset_index"):
            data = data.reset_index()

        if hasattr(data, "to_dict"):
            data = data.to_dict(orient="records")

        return clean_data(data)

    except Exception as e:

        print("convert error:", e)

        return []


# Recommendations
try:

    payload["recommendations"] = clean_data(
        ticker.recommendation_trend
    )

    print("recommendations OK")

except Exception as e:

    print("recommendations error:", e)


# Financials
try:

    payload["financials"] = clean_data(
        ticker.summary_detail
    )

    print("financials OK")

except Exception as e:

    print("financials error:", e)


# Earnings
try:

    payload["earnings"] = safe_convert(
        ticker.earnings
    )

    print("earnings OK")

except Exception as e:

    print("earnings error:", e)


# SEC Filings
try:

    payload["sec_filings"] = safe_convert(
        ticker.sec_filings
    )

    print("sec filings OK")

except Exception as e:

    print("sec filings error:", e)


payload = clean_data(payload)

json.dumps(payload, allow_nan=False)

print("JSON VALID")

response = requests.post(
    URL,
    json=payload,
    timeout=120
)

print("STATUS:", response.status_code)
print(response.text)
