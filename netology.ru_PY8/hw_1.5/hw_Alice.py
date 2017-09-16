# Домашнее задание к лекции 1.5 «Практика по использованию циклов, коллекций 
# и функций»

# Имеется группа студентов, у каждого из которых есть следующие
# характеристики: имя, фамилия, пол, предыдущий опыт в программировании
# (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ,
# оценка за экзамен по 10-балльной шкале. 

# Необходимо написать программу, которая в зависимости от запроса пользователя 
# будет выводить:

# 1. среднюю оценку за домашние задания и за экзамен по всем группе в
# следующем виде:
# Средняя оценка за домашние задания по группе: X
# Средняя оценка за экзамен: Y
# где X и Y - вычисляемые значения;

# 2. среднеюю оценку за домашние задания и за экзамен по группе в
# разрезе: а)пола б)наличия опыта в виде:
# Средняя оценка за домашние задания у мужчин: A
# Средняя оценка за экзамен у мужчин: B
# Средняя оценка за домашние задания у женщин: C
# Средняя оценка за экзамен у женщин: D
# Средняя оценка за домашние задания у студентов с опытом: E 
# Средняя оценка за экзамен у студентов с опытом: F
# Средняя оценка за домашние задания у студентов без опыта: G
# Средняя оценка за экзамен у студентов без опыта: H
# где A, B, C, D, E, F, G, H - вычисляемые значения;

# Студентов должно быть не менее 6.

students = [{ 
    'name'       : 'Olga', 
    'surname'    : 'Pavlova', 
    'gender'     : 'female', 
    'experience' : True, 
    'rating_hw'  : [5, 8, 9, 10, 7], 
    #'rating_ex' : [6] # зачем одно число в список оборачивать?
    'rating_ex'  : 6
    }, { 
    'name'       : 'Oleg', 
    'surname' 	 : 'Pavlov', 
    'gender'     : 'male', 
    'experience' : False, 
    'rating_hw'  : [7, 8, 8, 10, 7], 
    #'rating_ex' : [8]
    'rating_ex'  : 8
    }, { 
    'name'       : 'Potap', 
    'surname'    : 'Vershkov', 
    'gender'     : 'male', 
    'experience' : True, 
    'rating_hw'  : [9, 8, 9, 10, 9], 
    #'rating_ex' : [10]
    'rating_ex'  : 10
    }, { 
    'name'       : 'Ostap', 
    'surname'    : 'Sevruk', 
    'gender'     : 'male', 
    'experience' : True, 
    'rating_hw'  : [7, 7, 9, 10, 9], 
    #'rating_ex' : [9]
    'rating_ex'  : 9
    }, { 
    'name'       : 'Vasilisa', 
    'surname'    : 'Sevruk', 
    'gender'     : 'female', 
    'experience' : False, 
    'rating_hw'  : [6, 8, 7, 10, 9], 
    #'rating_ex' : [8]
    'rating_ex'  : 8
    }, { 
    'name'       : 'Matvei', 
    'surname'    : 'Dudchenko', 
    'gender'     : 'male', 
    'experience' : False, 
    'rating_hw'  : [9, 8, 9, 10, 7], 
    #'rating_ex' : [10]
    'rating_ex'  : 10
    }, { 
    'name'       : 'Alice', 
    'surname'    : 'Dobroserdova', 
    'gender'     : 'male', 
    'experience' : True, 
    'rating_hw'  : [9, 8, 9, 10, 9], 
    #'rating_ex' : [10]
    'rating_ex'  : 10
    }]

# def rating_homework():
#   sum_rating_hw_students = 0
#   for x in students:
#     sum_rating_hw_students += sum(x['rating_hw'])/len(x['rating_hw'])
#     average_rating_hw_students = sum_rating_hw_students/len(students)
#   print("Средняя оценка по домашнему заданию в группе студентов: ", average_rating_hw_students)

# rating_homework()

def rating(students):
    average_homeworks = (
        sum([sum(student['rating_hw']) / 5 for student in students]) 
            / len(students))
    average_exams = (
        sum([student['rating_ex'] for student in students]) 
            / len(students))
    return average_homeworks, average_exams
    
print('Средняя оценка по домашнему заданию в группе студентов: {:.2f}'.
    format(rating(students)[0]))

