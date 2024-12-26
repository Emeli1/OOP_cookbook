import os
from pprint import pprint

# Задание 1

def read_cook_book():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()  # название блюда
            count = int(f.readline())  # количество ингридиентов
            ingredients = list()
            for item in range(count):
                ingrs = {}
                ingredient = f.readline().strip() #читаем построчно
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingredient.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ingredients.append(ingrs)
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book

# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_cook_book()

    for dish_name in dishes:              #названия блюд которые передали
        if dish_name in cook_book:              #если они есть в cook_book
            for ings in cook_book[dish_name]:        # проходимся по ингридиентам этого блюда
                ing_list = {}
                if ings['ingredient_name'] not in shop_list:
                    ing_list['measure'] = ings['measure']
                    ing_list['quantity'] = ings['quantity'] * person_count
                    shop_list[ings['ingredient_name']]= ing_list
                else:
                    shop_list[ings['ingredient_name']]['quantity'] = shop_list[ings['ingredient_name']]['quantity'] + \
                                                                      ings['quantity'] * person_count
        else:
            return 'ошибка'
    return shop_list

# pprint(read_cook_book())
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


# Задание 3

base_path = os.getcwd()
files_folder = os.path.join(os.getcwd(), 'files')                # путь до папки с файлами
file_for_unite = os.path.join(os.getcwd(), 'united_file.txt')   # путь в файл куда обединить
full_path = os.path.join(base_path, files_folder)

def lines_count(file):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)                              # функция подсчёта количества строк в файле

def unite(full_path, file_for_unite):
    files = []

    for f in list(os.listdir(full_path)):                       # проходимся по каждому файлу в списке формируем список
        # по каждому файлу, кот. сост. из кол-ва строк и пути к этому файлу, названия и доб. в новый список
        files.append([(lines_count(os.path.join(files_folder, f))), os.path.join(base_path, files_folder, f), f])

    for file_item in sorted(files):
        with open(file_for_unite, 'a', encoding='utf-8') as file:
            file.write(f'{file_item[2]}\n')   # название файла
            file.write(f'{file_item[0]}\n')   # количество строк
            with open(file_item[1], 'r', encoding= 'utf-8') as f:    # открываем путь из списка, для чтения
                count = 1
                for line in f:
                    file.write(f'Строка номер {count} файла номер {file_item[2][0]} : {line}')  # записываем в объед. файл
                    count += 1
            file.write(f'\n')


unite(full_path, file_for_unite)






