from yahooquery import Ticker

ticker = Ticker("AAPL")

print("PRICE")
print(type(ticker.price))

print("PROFILE")
print(type(ticker.asset_profile))

print("SUMMARY")
print(type(ticker.summary_detail))
