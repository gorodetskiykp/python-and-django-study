import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

#можете посмотреть содержимое файлв с квартирами через print, можете - на вкладке output.csv
#print (flats_list)


#TODO 1:
#Напишите цикл, который проходит по всем квартирам, и печатает только новостройки
#и их порядковые номера в файле. Подсказка:
def flat_print(number, flat):
    return '{:65}'.format(
            '{:3d}. {} комн. {} м\u00B2{} {}{}'.format(
              number,                                                           # number
              flat[1],                                                          # rooms
              flat[7],                                                          # square
              ', {:>2} мин.'.format(flat[4]) if flat[4]!='не указано' else '',  # minutes
              flat[5] if flat[5]!='не указано' else '',                         # walk or bus
              ' до {}'.format(flat[3]) if flat[3]!='' else ''                   # station
            )
          ) + \
          '{:,.2f} \u20bd'.format(
            float(flat[11]))                                                    # price

for i, flat in enumerate(flats_list):
  if flat[2] == 'новостройка':
    print(flat_print(i, flat))

print('\n{}\n'.format('-'*80))
#TODO 2:
#При помощи пересечения множеств попробуйте сравнить больше двух новостроек между собой одновременно
#например, пересечение 3 и 6 квартиры из файла с ЦИАНа делается так:
flats_intersesction = set(flats_list[198]) & set(flats_list[199]) & set(flats_list[202]) 
print(flat_print(198, flats_list[198]))
print(flat_print(199, flats_list[199]))
print(flat_print(202, flats_list[202]))
print('\n{}\n'.format('-'*80))
print(flats_list[198])
print(flats_list[199])
print(flats_list[202])
print('\n{}\n'.format('-'*80))
print(flats_intersesction)

#Порядковые номера новостроек вы уже получили при выполнении предыдущего задания.
#Не забудьте вывести результат функцией print

print('\n{}\n'.format('-'*80))
#TODO3:
#Вот так мы превратили наш массив квартир в словарь, где ключом является уникальный номер объявления,
#а значением - ссылка на страничку с объявлением.
#Измените код так, чтобы стало наоборот.

test_dict = dict()
for i, flat in enumerate(flats_list):
  if i == 0:
    continue
  test_dict[flat[0]] = flat[len(flat)-1]
print (test_dict)

print('\n{}\n'.format('-'*80))
flats_dict = dict(zip(test_dict.values(), test_dict.keys()))
print (flats_dict)
    

