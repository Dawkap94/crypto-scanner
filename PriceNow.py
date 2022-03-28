import datetime
from bs4 import BeautifulSoup
from requests import get

#checking current price in format for example: 02.04.2005 21:37:00 Cardano is 2,11. Rank #3

def check_price(crypto: str):
        URL = f"https://coinmarketcap.com/currencies/{crypto}/"
        page = get(URL)
        bs4_page = BeautifulSoup(page.content, features="html.parser")
        price = bs4_page.find("div", class_="priceValue").get_text()
        rank = bs4_page.find("div", class_="namePill namePillPrimary").get_text()
        return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {crypto.capitalize()} is {price}, {rank}"

#returs crypto data like price, rank, lowest and highest value in last 24h

def crypto_details(crypto: str):
        URL = f"https://coinmarketcap.com/currencies/{crypto}/"
        page = get(URL)
        bs4_page = BeautifulSoup(page.content, features="html.parser")
        price = bs4_page.find("div", class_="priceValue").get_text()
        rank = bs4_page.find("div", class_="namePill namePillPrimary").get_text()
        lowest = bs4_page.find("div", class_="sc-16r8icm-0 fmPyWa").get_text().split("$")
        best_price = lowest[4][:-17:]
        worst_price = lowest[3]
        crypto_list = [price, rank, worst_price, best_price]
        return crypto_list

