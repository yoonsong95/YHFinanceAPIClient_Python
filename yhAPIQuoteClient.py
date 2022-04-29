
# newiyo5137@wowcg.com - YH API

import requests


def getQuote(apiKey, *symbols):
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols": f"{','.join(symbols)}"}
    headers = {'x-api-key': apiKey}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    return result["quoteResponse"]["result"]


def quoteResultToList(quoteResult):
    stockList = []
    for stockResult in quoteResult:
        s = Stock(stockResult["shortName"], stockResult["symbol"], stockResult["regularMarketPrice"], stockResult["currency"], stockResult["fiftyDayAverage"], stockResult["regularMarketVolume"])
        stockList.append(s)
    return stockList
    
    
class Stock:
    def __init__(self, shortName, symbol, price, currency, fiftyDayAverage, volume):
        self.name = shortName
        self.symbol = symbol
        self.currency = currency
        self.price = price
        self.fiftyDayAverage = fiftyDayAverage
        self.volume = volume
        
    def displayInfo(self):
        print("Company Name:", self.name)
        print("Ticker:", self.symbol)
        print("Currency:", self.currency)
        print("Price:", self.price)
        print("Fifty Day Average:", self.fiftyDayAverage)
        print("Volume:", self.volume)


apiKey = "Replace this string with API Key"
quoteResult = getQuote(apiKey, "MSFT", "NVDA", "AMD", "UBER")
stockList = quoteResultToList(quoteResult)


for stock in stockList:
    stock.displayInfo()
    print()