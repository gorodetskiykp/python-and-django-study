documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
	{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
	{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
	'1': ['2207 876234', '11-2'],
	'2': ['10006'],
	'3': []
}


def find_document(document_number:str) -> dict:
	for document in documents:
		if document.get("number", None) == document_number.lower():
			return(document)


def find_shelf(document_number:str) -> str:
	for shelf_number, documents_list in directories.items():
		if document_number in documents_list:
			return shelf_number
	return ""


def delete_document_from_shelf(document_number:str) -> str:
	shelf_number = find_shelf(document_number)
	if shelf_number:
		directories[shelf_number].remove(document_number)
		return shelf_number
	return ""


def show_document_owner() -> bool:
	document_number = input("Введите номер документа: ").strip()
	if document_number == "":
		print("Нужно было ввести номер документа")
		return False
	document = find_document(document_number)
	if document:
		print('{} - владелец документа с номером "{}"'.\
			format(document.get("name", "<имя не указано>"), document_number))
		return True
	print('Документ с номером "{}" не найден'.format(document_number))
	return False


def show_documents_list() -> None:
	documents_list = ['{} "{}" "{}"'.format(document["type"], document["number"], document["name"]) 
						for document in documents
					 ]
	print("\n".join(documents_list))


def show_shelf() -> bool:
	document_number = input("Введите номер документа: ").strip()
	if document_number == "":
		print("Нужно было ввести номер документа")
		return False	
	shelf_number = find_shelf(document_number)
	if shelf_number:
		print('Документ с номером "{}" лежит на полке "{}"'.\
			format(document_number, shelf_number))
		return True
	print('Документа с номером "{}" на полках нет'.format(document_number))
	return False
	

def add_document() -> bool:
	document_number = input("Введите номер документа: ").strip()
	document_type = input("Введите тип документа: ").strip()
	document_owner = input("Введите владельца документа: ").strip()
	document_shelf = input("На какую полку положить документ: ").strip()
	if not all([document_number, document_type, document_owner, document_shelf]):
		print("Нужно было ввести все параметры")
		return False		
	documents.append({
		"type": document_type, 
		"number": document_number, 
		"name": document_owner
	})
	add_shelf(document_shelf)
	directories[document_shelf].append(document_number)
	print('Документ <{} "{}" "{}"> помещен на полку "{}"'.\
		format(document_type, document_number, document_owner, document_shelf))
	return True


def delete_document() -> bool:
	document_number = input("Введите номер документа: ").strip()
	if document_number == "":
		print("Нужно было ввести номер документа")
		return False
	document = find_document(document_number)
	if document:
		deleted_document = document
		documents.remove(document)
	else:
		print('Документ с номером "{}" не найден'.format(document_number))
		return False
	shelf = delete_document_from_shelf(document_number)
	print('Документ {} (полка "{}") удален'.\
		format('{} "{}" "{}"'.\
			format(	document["type"], 
					document["number"], 
					document["name"]
			), 
			shelf
		))
	return True


def move_document() -> bool:
	document_number = input("Введите номер документа: ").strip()
	new_shelf = input("На какую полку переместить документ: ").strip()
	if not all([document_number, new_shelf]):
		print("Нужно было ввести все параметры")
		return False
	old_shelf = delete_document_from_shelf(document_number)
	if not old_shelf:
		print('Документа с номером "{}" на полках нет'.format(document_number))
		return False
	directories.setdefault(new_shelf, list(document_number)).append(document_number)
	print('Документ с номером "{}" перемещен с полки "{}" на полку "{}"'.\
		format(document_number, old_shelf, new_shelf))
	return True


def add_shelf(shelf_number:str="") -> bool:
	new_shelf = shelf_number if shelf_number else input("Введите номер полки: ").strip()
	if new_shelf == "":
		print('Нужно было ввести номер полки')
		return False
	if new_shelf in directories.keys():
		print('Полка "{}" уже есть'.format(new_shelf))
		return False
	else:
		directories[new_shelf] = list()
		print('Полка "{}" добавлена'.format(new_shelf))
		return True


def show_commands() -> None:
	print("Нет такой команды")
	print("\n".join(["{} - {}".\
		format(key, function.__name__) for key, function in commands.items()]))


if __name__ == '__main__':
	
	commands = {
		"p": show_document_owner,
		"l": show_documents_list,
		"s": show_shelf,
		"a": add_document,
		"d": delete_document,
		"m": move_document,
		"as": add_shelf,
	}
	
	while True:
		command = input("Введите команду: ").strip()
		
		if command.lower() == "q":
			break
		
		commands.get(command.lower(), show_commands)()
