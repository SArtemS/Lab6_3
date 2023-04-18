from main import *

# TODO 

data = pd.read_csv('train.csv', index_col="PassengerId")

def test_get_number_of_pass():
    assert get_number_of_pass(data) == 891, " Общее количество пассажиров"

def test_get_sex_distrib():
    assert get_sex_distrib(data) == (
        577, 314), " Количество мужчин и женщин на Титанике"
    
def test_get_port_distrib():
    assert get_port_distrib(data) == (
        644, 168, 77), " Количество пассажиров на портах S, C, Q"
    
def test_get_surv_percent():
    assert get_surv_percent(data) == (
        549, 61.62), " Количество погибших и их процент"
    
def test_get_class_distrib():
    assert get_class_distrib(data) == (
        (216, 24.24), (184, 20.65), (491, 55.11)), " Доли первого, второго и третьего класса"
    
def test_find_corr_sibsp_parch():
    assert find_corr_sibsp_parch(data) == (
        0.41), " Коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch)"
    
def test_find_corr_age_survival():
    assert find_corr_age_survival(data) == (
        -0.08), " Корреляция между возрастом и параметром Survived"

def test_find_corr_sex_survival():
    assert find_corr_sex_survival(data) == (
        0.0032), " Корреляция между полом человека и параметром Survived"
    
def test_find_corr_class_survival():
    assert find_corr_class_survival(data) == (
        -0.34), " Корреляция между классом, в котором пассажир ехал, и параметром Survived"
    
def test_find_pass_mean_median():
    assert find_pass_mean_median(data) == (
        29.7, 28.0), " Средний возраст пассажиров и значение медианы"
    
def test_find_ticket_mean_median():
    assert find_ticket_mean_median(data) == (
        32.2, 14.45), " Средняя цена за билет и значение медианы"
    
def test_find_popular_name():
    assert find_popular_name(data) == (
        "William"), " Самое популярное мужское имя"
    
def test_find_popular_adult_names():
    assert find_popular_adult_names(data) == (
        "William", "Elizabeth"), " Самые популярные мужское и женское имена людей, старше 15 лет"
