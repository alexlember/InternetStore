# coding=utf-8
import requests


def send_delivery(delivery):
    r = requests.post(url='http://localhost:8500/delivery', data={'хуй':'пизда'}, )


def reload_deliveries(user_email):
    r = requests.post(url='http://localhost:8500/delivery', data={'хуй':'пизда'}, )