# WebScraping electricity prices - buy only electricity when it's cheap

Python / Rasberry Pi project #inProgress

**This program is buying electicity for your home/house/business in the hours when it's cheapest.
Rasberry Pi turn on/off electrical relay on big elecrical consumers and turn them off in the hours
when the electricity are most expensive**

**Code planning**

1. Getting daily price for electricity. /Done
2. Finding the 8 cheapest hours of 24 if the price is over max cost value. /Done
3. Timefunction for when to buy. /Done
4. Function for renewing price index exery day. /Done
5. Pin output on Rasberry if price is cheap or under max cost. (put on electricity relay). /Done
6. Override button. (If elecricity is needed on hours even when it's expensive) / In progress
7. Time reset/auto off for override button. Set to 8 hours if override function is still on / forgotten. /In progress


