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
        show_all(file_name)
        print()
        interface(file_name)
    elif num == 4:
        change_contact(file_name)
        print()
        interface(file_name)
    elif num == 5:
        file_name.close()
    elif num == 6:
        del_cont(file_name)
        print()
        interface(file_name)
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
    print("3 - Показать все контакты.")
    print("4 - Изменение контакта.")
    print("5 - Выход.")
    print("6 - Удаление контакта.")


    print("9 - Удалить все данные.")
    num = int(input("Выберите действие: "))
    return num