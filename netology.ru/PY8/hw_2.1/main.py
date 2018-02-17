cook_book = {}
with open('recipes.txt', encoding='utf8') as file:
    for ingredient in file:
        key = ingredient.strip().lower()
        cook_book[key] = []
        for _ in range(int(file.readline())):
            ingredient_name, quantity, measure = \
                file.readline().strip().split(' | ')
            cook_book[key].append({
                'ingredient_name': ingredient_name,
                'quantity' : int(quantity),
                'measure' : measure
                }) 
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingradient in cook_book[dish]:
            new_shop_list_item = dict(ingradient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
    # person_count = int(input('Введите количество человек: '))
    person_count = 3
    # dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    dishes = 'стейк, салат'.lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()

