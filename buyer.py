import datetime
import sys
import time
import ConfigParser
from cryptopia_api import Api
import math 

config = ConfigParser.ConfigParser()
config.read("setup.ini")

if (config.get("TERMS", "USE") == "FALSE"):
    sys.exit("!!!!WARNING!!!!!! \n\nFOR YOUR SECURUTE YOU NEED AUTHORIZE IN SETUP.INI")

bit = Api(config.get("API", "key"), config.get("API", "secret"))

if(bit.get_market("MAGN_BTC")[1] != None):
    print(bit.get_market("MAGN_BTC")[1])
    sys.exit("!!!!WARNING!!!!!!\n\n")
    
    


myBalanceBtc = float(sys.argv[1])

coinMarketStart = raw_input("COIN INITIALS: ")
tempo = time.time()
coinMarket = coinMarketStart.upper() + "_BTC"
a = time.time()
priceActual = bit.get_market(coinMarket)[0]['LastPrice']
print("[INFO] - " + str(time.time() - a) + ' - CHECK LAST PRICE')
priceFuture = priceActual * float(config.get("BUY", "FACTOR"))
amount = myBalanceBtc / float(priceFuture)
amount = amount - amount * 0.01
priceSell = 0.0005 / amount

# a = time.time()
# print(bit.submit_trade(coinMarket, 'Buy',priceFuture,amount))
# print("[INFO] - " + str(time.time() - a) + ' - BUYING')

print(
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - BALANCE: " + str(myBalanceBtc))
print(
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - LAST PRICE: " + str(
        priceActual))
print("[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - BUY ORDER PRICE: " + str(
    priceFuture))
print(
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - AMOUNT TO BUY: " + str(amount))
print(
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - SELL PRICE 15: " + "{0:.15f}".format(priceSell))
print(
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - SELL PRICE 08: " + "{0:.8f}".format(priceSell+.00000001))
print(
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(time.time() - tempo) + " - BTC TOTAL: " + str(priceSell*amount))

if(config.get("SELL", "AUTO") == "TRUE"):
    a = time.time()
    print(bit.submit_trade(coinMarket, 'Sell',priceActual * float(config.get("SELL", "PERCENT")),amount))
    print("[INFO] - " + str(time.time() - a) + ' - ORDER WITH 20 PERCENT TO SELL')

raw_input("PRESS [ENTER] TO CANCEL ORDER AND EMERGENCY SELL")

if(config.get("SELL", "AUTO") == "TRUE"):
    a = time.time()
    print(bit.cancel_all_trade())
    print("[INFO] - " + str(time.time() - a) + ' - CANCELLING ORDERS')


a = time.time()
print(bit.submit_trade(coinMarket, 'Sell',priceSell+0.00000001,amount))
print("[INFO] - " + str(time.time() - a) + ' - QUICK SELL')
