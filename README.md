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

Sample output
=======

Stats grabbed on Tue May 28 15:14:09 2013 from ltcd.info and prices from BTC-e

LTC Current difficulty: 602

Next difficulty: 641 (6.57%)

Next difficulty change: 05-31-2013 19:45:07 - in 76.52 hours

Network hashrate: 17.14 Gh/s

Balance is 424.47 LTC @ 3.0234 [Vol: 263266] = 1283.32


License
=======

All material copyright 2013, prochobo

All code is licensed under the <a href="http://www.opensource.org/licenses/mit-license.php">MIT License</a>.
