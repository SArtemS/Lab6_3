import pandas as pd  

data = pd.read_csv('train.csv', index_col="PassengerId")

# TODO #0 Общее количество пассажиров. 
def get_number_of_pass(data):
    res = data.shape[0]
    return res

# TODO #1 Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
def get_sex_distrib(data):
    res = data['Sex'].value_counts()
    n_male, n_female = res['male'], res['female']
    return n_male, n_female


# TODO #2 Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
def get_port_distrib(data):
    res = data['Embarked'].value_counts()
    port_S, port_C, port_Q = res['S'], res['C'], res['Q']
    return port_S, port_C, port_Q


# TODO #3 Посчитайте долю погибших на параходе (число и процент)?
def get_surv_percent(data):
    res = data['Survived'].value_counts()
    n_died = res[0]
    perc_died = round(n_died/get_number_of_pass(data) * 100, 2)
    return n_died, perc_died


# TODO #4 Какие доли составляли пассажиры первого, второго, третьего класса? 
def get_class_distrib(data):
    res = data['Pclass'].value_counts()
    all_pass = get_number_of_pass(data)
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = (
        (res[1], round(res[1]/all_pass * 100, 2)), 
        (res[2], round(res[2]/all_pass * 100, 2)), 
        (res[3], round(res[3]/all_pass * 100, 2))
    )
    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# TODO #5 Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
def find_corr_sibsp_parch(data):
    corr_val = data['SibSp'].corr(data['Parch'])
    return round(corr_val, 2)


# TODO #6-1 Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между: возрастом и параметром Survived;
def find_corr_age_survival(data):
    corr_val = data['Age'].corr(data['Survived'])
    return round(corr_val, 2)


# TODO #6-2 Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между: полом человека и параметром Survived;
def find_corr_sex_survival(data):
    int_sex = []
    for i in range(get_number_of_pass(data)):
        if data.iloc[i]['Sex'] == "female": int_sex.append(0)
        else: int_sex.append(1)
    alt_sex_data = {'Sex' : int_sex}
    alt_sex_data_pd = pd.DataFrame(alt_sex_data)
    corr_val = alt_sex_data_pd['Sex'].corr(data['Survived'])
    return round(corr_val, 4)


# TODO #6-3 Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между: классом, в котором пассажир ехал, и параметром Survived.
def find_corr_class_survival(data):
    corr_val = data['Pclass'].corr(data['Survived'])
    return round(corr_val, 2)


