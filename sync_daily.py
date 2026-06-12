from yahooquery import Ticker
import requests
import json
import math
import pandas as pd

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

    # DataFrame
    if isinstance(obj, pd.DataFrame):
        return clean_data(
            obj.reset_index().to_dict(orient="records")
        )

    # Dict
    elif isinstance(obj, dict):
        return {
            str(k): clean_data(v)
            for k, v in obj.items()
        }

    # List
    elif isinstance(obj, list):
        return [
            clean_data(x)
            for x in obj
        ]

    # Tuple
    elif isinstance(obj, tuple):
        return str(obj)

    # Float
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
            data = data.to_dict(
                orient="records"
            )

        return clean_data(data)

    except Exception as e:

        print("convert error:", e)

        return []


# Recommendations
try:

    recommendations = ticker.recommendation_trend

    payload["recommendations"] = clean_data(
        recommendations
    )

    print("recommendations OK")

except Exception as e:

    print("recommendations error:", e)


# Financials
try:

    financials = ticker.summary_detail

    payload["financials"] = clean_data(
        financials
    )

    print("financials OK")

except Exception as e:

    print("financials error:", e)


# Earnings
try:

    earnings = ticker.earnings

    payload["earnings"] = safe_convert(
        earnings
    )

    print("earnings OK")

except Exception as e:

    print("earnings error:", e)


# SEC Filings
try:

    filings = ticker.sec_filings

    payload["sec_filings"] = safe_convert(
        filings
    )

    print("sec filings OK")

except Exception as e:

    print("sec filings error:", e)


# Final cleanup
payload = clean_data(payload)

# Debug
for key, value in payload.items():
    print(key, type(value))

# Validate JSON
json.dumps(
    payload,
    allow_nan=False
)

print("JSON VALID")

# Send to Firebase
response = requests.post(
    URL,
    json=payload,
    timeout=120
)

print("STATUS:", response.status_code)
print(response.text)
