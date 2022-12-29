from multiprocessing.sharedctypes import Value
from optparse import Values
import re, requests, ast
from prompt_toolkit import print_formatted_text
import RPi.GPIO as GPIO
import time
from heapq import nsmallest
import schedule
import pip._vendor.requests
import re

#Ange billigaste antal timmar per dygn att köpa el i HoursPerDay
#Ange maxpris i öre för att ständigt köpa el i PriceLimit

HoursPerDay = 10
PriceLimit = 40

############### !!!! GPIO can only be active in code on Raspberry platform !!!!! ####################
GPIO.setmode(GPIO.BCM) #mode for the type of pin board you use
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #set initial output on pin 18 start low volt



#get scrape from site
def scrape():
    r = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
    print("Lowify is running - Today's price range is collected.")
    print("Updated")
    return dict(zip([i[0] for i in re.findall(r"'((2[0-4]|[01]?[0-9]):([0-5]?[0-9]))'", r.text)],
            ast.literal_eval(re.search(r"data: .*(\[.*?\])[\s\S]+(?='Idag snitt')", r.text).group(1))))
    

fixed_scrape = scrape()


#find the cheapest hours, set hours in nsmallest
def cheap():
    my_dict = fixed_scrape 
    cheapest_hour = nsmallest(HoursPerDay, my_dict, key=my_dict.get)
    return [re.sub(r'0+(.+)', r'\1', i.rstrip('0').rstrip(':')) for i in cheapest_hour]


#find if price is under a certain thres
def threshold():
    price_hour = fixed_scrape
    price_hour = {k:v for k,v in price_hour.items() if v < PriceLimit}
    dick = nsmallest(24, price_hour, key=price_hour.get)
    return [re.sub(r'0+(.+)', r'\1', i.rstrip('0').rstrip(':')) for i in price_hour]


#schedules new scrape with  prices from site every day
#schedule.every().day.at("00:10").do(scrape)

#run the program
while True:
    #schedule.run_pending()
    now_time = time.strftime("%H") #update time in loop
    now_time = re.sub("^0+(?!$)", "", now_time)
    scrape_time = time.strftime("%H:%M") #set daily time for scrape
    if scrape_time == '00:15':
        fixed_scrape = scrape()
        print("Daily scrape is done - pricerange updated")
    
    
    #print(now_time)
    cheapest_hours = cheap()
    cheap_threshold = threshold()
    print(cheapest_hours, "Are the cheapest hours today")
    print(cheap_threshold, "Hours when price is under" , PriceLimit, "öre/kwh. (Buying on threshold)")
    
    
    print("Active hour now is: ",now_time)
    
    if now_time in cheap_threshold:
        print("Buying cheap electricity by threshold")
        GPIO.output(18, GPIO.HIGH)

    elif now_time in cheapest_hours:
        print("Buying cheap elecricity on low hour price right now")
        GPIO.output(18, GPIO.HIGH)

    else:
        print("Right now electricity is to expensive to buy.")
        GPIO.output(18, GPIO.LOW) 

    time.sleep(30) #sets time between time check / loop in seconds
    



#Rasberry Pi setup code
# https://www.youtube.com/watch?v=U6N5pRDOrg4&t=607s VIDEO tutorial for coding
#GPIO.setmode(GPIO.BCM) '''mode for the type of pin board you use'''
#GPIO.setwarnings(False)

#GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) '''set initial output on pin 18 start low volt'''
#GPIO.output(18, GPIO.HIGH) '''put 5 volt current on pin 18'''
#GPIO.output(18, GPIO.LOW) '''return current on pin 18 to 0 volt'''








