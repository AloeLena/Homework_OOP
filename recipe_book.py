# Задание 1

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def split_text(text):
    return [i.splitlines() for i in text.split('\n\n')]

def split_ingredients_data(lst):
    return lst[:1] + [i.split('|') for i in lst[2:]]

def convert_list_to_dict(lst):
    return {lst[0]: [{'ingredient_name': i[0], 'quantity': int(i[1]), 'measure': i[2]} for i in lst[1:]]}

def load_data(file_path):
    result = {}
    text = read_file(file_path)
    dish_list = split_text(text)
    format_dish_list = [split_ingredients_data(i) for i in dish_list]
    for i in format_dish_list:
        result.update(convert_list_to_dict(i))
    return result

recipe_book = load_data('recipes.txt')

for key, value in recipe_book.items():
    print("{0}:\n{1}".format(key,value))

# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in recipe_book:
            for ingredient in recipe_book[dish]:
                name = ingredient.get('ingredient_name')
                quantity = int(ingredient.get('quantity', 0)) * person_count
                measure = ingredient.get('measure', '')
                if name:
                    if name not in shop_list:
                        shop_list[name] = {
                            'quantity': quantity, 'measure': measure}
                    else:
                        shop_list[name]['quantity'] += quantity
                else:
                    print(f"Ингредиент не найден.")
        else:
            print(f"Блюдо '{dish}' не найдено.")
    return shop_list

print()
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5))