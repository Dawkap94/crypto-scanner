import time

from easygui import *
from PriceNow import crypto_details
from PriceNow import check_price

k = multenterbox("Please enter the name of the cryptocurrency and the refresh time." , "PriceNow",
             ["Crypto name:", "Refresh time (seconds):"], [], None, True)
crypto = k[0]
sleep_time = int(k[1])
crypto_details(crypto)

def crypto_scanner(crypto: str):
    print(f"The cryptocurrency you have chosen last 24h min/max value was: {crypto_details(crypto)[2]} / {crypto_details(crypto)[3]}")
    while True:
        print(check_price(crypto))
        time.sleep(sleep_time)

crypto_scanner(crypto)