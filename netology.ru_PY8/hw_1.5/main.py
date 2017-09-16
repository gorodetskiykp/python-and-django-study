from random import randint
from statistics import mean

students = [
    ['Александр Пирогов', 'м'],
    ['Алина Черникова', 'ж'],
    ['Дарья Юрьева', 'ж'],
    ['Максим Важенин', 'м'],
    ['Владимир Лукьянов', 'м'],
    ['Александра Дружинина', 'ж'],
    ['Леонид Литвинов', 'м'],
    ]
    
for student in students:
    student.append(randint(0,1))                    # programming experience
    points_for_homeworks = []
    for i in range(5):
        points_for_homeworks.append(randint(3,10))
    student.append(points_for_homeworks)
    student.append(randint(3,10))                   # points for exam
    
def average_point(students):
    try:
        homeworks_average = mean([mean(student[3]) for student in students])
        exam_average = mean([student[4] for student in students])
    except:
        homeworks_average = exam_average = 0
    return homeworks_average, exam_average

def average_point_template(students, words):
    homeworks_average, exam_average = average_point(students)
    return '{}\n{}'.format(
        'Средняя оценка за домашние задания {}: {:.2f}'.
            format(words, homeworks_average),
        'Средняя оценка за экзамен {}: {:.2f}'.
            format(words, exam_average))

def best_student(students):
    average_points = [0.6 * mean(student[3]) + 0.4 * student[4] 
        for student in students]
    best_average_points = max(average_points)
    start = 0
    positions = []
    for i in range(average_points.count(best_average_points)): 
        position = average_points.index(best_average_points, start)
        print(position)
        positions.append(position)
        start = position + 1
    
    if len(positions) == 1:
        print('Лучший студент: {} c интегральной оценкой {:.2f}'.format(
            students[positions.pop()][0], best_average_points))
    if len(positions) > 1:
        print('Лучшие студенты: {} c интегральной оценкой {:.2f}'.format(
                ', '.join([student[0] for position, student in enumerate(students) 
                if position in (positions)]), best_average_points))
                
def students_list(students):
    for s in students:
        print('{}; {}; ДЗ: {}; Экзамен: {}'.format(
            s[0], 
            'есть опыт' if s[2] else 'нет опыта',
            ', '.join(map(str, s[3])),
            s[4]))
            
show_menu = True

while True:
    if show_menu:
        print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(
            '-'*40,
            'qt - выход',
            'ls - список студентов',
            'ag - средние оценки по группе',
            'am - средние оценки по группе у мужчин',
            'af - средние оценки по группе у женщин',
            'ae - средние оценки по группе у студентов с опытом',
            'ai - средние оценки по группе у студентов без опыта',
            'bs - лучший студент (студенты)',
            'mu - показать/скрыть подсказку'
            ))
    user_choice = input('>>>')
    if user_choice == 'qt':
        break
    elif user_choice == 'mu':
        show_menu = not show_menu
    elif user_choice == 'ls':
        students_list(students)
    elif user_choice == 'ag':
        print(average_point_template(students, 'по группе'))
    elif user_choice == 'am':
        print(average_point_template(
        [student for student in students if student[1]=='м'], 'у мужчин'))
    elif user_choice == 'af':
        print(average_point_template(
            [student for student in students if student[1]=='ж'], 'у женщин'))
    elif user_choice == 'ae':
        print(average_point_template(
            [student for student in students if student[2]], 
            'у студентов с опытом'))
    elif user_choice == 'ai':
        print(average_point_template(
        [student for student in students if not student[2]], 
        'у студентов без опыта'))
    elif user_choice == 'bs':
        best_student(students)