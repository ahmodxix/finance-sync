from yahooquery import Ticker

stocks = ["AAPL", "MSFT", "NVDA", "TSLA"]

ticker = Ticker(stocks)

print("PRICE")
print(ticker.price)

print("PROFILE")
print(ticker.asset_profile)

print("SUMMARY")
print(ticker.summary_detail)

print("ESG")
print(ticker.esg_scores)

print("RECOMMENDATIONS")
print(ticker.recommendation_trend)
