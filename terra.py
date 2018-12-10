from sense_hat import SenseHat
import time
#import requests

api_link = 'https://terraapi.azurewebsites.net/api/'

sense = SenseHat()

def main_loop():
    while True:
        print('Checking status and settings...')
        post_status()
        get_setting()
        time.sleep(600000)

def post_status():
    data = {'isDay' : False, 'temp' : sense.temp, 'humid' : sense.humidity, 'light' : True}
    #r = requests.post(api_link + 'status/', data=data)
    print()


def get_setting():
    pass        

main_loop()