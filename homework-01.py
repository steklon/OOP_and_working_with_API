from pprint import pprint

def new_cook_book():
    with open('recipes.txt', encoding='UTF-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            dish, num_, *products = line.split('\n')
            ingredients = []
            for product in products:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, product.split(' | '))
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for foods, products in new_cook_book().items():
        for dish in dishes:
            if dish == foods:
                for i in products:
                    meal = dict()
                    meal["measure"] = i.get("measure")
                    meal["quantity"] = i.get("quantity") * person_count
                    result[i.get("ingredient_name")] = meal
    return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
