import re, requests, ast
from prompt_toolkit import print_formatted_text
#import RPi.GPIO as GPIO
import time
from heapq import nsmallest

#Import data from website

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

#import hour
now_time = time.strftime("%H")
print(now_time)

#loop for check time for on and off
while now_time not in cheapest_hours:
    #GPIO.output(18, GPIO.HIGH)
    print('ON')
else:
    print('OFF')
    
    



#Rasberry Pi setup code
# https://www.youtube.com/watch?v=U6N5pRDOrg4&t=607s VIDEO tutorial for coding
#GPIO.setmode(GPIO.BCM) '''mode for the type of pin board you use'''
#GPIO.setwarnings(False)

#GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) '''set initial output on pin 18 start low volt'''
#GPIO.output(18, GPIO.HIGH) '''put 3.3 volt current on pin 18'''
#GPIO.output(18, GPIO.LOW) '''return cullert on pin 18 to 0 volt'''








