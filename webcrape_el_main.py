import requests

web_spotprice = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
web_spotprice_raw = web_spotprice.content
print(web_spotprice_raw)
