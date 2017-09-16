from datetime import datetime, time, timedelta
from random import randint

work_begin = datetime.combine(datetime.today(), time(8,00))
work_time = timedelta(hours=8)
work_time_left = timedelta(hours=0)

print('{} Начало рабочего дня'.format(work_begin.strftime('%H:%M')))
print('{} Подготовка инструмента'.format(work_begin.strftime('%H:%M')))
work_time_left = timedelta(minutes=randint(15,60))

lunch_time = timedelta(hours=0)



if input('Петрович пришел на работу? (да/нет)') == 'да':
  petrovitch = True
else:
  petrovitch = False

while work_time_left < work_time:
  print('-')
  print('{} Перекур'.format((work_begin + work_time_left + lunch_time).strftime('%H:%M')))
  work_time_left += timedelta(minutes=randint(15,20))
  if work_time_left > work_time:
    print('Бросаем все, идем домой')
    break
  print('{} Копаем яму'.format((work_begin + work_time_left + lunch_time).strftime('%H:%M')))
  work_time_left += timedelta(minutes=randint(15,30))
  if work_time_left > work_time:
    print('Бросаем все, идем домой')
    break
  if petrovitch:
    print('{} Сажаем саженец'.format((work_begin + work_time_left + lunch_time).strftime('%H:%M')))
    work_time_left += timedelta(minutes=randint(5,20))
    if work_time_left > work_time:
      print('Бросаем все, идем домой')
      break
  print('{} Закапываем'.format((work_begin + work_time_left + lunch_time).strftime('%H:%M')))
  work_time_left += timedelta(minutes=randint(10,20))
  if work_time_left > work_time:
    print('Бросаем все, идем домой')
    break
  print('{} Переходим на новое место'.format((work_begin + work_time_left + lunch_time).strftime('%H:%M')))
  work_time_left += timedelta(minutes=randint(5,10))
  if work_time_left > work_time:
    print('Бросаем все, идем домой')
    break
  if lunch_time == timedelta(hours=0) and work_time_left >= timedelta(hours=4):
    lunch_time = timedelta(hours=1)
    print('-')
    print('{} Обед'.format((work_begin + work_time_left).strftime('%H:%M')))
