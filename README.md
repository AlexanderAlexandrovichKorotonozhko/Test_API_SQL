Авто тесты для проекта 11
А вообще у меня сильно сгорело от задачи сохранить трек.
Дело в том что метод .cpy не работает с неизменяемыми типами данных и как выяснилось с функциями запросов тоже,
умники которые скажут что сохрани в переменную и там делай что хочешь, могут идти читать про питон.
Питон не сохраняет значение в переменную от дает переменной ссылку на объект.
Поскольку я не нашел альтернативного способа сохранить переменную я сделал как сделал.
Работает и ладно, я не настолько программист, чтобы решать такие задачи прямо сейчас, в будущем обязательно, но не на дипломе.

Подводные камни использования copy()
Помимо различия между поверхностным и глубоким копированием,
важно помнить, что не все типы данных в Python поддерживают метод copy().
Например, числа, строки и кортежи являются неизменяемыми (immutable),
и у них нет метода copy(). Попытка вызвать copy() у такого объекта приведет к ошибке:
https://fullstacker.ru/osnovnye-printsipy-raboty-metoda-copy-v-python

