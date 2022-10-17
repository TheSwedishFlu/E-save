# WebScraping electricity prices - buy only electricity when it's cheap

Python / Rasberry Pi project #inProgress

**This program is buying electicity for your home/house/business in the hours when it's cheapest.
Rasberry Pi turn on/off electrical relay on big elecrical consumers and turn them off in the hours
when the electricity are most expensive**


Right now it collecting the daily electricity price and sort out the cheapest hours. You can set how many hours you want to buy.
If you select 1 hour you get the cheapest hour that day, if you select 4 hours you get the 4 cheapest hours out of the 24 and so on.
Filter out from cheapest to most expensive the more hours you put in.

You can also set threshold for a price when you always want to buy depending of the size of your wallet.
for example always buy when the price is under 50 öre.

**Code planning**

1. Server solution.
2. Multiple users / accounts.
3. Web gui.


