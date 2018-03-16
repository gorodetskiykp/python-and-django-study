def read_cook_book(file_name):
    cook_book = {}
    with open(file_name) as cook_book_file:
        for dish in cook_book_file:
            dish = dish.strip().lower()
            cook_book[dish] = list()
            for line in range(int(cook_book_file.readline())):
                ingridients = cook_book_file.readline().split(' | ')
                cook_book[dish].append({
                    'ingridient_name': ingridients[0].strip().lower(), 
                    'quantity': int(ingridients[1].strip()), 
                    'measure': ingridients[2].strip().lower()})
            cook_book_file.readline()
    return cook_book


def get_shop_list_by_dishes(person_count, dishes):
    shop_list = {}
    cook_book = read_cook_book("cook_book.txt")
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
                    new_shop_list_item['quantity']
    return shop_list
    
    
def print_shop_list(shop_list):
    full_shop_list = []
    for shop_list_item in shop_list.values():
        full_shop_list.append('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    for shop_list_item in sorted(full_shop_list):
        print(shop_list_item)


def create_shop_list():
    person_count = int(input("Введите количество человек: "))
    dishes = input("Введите блюда в расчете на одного человека через запятую: ").lower().split(", ")
    shop_list = get_shop_list_by_dishes(person_count, dishes)
    print_shop_list(shop_list)
    

create_shop_list()