# TODO #7 Посчитайте средний возраст пассажиров и медиану.
def find_pass_mean_median(data):
    all_pass = data['Age'].notnull().sum()
    mean_age = round(data['Age'].sum()/all_pass, 2)
    lst_median = data[data['Age'].notna()]['Age'].values.tolist()
    lst_median.sort()
    if all_pass % 2 != 0:
        median = lst_median[all_pass//2]
    else:
        median = (lst_median[all_pass//2 - 1] + lst_median[all_pass//2])/2
    return mean_age, round(median, 2)


# TODO #8 Посчитайте среднюю цену за билет и медиану.
def find_ticket_mean_median(data):
    all_pass = get_number_of_pass(data)
    mean_price = round(data['Fare'].sum()/all_pass, 2)
    lst_median = data['Fare'].values.tolist()
    lst_median.sort()
    if all_pass % 2 != 0:
        median = lst_median[all_pass//2]
    else:
        median = (lst_median[all_pass//2 - 1] + lst_median[all_pass//2])/2
    return mean_price, round(median, 2)


# TODO #9 Какое самое популярное мужское имя на корабле?
def find_popular_name(data):
    from collections import Counter
    import re
    lst_male_fullnames = data[data['Sex'] == "male"]['Name'].values.tolist()
    lst_male_firstnames = []
    for fullname in lst_male_fullnames:
        name = fullname.split(". ", 1)[1]
        name = re.sub('[()"]', "", name)
        name = name.split()
        lst_male_firstnames.extend(name)
    most_popular_male_name = Counter(lst_male_firstnames).most_common(1)[0][0]
    return most_popular_male_name


# TODO #10 Какие самые популярные мужское и женское имена людей, старше 15 лет на корабле?
def find_popular_adult_names(data):
    from collections import Counter
    import re
    lst_male_fullnames = data[(data['Sex'] == "male") & (data['Age'] > 15)]['Name'].values.tolist()
    lst_female_fullnames = data[(data['Sex'] == "female") &(data['Age'] > 15)]['Name'].values.tolist()
    lst_male_firstnames = []
    for fullname in lst_male_fullnames:
        name = fullname.split(". ", 1)[1]
        name = re.sub('[()"]', "", name)
        name = name.split()
        lst_male_firstnames.extend(name)
    lst_female_firstnames = []
    for fullname in lst_female_fullnames:
        name = fullname.split(". ", 1)[1]
        name = re.sub('[")]', "", name)
        if "(" in name:
            name = name.split("(")[1]
        name = name.split()
        lst_female_firstnames.extend(name)
    popular_male_name = Counter(lst_male_firstnames).most_common(1)[0][0]
    popular_female_name = Counter(lst_female_firstnames).most_common(1)[0][0]
    return popular_male_name, popular_female_name

#0
print("0. Вычисление количества пассажиров на параходе\nРезультат: количество пассажиров на параходе = " + str(get_number_of_pass(data)) + ".")

#1
sex_distrib = get_sex_distrib(data)
print("\n1. Какое количество мужчин и женщин ехало на параходе?\nРезультат: количество мужчин = " + str(sex_distrib[0])
      + ", количество женщин = " + str(sex_distrib[1]) + ".")

#2
port_distrib = get_port_distrib(data)
print("\n2. Сколько пассажиров загрузилось на борт в различных портах?\nРезультат: пассажиров на порту S = " + str(port_distrib[0])
      + ", пассажиров на порту C = " + str(port_distrib[1]) + ", пассажиров на порту Q = " + str(port_distrib[2]) + ".")

#3
surv_percent = get_surv_percent(data)
print("\n3. Какая доля погибших на параходе?\nРезультат: " + "число погибших = " + str(surv_percent[0]) + ", % погибших = " 
      + str(surv_percent[1]) + "%.")

#4
class_distrib = get_class_distrib(data)
print("\n4. Какие доли составляли пассажиры первого, второго, третьего класса?\nРезультат:\nчисло пассажиров первого класса = " 
      + str(class_distrib[0][0]) + ", % пассажиров первого класса = " + str(class_distrib[0][1]) + "%;\nчисло пассажиров второго класса = "
      + str(class_distrib[1][0]) + ", % пассажиров второго класса = " + str(class_distrib[1][1]) + "%;\nчисло пассажиров третьего класса = "
      + str(class_distrib[2][0]) + ", % пассажиров второго класса = " + str(class_distrib[2][1]) + "%.")

#5
print("\n5. Какой коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch)?\nРезультат: " + str(find_corr_sibsp_parch(data)))

#6.1
print("\n6.1. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между: возрастом и параметром Survived.\nРезультат: "
      + str(find_corr_age_survival(data)))

#6.2
print("\n6.2. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между: полом человека и параметром Survived.\nРезультат: "
      + str(find_corr_sex_survival(data)))

#6.3
print("\n6.3. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между: классом, в котором пассажир ехал, и параметром Survived.\nРезультат: "
      + str(find_corr_class_survival(data)))

#7
pass_mean_median = find_pass_mean_median(data)
print("\n7. Каков средний возраст пассажиров и какое значение медианы?\nРезультат: средний возраст = " 
      + str(pass_mean_median[0]) + ", медиана = " + str(pass_mean_median[1]) + ".")

#8
ticket_mean_median = find_ticket_mean_median(data)
print("\n8. Какова средняя цена за билет и какое значение медианы?\nРезультат: средняя цена за билет = " 
      + str(ticket_mean_median[0]) + ", медиана = " + str(ticket_mean_median[1]) + ".")

#9
print("\n9. Какое самое популярное мужское имя на корабле?\nРезультат: самое популярное мужское имя = " + find_popular_name(data))

#10
popular_names = find_popular_adult_names(data)
print("\n10. Какие самые популярные мужское и женское имена людей, старше 15 лет на корабле?\nРезультат: самое популярное мужское имя = "
       + popular_names[0] + ", самое популярное женское имя = " + popular_names[1])
