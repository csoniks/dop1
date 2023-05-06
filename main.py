import re
file = open("synonyms.txt", "r+")
spisok_sin = file.readlines()
print(spisok_sin)
def find_synonim():
    cnt = 0
    user_word = input(str("найти синоним: "))
    file.seek(0)
    for i in file:
        if user_word in i:
            #print(line.strip())
            syn = re.split(r"[ ]", i) #делит строку по '-'  и возвращает список получившихся подстрок
            #print(syn)
            cnt = 1
            if user_word == syn[0]:
                print(syn[2])
                if len(syn) == 4:
                    print(syn[3])
            else:
                print(syn[0])
    if cnt == 0:
        print("синоним не найден")

def choice(user_word):
    add_choice = input("нравится синоним? ")
    if add_choice == 'нет':
        print("сейчас добавим ваш вариант")
        return dobavim_synonims(user_word)
    else:
        return

def dobavim_synonims(user_word):
    x = input("введите свой вариант: ")
    newwords = user_word.title() + " - " + x + "\n" #title первая заглавная
    file.write(newwords) #записываем в конец файлика
    print("добавлено")
    return

find_synonim()