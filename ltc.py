#!/usr/bin/python

from time import strftime, localtime
import grequests
import urllib2
import json
import re
import locale

urls = [
    'http://api.ltcd.info/difficulty',
    'http://api.ltcd.info/difficulty/next',
    'http://api.ltcd.info/difficulty/next/time',
    'http://api.ltcd.info/network/hashrate',
    'https://btc-e.com/api/2/ltc_usd/ticker',
    # Change the portion after "/address/" to your LTC wallet
    'http://explorer.litecoin.net/address/LUdqJU4uqEkLFKzHh9r3fxSnW74fKFRhEC'
]

# data list for storing URL JSON contents
data_list = []

# for each url, this method is applied.
def response_get(r):
	# If come across non JSON url. Must use if statement first, else the bad URL will
	# try to JSON load first.  Again, change the address to your LTC adddress.
	if r == 'http://explorer.litecoin.net/address/LUdqJU4uqEkLFKzHh9r3fxSnW74fKFRhEC':
		w = urllib2.urlopen(r)
		d = w.read()
		# open the url, use regex to search for my balance
		balance = re.findall(r'Balance: (\d+\.\d+)', d)
		# add it to the list of url JSON info
		data_list.append(float(balance[0]))
	# add each page's json data to the data_list
	else:
		data = json.load(urllib2.urlopen(r))
		data_list.append(data)

def print_data():
	# calculate hashrate
	hashrate = (float(data_list[3]['hashes-per-second'])) / 1024**3
	# Print stuff, sorry it's a little messy here.
	print '\nStats grabbed on ' + strftime("%c") + " from ltcd.info and prices from BTC-e\n"
	print 'LTC Current difficulty: %d' % data_list[0]['current-difficulty']
	print 'Next difficulty: %d (%.2f%%)' % (data_list[1]['next-difficulty'], ((data_list[1]['next-difficulty']/data_list[0]['current-difficulty']) - 1) * 100)
	print 'Next difficulty change: %s - in %.2f hours' % (strftime('%m-%d-%Y %H:%M:%S', localtime(data_list[2]['retarget-timestamp'])), data_list[2]['seconds-to-retarget'] / 3600.0)
	print 'Network hashrate: %.2f Gh/s\n' % hashrate
	print "Balance is %.2f LTC @ %.4f [Vol: %10s] = %.2f\n" % (data_list[5], data_list[4]['ticker']['last'], data_list[4]['ticker']['vol'], (data_list[5] * data_list[4]['ticker']['last']))

# use grequests.get to get the response from the page, then pass
# the url into response_get() to add the content to the data list.
# the hooks specify this.
rs = (grequests.get(u, hooks={'response' : response_get(u)}) for u in urls)
response = grequests.map(rs)

print_data()
