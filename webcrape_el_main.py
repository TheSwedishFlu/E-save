import requests

web_spotpris = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
print(web_spotpris.text)