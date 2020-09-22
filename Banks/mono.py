import requests
import json

res = requests.get("https://api.monobank.ua/bank/currency")

with open('../data/currencyExchangeMono.json', 'w') as outf:
    json.dump(res.json(), outf)

with open('../data/currencyExchangeMono.json') as json_file:
    data = json.load(json_file)


zloty_buy = float(data[4]["rateBuy"])
zloty_sell = float(data[4]["rateSell"])
