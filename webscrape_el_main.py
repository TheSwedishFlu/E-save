import re, requests, ast
from prompt_toolkit import print_formatted_text
#import RPi.GPIO as GPIO
import time
from heapq import nsmallest
import schedule


############### !!!! GPIO can only be active in code on Raspberry platform !!!!! ####################
#GPIO.setmode(GPIO.BCM) #mode for the type of pin board you use
#GPIO.setwarnings(False)
#GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #set initial output on pin 18 start low volt



#get scrape from site
def scrape():
    r = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
    print("Daily Scrape is done")
    return dict(zip([i[0] for i in re.findall(r"'((2[0-4]|[01]?[0-9]):([0-5]?[0-9]))'", r.text)],
            ast.literal_eval(re.search(r"data: .*(\[.*?\])[\s\S]+(?='Idag snitt')", r.text).group(1))))
    
fixed_scrape = scrape()

#find the 8 cheapest hours
def cheap():
    my_dict = fixed_scrape 
    cheapest_hour = nsmallest(8, my_dict, key=my_dict.get)
    #strip minutes away from hours
    return [i.strip(':00') for i in cheapest_hour]

cheapest_hours = cheap()



#schedules new scrape with prices from site every day
schedule.every().day.at("00:05").do(scrape)



#run the program
while True:
    schedule.run_pending()
    time.sleep(10) #sets time between time check in seconds
    now_time = time.strftime("%H") #update time in loop
    cheapest_hours = cheap()
    print(cheapest_hours)
    
    #import hour for time
    now_time = time.strftime("%H")
    print(now_time)

    if now_time in cheapest_hours:
        print(True)
        #GPIO.output(18, GPIO.HIGH)

    else:
        print(False)
        #GPIO.output(18, GPIO.LOW) 
    
    



#Rasberry Pi setup code
# https://www.youtube.com/watch?v=U6N5pRDOrg4&t=607s VIDEO tutorial for coding
#GPIO.setmode(GPIO.BCM) '''mode for the type of pin board you use'''
#GPIO.setwarnings(False)

#GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) '''set initial output on pin 18 start low volt'''
#GPIO.output(18, GPIO.HIGH) '''put 5 volt current on pin 18'''
#GPIO.output(18, GPIO.LOW) '''return current on pin 18 to 0 volt'''