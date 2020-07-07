"""
Для решения этой задачи Вам нужно использовать SendGrid API Key. 
Когда нажмете "Run" (Запустить), Вы увидите результаты использования Вашего ключа API с Вашими данными, но если Вы нажмете "Check" (Проверить), 
Ваше решение будет проверено с использованием наших данных.
Вы должны иметь возможность работать со статистическими данными Вашей электронной почты, а SendGrid имеет множество API-интерфейсов, которые предоставят Вам необходимую информацию.
Ваша миссия состоит в том, чтобы выяснить, какая страна чаще всего открывает Ваши электронные письма. 
Вы можете использовать эту информацию, чтобы сосредоточиться на определенном сегменте.
Входные данные: День в виде строки в формате 'YYYY-MM-DD'
Выходные данные: Строка, Двузначный код страны, в которой большее количество оригинальных кликов.
Пример:
    best_country('2016-01-01') == 'UA'
"""

import sendgrid
import json

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(API_KEY)

def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })
    json_content = json.loads(response.body)
    country_with_maximum_clicks = ""
    maximum_clicks = 0
    for country in json_content[0]['stats']:
        if country['metrics']['unique_clicks'] > maximum_clicks:
            maximum_clicks = country['metrics']['unique_clicks']
            country_with_maximum_clicks = country['name']
    return country_with_maximum_clicks
    return json.loads(response.body)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print(best_country('2020-05-21'))
    print('Check your results')