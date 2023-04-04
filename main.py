# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 3
"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром Survived;
2) полом человека и параметром Survived;
3) классом, в котором пассажир ехал, и параметром Survived.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 
"""

import pandas as pd  # импортирование библиотеки для считывания данных
import math

# считаем данные из файла, в качестве столбца индексов используем PassengerId
data = pd.read_csv('train.csv', index_col="PassengerId")


# TODO #1 Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
def get_sex_distrib(data):
    n_male, n_female = 0, 0
    res = data['Sex'].value_counts()
    n_male, n_female = res['male'], res['female']
    return n_male, n_female


# TODO #2 Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
def get_port_distrib(data):
    port_S, port_C, port_Q = 0, 0, 0
    res = data['Embarked'].value_counts()
    port_S, port_C, port_Q = res['S'], res['C'], res['Q']
    return port_S, port_C, port_Q


# TODO #3 Посчитайте долю погибших на параходе (число и процент)?
def get_surv_percent(data):
    n_died, perc_died = 0, 0
    res = data['Survived'].value_counts()
    n_died = res[0]
    perc_died = round(n_died/get_number_of_pass(data) * 100, 1)
    return n_died, perc_died


# TODO #4 Какие доли составляли пассажиры первого, второго, третьего класса? 
def get_class_distrib(data):
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0
    res = data['Pclass'].value_counts()
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = res[1], res[2], res[3]
    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    corr_val = -1
    return corr_val


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром Survived;

    """

    corr_val = -1
    return corr_val


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром Survived;
    """

    corr_val = -1
    return corr_val


# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром Survived.
    """

    corr_val = -1
    return corr_val


# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = None, None
    return mean_age, median


# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price, median = None, None
    return mean_price, median


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    name = ""
    return name


# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    popular_male_name, popular_female_name = "", ""
    return popular_male_name, popular_female_name


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу.
# С помощью запроса ниже мы можем получить имя сотого пассажира
# print(type(data.iloc[100]))
# print(data.iloc[100]['Name'])

# print((data['Name'], data['Sex']))


def get_number_of_pass(data):
    res = data.shape[0]
    return res


# print(find_corr_sex_survival(data))
#0
print(get_number_of_pass(data))
#1
print(get_sex_distrib(data))
#2
print(get_port_distrib(data))
#3
print(get_surv_percent(data))
#4
print(get_class_distrib(data))