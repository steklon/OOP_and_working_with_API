from pprint import pprint
print('______________________________')


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
print('______________________________')

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 4))
print('______________________________')

# Задание №3:


class File:
    def __init__(self, link_to_file):
        self.link_to_file = link_to_file

    def number_of_lines(self):
        number_lines_file = len(self.reading_file())
        return number_lines_file

    def __str__(self):
        return f'{self.link_to_file}'

    def reading_file(self):
        with open(self.link_to_file, encoding='UTF-8') as file:
            data = file.read().split('\n')
        return data

    def write_to_file(self, data):
        with open(self.link_to_file, 'a', encoding='UTF-8') as file:
            file.write(f'{data}\n')


def preparation():
    file_1 = File('1.txt')
    file_2 = File('2.txt')
    file_3 = File('3.txt')
    write_file = File('write.txt')

    file_name_list = [f'{file_1}', f'{file_2}', f'{file_3}']
    file_number_list = [file_1.number_of_lines(), file_2.number_of_lines(), file_3.number_of_lines()]
    file_text_list = [file_1.reading_file(), file_2.reading_file(), file_3.reading_file()]

    tuples_list = list(zip(file_name_list, file_number_list, file_text_list))
    tuples_list.sort(key=lambda x: x[1])

    for name, number, text in tuples_list:
        write_file.write_to_file(name)
        write_file.write_to_file(number)
        for line in text:
            write_file.write_to_file(line)


preparation()
