#Coder: codingdudepy
#function: Create a terminal based stock notifier program for mac, windows, and ios. Going to add gui soon with tkinter


#import packages colorama not used yet
import os
import requests 
import yfinance as yf
import colorama 
from colorama import Fore
import time


#Need to create oop functionality for user handling




print("""
███████ ████████  ██████   ██████ ██   ██     ████████ ██████   █████   ██████ ██   ██ ███████ ██████  
██         ██    ██    ██ ██      ██  ██         ██    ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
███████    ██    ██    ██ ██      █████          ██    ██████  ███████ ██      █████   █████   ██████  
     ██    ██    ██    ██ ██      ██  ██         ██    ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
███████    ██     ██████   ██████ ██   ██        ██    ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ 
                                                                                                       
                                                                                                                                                                                                                                           """)
print("\n")
print("\n")


print("Welcome to my stock terminal client tracker made by codingdudepy")
print("\n")
option_choice_one = input("Please enter the stock ticker you would like to track. i.e = (Tesla= TSLA): ")
option_choice_two = input("How time intervals would you like to be alerted with(in minutes minumum is 2):  ")

opt_choice_two = int(option_choice_two)
if opt_choice_two < 2:
    quit()

stock_info = yf.Ticker(option_choice_one).info
thenews = (option_choice_one).news
print(thenews)
market_price = stock_info['regularMarketPrice']

while True:
    title = "Price Update"
    message = f"Stock Price is: {market_price} "
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)
    conversionofopt = opt_choice_two*60
    time.sleep(conversionofopt)

