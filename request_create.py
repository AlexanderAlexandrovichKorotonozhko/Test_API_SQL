import requests
import configuration
import data


def create_new():
    return requests.post(configuration.URL + configuration.CREATE_AN_ORDER,
                         json=data.creating_an_order).json()["track"]


#
# def get_track(create_track_response):
#     return create_track_response.json()["track"]
# # get_track_create_new = get_track(create_new())
print(copy_create_new)
# # print(get_track_create_new)
