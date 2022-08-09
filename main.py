import os.path
def vse_menu(files:str) -> dict:
    with open('spisok.txt', encoding="utf-8") as f:

        ingredienti = {}
        for fail in f:
            lines = fail.strip()
            ingredienti[lines] = []

            for menu in range(int(f.readline())):
                razdelenie = f.readline().split(' | ')
                ingredienti[lines].append({'ingredient_name': razdelenie[0],
                                           'quantity': int(razdelenie[1]),
                                           'measure': razdelenie[2].strip()})
            f.readline()
    return ingredienti

print(vse_menu(dict))