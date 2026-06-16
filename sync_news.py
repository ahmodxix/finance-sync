import requests
from datetime import datetime

FINNHUB_API_KEY = "d7cjehhr01qv03esj040d7cjehhr01qv03esj04g"

SAVE_NEWS_URL = "https://savenews-aelyywg2a-uc.a.run.app"

url = (
    f"https://finnhub.io/api/v1/news"
    f"?category=general"
    f"&token={FINNHUB_API_KEY}"
)

response = requests.get(url)
news_items = response.json()

print(f"Found {len(news_items)} articles")

for item in news_items:

    payload = {
        "title": item.get("headline", ""),
        "summary": item.get("summary", ""),
        "imageUrl": item.get("image", ""),
        "articleUrl": item.get("url", ""),
        "source": item.get("source", ""),
        "category": item.get("category", "Markets"),

        # ISO Date for Flutter
        "publishedAt": datetime.fromtimestamp(
            item.get("datetime", 0)
        ).isoformat(),
    }

    try:
        r = requests.post(
            SAVE_NEWS_URL,
            json=payload,
            timeout=30,
        )

        print(
            r.status_code,
            payload["title"][:60]
        )

    except Exception as e:
        print(e)
