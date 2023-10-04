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


print('** cook_book: **')
pprint(new_cook_book())
print()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for foods, lists_of_all_products in new_cook_book().items():
        for dish in dishes:
            if dish == foods:
                for ingredient in lists_of_all_products:
                    portion = dict()
                    portion["measure"] = ingredient.get("measure")
                    if ingredient.get("ingredient_name") in result.keys():
                        units = result.get(ingredient.get("ingredient_name"))
                        portion["quantity"] = units.get('quantity') + ingredient.get("quantity") * person_count
                    else:
                        portion["quantity"] = ingredient.get("quantity") * person_count
                    result[ingredient.get("ingredient_name")] = portion
    return result


print('** Необходимое количество ингредиентов: **')
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 4))