# def rating_exam():    
#   sum_rating_ex_students = 0
#   for y in students:
#     # sum_rating_ex_students += sum(y['rating_ex'])
#     sum_rating_ex_students += y['rating_ex']
#     average_rating_ex_students = sum_rating_ex_students/len(students)
#   print("Средняя оценка по экзамену в группе студентов: ", average_rating_ex_students)

# rating_exam() 

# print("--------------------------")

print('Средняя оценка по экзамену в группе студентов: {:.2f}'.
    format(rating(students)[1]))

print('-'*60)


# def rating_male_hw():
#   sum_rating_hw_male = 0
#   hw_male = []
#   for a in students:
#       if a['gender'] == 'male':
#         hw_male.append(sum(a['rating_hw'])/len(a['rating_hw']))
#         sum_rating_hw_male += sum(a['rating_hw'])/len(a['rating_hw'])
#   average_raiting_hw_male = sum_rating_hw_male/len(hw_male)
#   print ("Средняя оценка за домашнюю работу у мужчин: ",  average_raiting_hw_male)
# rating_male_hw()

male_students = [student for student in students 
                    if student['gender'] == 'male']

female_students = [student for student in students 
                    if student['gender'] == 'female']

exp_students = [student for student in students 
                    if student['experience']]

non_exp_students = [student for student in students 
                    if not student['experience']]

print('Средняя оценка за домашнюю работу у мужчин: {:.2f}'.
    format(rating(male_students)[0]))

# def rating_male_ex():
#   sum_rating_ex_male = 0
#   ex_male = []
#   for b in students:
#     if b['gender'] == 'male':
#       # ex_male.append(sum(b['rating_ex'])/len(b['rating_ex']))
#       ex_male.append(b['rating_ex'])
#       # sum_rating_ex_male += sum(b['rating_ex'])/len(b['rating_ex'])
#       sum_rating_ex_male += b['rating_ex']
#       average_raiting_ex_male = sum_rating_ex_male/len(ex_male)
#   print ("Средняя оценка за экзамен у мужчин: ",  average_raiting_ex_male)
# rating_male_ex()
# print("--------------------------")

print('Средняя оценка за экзамен у мужчин: {:.2f}'.
    format(rating(male_students)[1]))

print('-'*60)

'''
def rating_female_hw():
  sum_rating_hw_female = 0
  hw_female = []
  for c in students:
    if c['gender'] == 'female':
      hw_female.append(sum(c['rating_hw'])/len(c['rating_hw']))
      sum_rating_hw_female += sum(c['rating_hw'])/len(c['rating_hw'])
      average_raiting_hw_female = sum_rating_hw_female/len(hw_female)
  print ("Средняя оценка за домашнюю работу у женщин: ", average_raiting_hw_female)
rating_female_hw()

def rating_female_ex():
  sum_rating_ex_female = 0
  ex_female = []
  for d in students:
    if d['gender'] == 'female':
      # ex_female.append(sum(d['rating_ex'])/len(d['rating_ex']))
      ex_female.append(d['rating_ex'])
      # sum_rating_ex_female += sum(d['rating_ex'])/len(d['rating_ex'])
      sum_rating_ex_female += d['rating_ex']
      average_raiting_ex_female = sum_rating_ex_female/len(ex_female)
  print ("Средняя оценка за экзамен у женщин: ",  average_raiting_ex_female)
rating_female_ex()
print("--------------------------")
'''

print('Средняя оценка за домашнюю работу у женщин: {:.2f}'.
    format(rating(female_students)[0]))
    
print('Средняя оценка за экзамен у женщин: {:.2f}'.
    format(rating(female_students)[1]))
    
print('-'*60)

