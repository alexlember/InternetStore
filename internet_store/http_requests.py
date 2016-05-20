# coding=utf-8
import urllib
import urllib2

import requests


def send_delivery(delivery):
    #r = requests.post(url='http://localhost:9000/delivery', data={'хуй':'пизда'}, )
    post_data = [('name', 'Gladys'), ]     # a sequence of two element tuples
    result = urllib2.urlopen('http://localhost:8500/dhm/user/', urllib.urlencode(post_data))
    content = result.read()
    print('http call completed')

def reload_deliveries(user_email):
    pass    #r = requests.post(url='http://localhost:90000/delivery', data={'хуй':'пизда'}, )