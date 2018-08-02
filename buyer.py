import datetime
import sys
import time
import ConfigParser
from bittrex import Bittrex
from cryptopia_api import Api

config = ConfigParser.ConfigParser()
config.read("setup.ini")

if (config.get("TERMS", "USE") == "FALSE"):
    sys.exit("!!!!WARNING!!!!!! \n\nFOR YOUR SECURUTE YOU NEED AUTHORIZE IN SETUP.INI")

bit = Api(config.get("API", "key"), config.get("API", "secret"))

myBalanceBtc = float(sys.argv[1])

coinMarketStart = raw_input("COIN INITIALS: ")
tempo = time.time()
coinMarket = coinMarketStart.upper() + "_BTC"
priceActual = bit.get_market(coinMarket)[0]['LastPrice']
priceFuture = priceActual * float(config.get("BUY", "FACTOR"))
amount = myBalanceBtc / float(priceFuture)
amount = amount - amount * 0.01
priceSell = 0.0005 / amount

# print(bit.buy_limit(coinMarket, amount, priceFuture))
# print(bit.submit_trade(coinMarket, 'Buy',priceFuture,amount))

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
    "[INFO] - " + str(datetime.datetime.now()) + " - " + str(
        time.time() - tempo) + " - SELL PRICE: " + '{0:.15f}'.format(
        priceSell))

# bit.sell_limit(coinMarket, amount, priceActual * float(config.get("SELL", "PERCENT")))
# bit.submit_trade(coinMarket, 'Sell', priceActual * float(config.get("SELL", "PERCENT"), amount))

raw_input("PRESS [ENTER] TO CANCEL ORDER AND EMERGENCY SELL")

orders = bit.get_openorders(coinMarket)[0]['result']
# for cancelOrder in orders:
#     uuid = cancelOrder['OrderUuid']
#     bit.cancel(uuid)
#     print("[ORDER CANCEL] - " + uuid)

# print(bit.sell_limit(coinMarket, amount, priceSell))
