ltcinfo
=======

Returns Litecoin info such as difficulty, hashrate, your LTC balance, etc.

This uses the API provided by ltcd.info for LTC network info, litecoin explorer to get your balance, and BTC-e for prices.

You need the grequests module installed in order to run this script.  It utilizes async HTTP requests, which was
deprecated in the requests module awhile ago.

Change the last address in the urls to your LTC address: http://explorer.litecoin.net/address/your-address-here (the one in the script is my address).

If you'd like to donate:

BTC: 1J1R19Lztcw97NLWrqvhPL37vHbTDf1Ws1
LTC: LUdqJU4uqEkLFKzHh9r3fxSnW74fKFRhEC
