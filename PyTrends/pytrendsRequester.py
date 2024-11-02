from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)

pytrends.build_payload(['keyword1', 'keyword2'], cat=0, timeframe='today 5-y', geo='', gprop='')
interest_over_time = pytrends.interest_over_time()
print(interest_over_time)