import os.path
import pprint

def vse_menu():
    cook_dikt = {}
    with open('spisok.txt', encoding="utf-8") as f:
        for line in f:
            dish_name = line.strip()
            counter = f.readline()
            list_of_ingrigient = []
            for i in range(int(counter)):
                ingridient = f.readline().split(' | ')
                list_ingrigient = ({'ingredient_name': ingridient[0],
                                'quantity': int(ingridient[1]),
                                'measure': ingridient[2]})

                list_of_ingrigient.append(list_ingrigient)

            cook_dikt[dish_name] = list_of_ingrigient
            f.readline()
        return cook_dikt


def list_gosti(dish_name, person_count) -> dict:
    cook_book = vse_menu()
    result = {}
    for dish in dish_name:
        if dish in cook_book.keys():
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                       'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'этого блюда {dish}, нет в книге рецептов')
    return result

# pprint.pp(list_gosti(['Омлет', 'Утка по-пекински'], 7))

def texts():
    TEXTS = 'failsss'
    full_path_to_texts = os.path.join(os.getcwd(), TEXTS)
    texts_list = os.listdir(full_path_to_texts)
    all_texts = {}
    for file in texts_list:
        file_path = os.path.join(full_path_to_texts, file)
        with open(file_path, 'r', encoding = 'utf-8') as file_to_read:
            list_of_strings = []
            for line in file_to_read:
                list_of_strings.append(line.strip())
            text = '\n'.join(list_of_strings)
        all_texts[len(list_of_strings)] = {'name': file, 'length': str(len(list_of_strings)), 'text': text}
    for all in sorted(all_texts):
        sorted_all = all_texts.get(all)
        pprint.pp(sorted_all)
    return

if __name__ == '__main__':
    texts()