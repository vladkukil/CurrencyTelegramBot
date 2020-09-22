import requests
import json

res = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")

with open('../data/currencyExchange.json', 'w') as outf:
    json.dump(res.json(), outf)

with open('../data/currencyExchange.json') as json_file:
    data = json.load(json_file)

usd_buy = float(data[0]["buy"])
usd_sale = float(data[0]["sale"])
euro_buy = float(data[1]["buy"])
euro_sale = float(data[1]["sale"])
btc_buy = float(data[3]["buy"])
btc_sale = float(data[3]["sale"])
