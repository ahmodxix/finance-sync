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
    "esg": {},
    "institution_ownership": [],
    "fund_ownership": [],
    "major_holders": [],
    "insider_transactions": []
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

        # DataFrame
        if hasattr(data, "reset_index"):
            data = data.reset_index()

        # Convert dataframe to records
        if hasattr(data, "to_dict"):
            data = data.to_dict(orient="records")

        return clean_data(data)

    except Exception as e:

        print("convert error:", e)

        return []


# ESG
try:

    esg = ticker.esg_scores

    payload["esg"] = clean_data(esg)

    print("ESG OK")

except Exception as e:

    print("esg error:", e)


# Institution Ownership
try:

    payload["institution_ownership"] = safe_convert(
        ticker.institution_ownership
    )

    print("institution ownership OK")

except Exception as e:

    print("institution ownership error:", e)


# Fund Ownership
try:

    payload["fund_ownership"] = safe_convert(
        ticker.fund_ownership
    )

    print("fund ownership OK")

except Exception as e:

    print("fund ownership error:", e)


# Major Holders
try:

    payload["major_holders"] = safe_convert(
        ticker.major_holders
    )

    print("major holders OK")

except Exception as e:

    print("major holders error:", e)


# Insider Transactions
try:

    payload["insider_transactions"] = safe_convert(
        ticker.insider_transactions
    )

    print("insider transactions OK")

except Exception as e:

    print("insider transactions error:", e)


# Final cleanup
payload = clean_data(payload)

# Verify JSON before sending
json.dumps(payload, allow_nan=False)

print("JSON VALID")

# Send to Firebase
response = requests.post(
    URL,
    json=payload,
    timeout=120
)

print("STATUS:", response.status_code)
print(response.text)
