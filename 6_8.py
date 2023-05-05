# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны


COUNTRY_CITY = {'belarus': ['minsk', 'grodno'], 'ukraine': ['kiev', 'odessa']}


def your_country(city):
    # if city not in COUNTRY_CITY.values():
    #     print('We do not know your city')
    #     return
    for country, cities in COUNTRY_CITY.items():
        if city in cities:
            print(f'your country is {country}')
            return
    print('We do not know where are you from')
    return


your_country('odessa')
