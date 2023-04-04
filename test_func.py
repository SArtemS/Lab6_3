"""
    Указать здесь тесты, включая последние задания.
"""
from main import get_number_of_pass

# TODO 

def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (
        577, 314), " Количество мужчин и женщин на Титанике"


# аналогично протестировать остальные функции
