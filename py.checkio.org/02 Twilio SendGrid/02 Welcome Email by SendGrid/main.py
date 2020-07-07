"""
Чтобы решить эту задачу, вы должны использовать SendGrid API Key (в этом видео Вы сможете найти объяснение, как создать Ваш собственный API Key). 
Все начинается с Вашего первого электронного письма. Давайте попробуем его отправить.
Ваша задача заключается в том, чтобы создать функцию, которая отправлят приветственный емейл пользователю. Функция получает два параметра: емейл и имя пользователя.
Темой письма должно быть "Welcome", а текст письма просто "Hi {name}" ({name} должно быть заменено на имя пользователя).
Входные данные: Два параметра: емейл и имя пользователя.
Выходные данные: Нет. Вам нужно отправить емейл. Вам ничего не нужно возвращать.
send_email('a.lyabah@checkio.org', 'oduvan')
send_email('somebody@gmail.com', 'Some Body')
"""

import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'

sg = sendgrid.SendGridAPIClient(API_KEY)

def send_email(email, name):
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content='Hi {}'.format(name)
    )
    
    response = sg.send(message)
    
if __name__ == '__main__':
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')