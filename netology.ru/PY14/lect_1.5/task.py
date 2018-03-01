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
		"homeworks_rates": [8, 4, 8, 8, 6],
		"exam_rate": 9,
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
		"gender": "male",
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


def calculate_average() -> None:
	homeworks_sum_rate = 0
	exam_sum_rate = 0
	students_number = len(students)
	for student in students:
		homeworks_sum_rate += sum(student["homeworks_rates"]) / len(student["homeworks_rates"])
		exam_sum_rate += student["exam_rate"]
	print(homeworks_sum_rate / students_number)
	print(exam_sum_rate / students_number)
	
	
calculate_average()
