import requests
from configuration import *
from data import *


def create_new():
    return requests.post(URL + CREATE_AN_ORDER,
                         json=creating_an_order).json()['track']

cn = create_new()
cn_s = str(cn)


# cn_l = list(cn)
#
# def copy_cn():
#     cop = cn_l.copy()
#     return cop


# в задании было сохронить, какой ТЗ такой ХЗ.
track = open('track.txt', 'w')
track.write(cn_s)
track.close()







def test_accept_the_order():
    return requests.get(URL + ACCEPT_THE_ORDER + cn_s).status_code
