import requests
import configuration
import data
import request


def selection_track(track):
    url_track = configuration.RECEIVE + track
    return url_track



# new_user_response = sender_stand_request.create_new_user()
# auth_headers = sender_stand_request.get_auth_headers(sender_stand_request.get_user_token(new_user_response))
#
#
# def create_kit(kz):
#     return requests.post(configuration.URL + configuration.CREATE_KIT, json=kz,
#                          headers=auth_headers)
#
#
# # ПОЗИТИВ
# def poz_test(t):
#     kit_body_poz_zap = create_kit(t).json()['name']
#     kit_body_poz_stat = create_kit(t).status_code
#     assert kit_body_poz_stat == 201
#     assert kit_body_poz_zap == t['name']
#
#
# # НEГАТИВ
# def nega_test(t):
#     kit_body_nega = create_kit(t).status_code
#     assert kit_body_nega == 400
























#
# def get_kit_body(kit_name):
#     current_body = data..copy()
#     current_body["name"] = kit_name
#     return current_body
#
#
# new_user_response = sender_stand_request.create_new_user()
# auth_headers = sender_stand_request.get_auth_headers(sender_stand_request.get_user_token(new_user_response))
#
#
# def create_kit(kz):
#     return requests.post(configuration.URL + configuration.CREATE_KIT, json=kz,
#                          headers=auth_headers)
#
#
# # ПОЗИТИВ
# def poz_test(t):
#     kit_body_poz_zap = create_kit(t).json()['name']
#     kit_body_poz_stat = create_kit(t).status_code
#     assert kit_body_poz_stat == 201
#     assert kit_body_poz_zap == t['name']
#
#
# # НEГАТИВ
# def nega_test(t):
#     kit_body_nega = create_kit(t).status_code
#     assert kit_body_nega == 400

