#from sense_hat import SenseHat
import time
import requests

api_link = 'https://terraapi.azurewebsites.net/api/'

#sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)


#warns
no_warn = True
too_warm = False
too_cold = False
too_humid = False
too_dry = False

#displays
def ok_disp():
        N = nothing
        G = green

        f1 = [
        N, N, N, N, N, N, N, N,
        G, G, G, G, N, G, N, G,
        G, N, N, G, N, G, G, N,
        G, N, N, G, N, G, N, N,
        G, N, N, G, N, G, G, N,
        G, G, G, G, N, G, N, G,
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,  
        ]

        return f1

def too_warm_disp():
        R = red
        N = nothing
        
        f1 = [
        N, N, N, N, N, N, N, N,
        N, N, N, R, R, N, N, N,
        N, N, N, R, R, N, N, N,
        N, N, R, R, R, R, N, N,
        N, N, R, R, R, R, N, N,
        N, R, R, R, R, R, R, N,
        N, R, R, R, R, R, R, N,
        N, N, R, R, R, R, N, N,  
        ]

        return f1

def too_cold_disp():
        O = nothing
        B = blue
        
        f1 = [
        B, O, O, O, O, O, O, B,
        O, B, O, B, B, O, B, O,
        O, O, B, O, O, B, O, O,
        O, B, O, B, B, O, B, O,
        O, B, O, B, B, O, B, O,
        O, O, B, O, O, B, O, O,
        O, B, O, B, B, O, B, O,
        B, O, O, O, O, O, O, B,  
        ]

        return f1

def too_humic_disp():
        O = nothing
        B = blue

        f1 = [
        O, O, O, B, B, O, O, O,
        O, O, O, B, B, O, O, O,
        O, O, B, B, B, B, O, O,
        O, O, B, B, B, B, O, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        O, O, B, B, B, B, O, O,
        O, O, O, B, B, O, O, O,  
        ]

        return f1

def too_dry_disp():
        Y = yellow
        N = nothing

        f1 = [
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,
        Y, Y, Y, Y, Y, Y, Y, Y,  
        ]

        return f1

def main_loop():
    while True:
        print('Checking status and settings...')
        #check_warns()
        #draw_warns()
        #get_setting()
        post_status()
        time.sleep(600000)

def post_status():
    #data = {'isDay' : False, 'temp' : sense.temp, 'humid' : sense.humidity, 'light' : True}
    datadebug = {"isDay" : 0, "temp" : 30.0, "humid" : 40.1, "light" : 1}
    r = requests.post(api_link + 'status/', data=datadebug)
    print(r)
    print(datadebug)

def get_setting():
    pass 

def check_warns():
        pass

main_loop()