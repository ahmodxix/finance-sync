import requests

FINNHUB_API_KEY = "d7cjehhr01qv03esj040d7cjehhr01qv03esj04g"

SAVE_NEWS_URL = "https://savenews-aely4ywg2a-uc.a.run.app"

url = (
    f"https://finnhub.io/api/v1/news"
    f"?category=general"
    f"&token={FINNHUB_API_KEY}"
)

response = requests.get(url)
news_items = response.json()

for item in news_items[:100]:

    payload = {
        "title": item.get("headline", ""),
        "imageUrl": item.get("image", ""),
        "category": item.get("category", "Markets"),
        "articleUrl": item.get("url", ""),
        "source": item.get("source", ""),
        "publishedAt": str(
            item.get("datetime", 0)
        )
    }

    try:
        r = requests.post(
            SAVE_NEWS_URL,
            json=payload,
            timeout=30
        )

        print(
            payload["title"][:50],
            r.status_code
        )

    except Exception as e:
        print(e)
