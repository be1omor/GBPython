from function import *

def interface(file_name):
    num = text_interface()
    if num == 1:
        add_contact(file_name)
        print()
        interface(file_name)
    elif num == 2:
        search_contact(file_name)
        print()
        interface(file_name)
    elif num == 3:
        change_contact()
        print()
        interface(file_name)
    elif num == 4:
        del_cont()
        print()
        interface(file_name)
    elif num == 5:
        show_all(file_name)
        print()
        interface(file_name)
    elif num == 6:
        file_name.close()
    elif num == 9:
        del_all(file_name)
        print()
        interface(file_name)
    else:
        print('\n'+"Ошибка! Повторите ввод."+'\n')
        interface(file_name)

def text_interface():
    print("1 - Добавить контакт.")
    print("2 - Поиск контакта.")
    print("3 - Изменение контакта.")
    print("4 - Удаление контакта.")
    print("5 - Показать все контакты.")
    print("6 - Выход.")
    print("9 - Удалить все данные.")
    num = int(input("Выберите действие: "))
    return num