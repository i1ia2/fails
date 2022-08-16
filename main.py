import os.path
import pprint
# def vse_menu(files:str) -> dict:
#     with open('spisok.txt', encoding="utf-8") as f:
#         ingredienti = {}
#         for fail in f:
#             lines = fail.strip()
#             ingredienti[lines] = []
#             for menu in range(int(f.readline())):
#
#                 razdelenie = f.readline().split(' | ')
#                 ingredienti[lines].append({'ingredient_name': razdelenie[0],
#                                            'quantity': int(razdelenie[1]),
#                                            'measure': razdelenie[2].strip()})
#
#             f.readline()
#     return ingredienti
#
# print(vse_menu(dict))

def vse_menu(files:str) -> dict:
    cook_dikt = {}
    with open('spisok.txt', encoding="utf-8") as f:
        for line in f:
            dish_name = line.strip()
            counter = f.readline()
            list_of_ingrigient = []
            for i in range(int(counter)):
                ingridient = f.readline().split(' | ')
                list_of_ingrigient = ({'ingredient_name': ingridient[0],
                                'quantity': ingridient[1],
                                'measure': ingridient[2]})
            cook_dikt[dish_name] = list_of_ingrigient
            f.readline()
        return cook_dikt


def list_gosti(dishen: list, person: int, cook_book: dict) -> dict:
    result = {}
    for dish in dishen:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                       'quantity': (consist['quantity'] * person)}
        else:
            print(f'этого блюда {dish}, нет в книге рецептов')
    return result
print(list_gosti(dict))

