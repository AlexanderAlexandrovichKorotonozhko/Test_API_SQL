import requests
import configuration
import data


def create_new():
    return requests.post(configuration.URL + configuration.CREATE,
                         json=data.creating_an_order)


def get_track(create_track_response):
    return create_track_response.json()["track"]
# print(get_track(create_new()))
