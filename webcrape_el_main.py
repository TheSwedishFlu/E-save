import re, requests, ast
import RPi.GPIO as GPIO
import time

#Import data from website

r = requests.get('https://www.elbruk.se/timpriser-se3-stockholm')
idag = dict(zip([i[0] for i in re.findall(r"'((2[0-4]|[01]?[0-9]):([0-5]?[0-9]))'", r.text)],
            ast.literal_eval(re.search(r"data: .*(\[.*?\])[\s\S]+(?='Idag snitt')", r.text).group(1))))

print(idag)


#Rasberry Pi setup code
# https://www.youtube.com/watch?v=U6N5pRDOrg4&t=607s VIDEO tutorial for coding
GPIO.setmode(GPIO.BCM) '''mode for the type of pin board you use'''
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) '''set initial output on pin 18 start low volt'''
GPIO.output(18, GPIO.HIGH) '''put 3.3 volt current on pin 18'''
GPIO.output(18, GPIO.LOW) '''return cullert on pin 18 to 0 volt'''








