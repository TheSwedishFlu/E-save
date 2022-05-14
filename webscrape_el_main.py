import re, requests, ast
from prompt_toolkit import print_formatted_text
#import RPi.GPIO as GPIO
import time
from heapq import nsmallest
import schedule

#Scrape data from website on start up
r = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
fixed_scrape = dict(zip([i[0] for i in re.findall(r"'((2[0-4]|[01]?[0-9]):([0-5]?[0-9]))'", r.text)],
            ast.literal_eval(re.search(r"data: .*(\[.*?\])[\s\S]+(?='Idag snitt')", r.text).group(1))))
#print(fixed_scrape)


#find the 8 cheapest hours
my_dict = fixed_scrape 
cheapest_hours = nsmallest(8, my_dict, key=my_dict.get)
print(cheapest_hours) 


#strip minutes away from hours
cheapest_hours = [i.strip(':00') for i in cheapest_hours]

print(cheapest_hours)

#import hour for time update
now_time = time.strftime("%H")
print(now_time)



#renew fixed_scrape every day / try time here
def scrape():
    r = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
    fixed_scrape = dict(zip([i[0] for i in re.findall(r"'((2[0-4]|[01]?[0-9]):([0-5]?[0-9]))'", r.text)],
            ast.literal_eval(re.search(r"data: .*(\[.*?\])[\s\S]+(?='Idag snitt')", r.text).group(1))))
    print(fixed_scrape)
    return fixed_scrape
schedule.every().day.at("00:05").do(scrape)




while True:
    schedule.run_pending()
    time.sleep(30)
    if now_time in cheapest_hours:
        print(True)
        #GPIO.output(18, GPIO.HIGH) '''put 3.3 volt current on pin 18'''

    else:
        print(False)
        #GPIO.output(18, GPIO.LOW) '''return cullert on pin 18 to 0 volt'''
    
    



#Rasberry Pi setup code
# https://www.youtube.com/watch?v=U6N5pRDOrg4&t=607s VIDEO tutorial for coding
#GPIO.setmode(GPIO.BCM) '''mode for the type of pin board you use'''
#GPIO.setwarnings(False)

#GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) '''set initial output on pin 18 start low volt'''
#GPIO.output(18, GPIO.HIGH) '''put 3.3 volt current on pin 18'''
#GPIO.output(18, GPIO.LOW) '''return cullert on pin 18 to 0 volt'''








