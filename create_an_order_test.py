import requests
from configuration import *
from request_create import *
import copy


def copy_track():
     copy_track_order = copy.deepcopy(create_new())
     return copy_track_order

# def collect_an_order_receipt_request():
#
#
#     end_point = URL + CREATE_AN_ORDER #+ str(track)
#     # end_point += str(track)
#     return end_point
# # print(collect_an_order_receipt_request(123456))
print(copy_track)














#
# url_track = get_track(create_new())
# recive = RECEIVE + str(url_track)
# def accept_the_order():
#     return requests.get(URL + recive)
#
# poz_stat = accept_the_order().status_code
#
# print(poz_stat)