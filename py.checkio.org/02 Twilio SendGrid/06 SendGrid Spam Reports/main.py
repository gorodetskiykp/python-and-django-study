"""
Чтобы решить эту задачу, Вам необходимо использовать SendGrid API Key. Когда нажмете "Run" (Запустить), 
Вы увидите результаты использования Вашего ключа API с Вашими данными, но если Вы нажмете "Check" (Проверить), 
Ваше решение будет проверено с использованием наших данных.
Вы массово отправляете тысячи и тысячи писем каждый день, тем временем экспериментируя с темами и содержанием сообщения. 
SendGrid позволяет Вам просматривать статистику Ваших спам-отчетов.
Ваша миссия состоит в том, чтобы выяснить, сколько отчетов о спаме вы получаете в определенный день.
Входные данные: День в виде строки в формате 'YYYY-MM-DD'
Выходные данные: Int. Количество спам-отчетов.
Пример:
    how_spammed('2014-5-5') == 16
"""

import sendgrid
from datetime import datetime, timedelta
import json

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(API_KEY)


def how_spammed(str_date):

    start_time = datetime.strptime(str_date, '%Y-%m-%d')
    end_time = start_time + timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(query_params={
        'start_time': int(start_time.timestamp()),
        'end_time':int(end_time.timestamp())
    })
    data = json.loads(response.body)
    return len(data)
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')

