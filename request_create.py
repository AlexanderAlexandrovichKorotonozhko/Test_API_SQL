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




# А вообще у меня сильно сгорело от задачи сохранить трек.
# Дело в том что метод .cpy не работает с неизменяемыми типами данных и как выяснилось с функциями запросов тоже,
# умники которые скажут что сохрани в переменную и там делай что хочешь могут идти читать про питон.
# Питон не сохраняет значение в переменную от дает переменной ссылку на объект.
# Поскольку я не нашел альтернативного способа сохранить переменную я сделал как сделал.
# Работает и ладно, я не настолько программист чтобы решать такие задачи, ну может в будущем.

# Подводные камни использования copy()
# Помимо различия между поверхностным и глубоким копированием,
# важно помнить, что не все типы данных в Python поддерживают метод copy().
# Например, числа, строки и кортежи являются неизменяемыми (immutable),
# и у них нет метода copy(). Попытка вызвать copy() у такого объекта приведет к ошибке:
# https://fullstacker.ru/osnovnye-printsipy-raboty-metoda-copy-v-python



def test_accept_the_order():
    return requests.get(URL + ACCEPT_THE_ORDER + cn_s).status_code
