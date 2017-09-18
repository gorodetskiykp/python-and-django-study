import json

cook_book = {
    'яйчница': [
        {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
    'стейк': [
        {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
    'салат': [
        {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
}

json_data = json.dumps(cook_book, indent=4)

with open('recipes.json', 'w') as file:
    file.write(json_data)