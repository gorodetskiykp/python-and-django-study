import os
import osa

FILES_DIR = 'currencies'
STATISTICS_URL = 'http://www.webservicex.net/Statistics.asmx?WSDL'
TEMPERATURE_CONV_URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
CURRENCY_CONV_URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
DISTANCE_CONV_URL = 'http://www.webservicex.net/length.asmx?WSDL'

def get_average(args):
    """Вычисление среднего значения

    Получает список чисел
    Возвращает среднее значение"""

    client = osa.Client(STATISTICS_URL)
    array = client.types.ArrayOfDouble()
    array.double = args
    response = client.service.GetStatistics(array)
    return response.Average


def fahrenheit_to_celsius(temperature):
    """Конвертирует Фаренгейты в Цельсии"""

    client = osa.Client(TEMPERATURE_CONV_URL)
    return client.service.ConvertTemp(temperature, 'degreeFahrenheit', 'degreeCelsius')


def get_temperatures(file_name):
    """Читает файл с температурами и
    возвращает список температур
    """

    with open(os.path.join(FILES_DIR, file_name)) as f_temp:
        return [int(temperature.split()[0]) for temperature in f_temp]


def get_average_temperature(file_name):
    """Читает из файла температуры в Фаренгейтах
    и возвращает среднюю в Цельсиях
    """

    temperatures = get_temperatures(file_name)
    average_temp = get_average(temperatures)
    celsius_temp = fahrenheit_to_celsius(average_temp)
    return '{:.2f}'.format(celsius_temp)


def convert_to_rubles(cost, currency):
    """Конвертирует полученную сумму в рубли

    cost - стоимость в валюте
    currency - код валюты
    """

    client = osa.Client(CURRENCY_CONV_URL)
    response = client.service.ConvertToNum(toCurrency='RUB', fromCurrency=currency, amount=cost, rounding=True)
    return '{} RUB'.format(response)


def get_travels_cost_in_rubles(file_name):
    """Читает из файла записи о путешествиях
    и конвертирует стоимости в валюте в рубли
    """

    with open(os.path.join(FILES_DIR, file_name)) as f_travel:
        return '\n'.join([
            ' '.join(
                (travel.split()[0], convert_to_rubles(*travel.split()[1:])))
            for travel in f_travel])


def convert_to_kilometres(miles):
    """Конвертирует полученную дистанцию в километры"""

    client = osa.Client(DISTANCE_CONV_URL)
    response = client.service.ChangeLengthUnit(miles, 'Miles', 'Kilometers')
    return response


def get_distance_in_km(file_name):
    """Читает из файла записи о путешествиях
    и возвращает сумму расстояний в километрах
    """

    with open(os.path.join(FILES_DIR, file_name)) as f_dist:
        return convert_to_kilometres(sum(
            [float(distance.split()[1].replace(',', '')) for distance in f_dist]))


if __name__ == '__main__':
    print('1. Средняя температура в Цельсиях: {}\n'.format(get_average_temperature('temps.txt')))
    print('2. Стоимость путешествий в рублях:\n{}\n'.format(get_travels_cost_in_rubles('currencies.txt')))
    print('3. Суммарное расстояние в километорах: {:.2f}'.format(get_distance_in_km('travel.txt')))
