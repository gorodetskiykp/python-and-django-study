students = [
	{
		"name": "Павел",
		"surname": "Иванов",
		"gender": "male",
		"coding_experience": 0,
		"homeworks_rates": [5, 7, 8, 6, 3],
		"exam_rate": 8,
	},
	{
		"name": "Сергей",
		"surname": "Василевский",
		"gender": "male",
		"coding_experience": 0,
		"homeworks_rates": [5, 3, 8, 7, 4],
		"exam_rate": 7,
	},
	{
		"name": "Галина",
		"surname": "Лямина",
		"gender": "female",
		"coding_experience": 0,
		"homeworks_rates": [7, 7, 8, 8, 8],
		"exam_rate": 10,
	},
	{
		"name": "Иван",
		"surname": "Ершов",
		"gender": "male",
		"coding_experience": 1,
		"homeworks_rates": [3, 3, 5, 6, 4],
		"exam_rate": 5,
	},
	{
		"name": "Майя",
		"surname": "Велькова",
		"gender": "female",
		"coding_experience": 1,
		"homeworks_rates": [6, 6, 8, 8, 9],
		"exam_rate": 9,
	},
	{
		"name": "Артем",
		"surname": "Нестеров",
		"gender": "male",6
		"coding_experience": 1,
		"homeworks_rates": [7, 7, 8, 7, 9],
		"exam_rate": 10,
	},
	{
		"name": "Ирина",
		"surname": "Калайтанова",
		"gender": "female",
		"coding_experience": 1,
		"homeworks_rates": [5, 5, 8, 7, 6],
		"exam_rate": 8,
	},
	{
		"name": "Владимир",
		"surname": "Савран",
		"gender": "male",
		"coding_experience": 0,
		"homeworks_rates": [3, 3, 1, 4, 5],
		"exam_rate": 3,
	},
]


def get_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


def stitching(function):
    def wrapper(*args, **kwargs):
        print("-"*100)
        function(*args, **kwargs)
        print("-"*100)
    return wrapper


@stitching
def calculate_average(  students: list, 
                        message_suffix: str, 
                        gender: str = "", 
                        coding_experience: int = -1) -> None:
    homeworks_message = "Средняя оценка за домашние задания"
    exams_message = "Средняя оценка за экзамен"

    if gender:
        students = [student for student in students if student['gender'] == gender]

    if coding_experience >= 0:
        students = [student for student in students 
                        if student['coding_experience'] == coding_experience]

    homeworks_average = get_average([get_average(student["homeworks_rates"]) 
                                        for student in students])
    exams_average = get_average([student["exam_rate"] for student in students])

    print("{} {}: {:.2f}".format(homeworks_message, message_suffix, homeworks_average))
    print("{} {}: {:.2f}".format(exams_message, message_suffix, exams_average))
    

@stitching
def best_student() -> dict:
    rates = {"{} {}".format(student["name"], student["surname"]): 
        0.6 * get_average(student["homeworks_rates"]) + 0.4 * student["exam_rate"] 
        for student in students}
    maximum_rate = max(rates.values())
    best_students_dict = {student: rate for student, rate in rates.items() if rate == maximum_rate}
    message_prefix = "Лучший студент"
    if len(best_students_dict) > 1:
        message_prefix = "Лучшие студенты"
    print("{}: {} с интегральной оценкой {:.2f}".format(
        message_prefix, ", ".join(best_students_dict.keys()), list(best_students_dict.values())[0]))
    

while True:
    print("Отчеты:\n1. Средние оценки по группе\n2. Средние оценки у мужчин",
          "\n3. Средние оценки у женщин\n4. Средние оценки у опытных",
          "\n5. Средние оценки у неопытных\n6. Лучшие студенты\nq - выход")
    choice = input("Выберите вариант отчета: ")
    if choice == '1':
        calculate_average(students, "по группе")
    elif choice == '2':
        calculate_average(students, "у мужчин", gender="male")
    elif choice == '3':
        calculate_average(students, "у женщин", gender="female")
    elif choice == '4':
        calculate_average(students, "у студентов с опытом", coding_experience=1)
    elif choice == '5':
        calculate_average(students, "у студентов без опыта", coding_experience=0)
    elif choice == '6':
        best_student()
    elif choice == 'q':
        break