'''
def rating_expirienced_hw():
  sum_rating_hw_experienced = 0
  hw_experienced = []
  for e in students:
    if e['experience'] == True:
      hw_experienced.append(sum(e['rating_hw'])/len(e['rating_hw']))
      sum_rating_hw_experienced += sum(e['rating_hw'])/len(e['rating_hw'])
      average_raiting_hw_expirienced = sum_rating_hw_experienced/len(hw_experienced)
  print ("Средняя оценка за домашнюю работу у опытных: ", average_raiting_hw_expirienced)
rating_expirienced_hw()

def rating_expirienced_ex():
  sum_rating_ex_experienced = 0
  ex_experienced = []
  for f in students:
    if f['experience'] == True:
      # ex_experienced.append(sum(f['rating_ex'])/len(f['rating_ex']))
      # sum_rating_ex_experienced += sum(f['rating_ex'])/len(f['rating_ex'])
      ex_experienced.append(f['rating_ex'])
      sum_rating_ex_experienced += f['rating_ex']
      average_raiting_ex_expirienced = sum_rating_ex_experienced / len(ex_experienced)
  print ("Средняя оценка за экзамен у опытных: ", average_raiting_ex_expirienced)
rating_expirienced_ex()
print("--------------------------")

def rating_non_expirienced_hw():
  sum_rating_hw_non_expirienced = 0
  hw_non_expirienced = []
  for g in students:
    if g['experience'] == False:
      hw_non_expirienced.append(sum(g['rating_hw'])/len(g['rating_hw']))
      sum_rating_hw_non_expirienced += sum(g['rating_hw'])/len(g['rating_hw'])
      average_raiting_hw_non_expirienced = sum_rating_hw_non_expirienced/len(hw_non_expirienced)
  print ("Средняя оценка за домашнюю работу у неопытных: ",  average_raiting_hw_non_expirienced)
rating_non_expirienced_hw()

def rating_non_expirienced_ex():
  sum_rating_ex_non_expirienced = 0
  ex_non_expirienced = []
  for h in students:
    if h['experience'] == False:
      #ex_non_expirienced.append(sum(h['rating_ex'])/len(h['rating_ex']))
      #sum_rating_ex_non_expirienced += sum(h['rating_ex'])/len(h['rating_ex'])
      ex_non_expirienced.append(h['rating_ex'])
      sum_rating_ex_non_expirienced += h['rating_ex']
      average_raiting_ex_non_expirienced = sum_rating_ex_non_expirienced/len(ex_non_expirienced)
  print ("Средняя оценка за экзамен у неопытных: ",  average_raiting_ex_non_expirienced)
rating_non_expirienced_ex()
print("--------------------------")
'''

print('Средняя оценка за домашнюю работу у оытных: {:.2f}'.
    format(rating(exp_students)[0]))
    
print('Средняя оценка за экзамен у опытных: {:.2f}'.
    format(rating(exp_students)[1]))

print('-'*60)

print('Средняя оценка за домашнюю работу у неоптыных: {:.2f}'.
    format(rating(non_exp_students)[0]))
    
print('Средняя оценка за экзамен у неоптыных: {:.2f}'.
    format(rating(non_exp_students)[1]))

print('-'*60)


# 3. определять лучшего студента, у которого будет максимальный балл по
# формуле 0.6 * его средняя оценка за домашние задания + 0.4 *
# оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, 
# где S - имя/имена студентов, Z - вычисляемое значение.

'''
for z in students:
  integral_rating = 0.6*(sum(z['rating_hw'])/len(z['rating_hw']))) + 0.4*float((z['rating_ex']))
print(integral_rating)
'''

def integral_ratings(students):
    return [rating([student])[0] * 0.6 + student['rating_ex'] * 0.4 
        for student in students]

'''
# def best_student():
#   best_students = []
#   best = 0
#   for z in students:
#     best_students.append(sum(z['rating_hw'])/len(z['rating_hw']))
#     best = (0.6*(sum(z['rating_hw'])/len(z['rating_hw']))) + (0.4*(z['rating_ex']))
#   print(best_students)
# best_student()

'''

def best_students(students):
    integral_ratings_list = integral_ratings(students)
    max_rating = max(integral_ratings_list)
    max_indexes = [rating_index for rating_index, rating 
        in enumerate(integral_ratings_list) if rating == max_rating]
    
    return (max_rating, 
        ['{} {}'.format(
                    students[student_index]['name'], 
                    students[student_index]['surname']) 
                        for student_index in max_indexes])

best_students = best_students(students)   

if len(best_students[1]) == 1:
    print('Лучший студент: ', end = '')
else:
    print('Лучшие студенты: ', end = '')

print('{} с интегральной оценкой {:.2f}'.format(
    ', '.join(sorted(best_students[1])), best_students[0]
)) 

