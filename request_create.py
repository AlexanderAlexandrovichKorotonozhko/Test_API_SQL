# Александр Коротоножко, 7-я когорта - Финальный проект. Инженер по тестированию плюс

import requests
from configuration import *
from data import *


def create_new():                                                       # запрос на добавление заказа со сборкой эндпоинта и вычленением трека из ответа.
    return requests.post(URL + CREATE_AN_ORDER,
                         json=creating_an_order).json()['track']        # НА ВЫХОДЕ ГОТОВЫЙ ТРЕК В int!!!!!!!


cn = create_new()                                                       # создаем временную переменную чтобы потом
cn_s = str(cn)                                                          # ее содержимое преобразовать в str, иначе str не склеится с int.


def accept_the_order():                                                 # Это произведение искусства отвечает за сборку и гет запрос. А также вытаскивает статус код из ответа
    return requests.get(URL + ACCEPT_THE_ORDER + cn_s).status_code



def poz_requests():                                                     # здесь мы говорим что при выполнении функции accept_the_order() ответ должен быть равен 200
    poz_a = accept_the_order()
    assert poz_a == 200


def test_requests():                                                    # тест обращяется к функции poz_requests которая в свою очередь поднимает accept_the_order но для ее работы нужен трек который
    poz_requests()                                                      # она берет из переменной cn_s которая для свих монипуляций призывает функцию create_new. Так как-то в кратце.