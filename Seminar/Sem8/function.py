def add_contact(file_name):
    with open('phone_book.txt', 'a') as file_name:
        print("Введите данные: ")
        file_name.write(input() + "\n")
    file_name.close()
    
def search_contact(file_name):
    stri = input("Введите фамилию: ")
    file_name = open('phone_book.txt', 'r')
    for line in file_name:
        if stri in line:
            print("\n"+line)
            break
    else: 
        print("\nТакого нет")
        a = input("\nХотите добавить?(yes/no): ")
        if a == "yes":
            with open('phone_book.txt', 'a') as file_name:
                file_name.write(stri + " ")
                n = str(input("Добавьте номер телефона: "))
                file_name.write(n + "\n")
            file_name.close()
    file_name.close()

def show_all(file_name):
    file_name = open('phone_book.txt', 'r')
    for line in file_name:
        print(line)
    file_name.close()

def change_contact():
    with open('phone_book.txt', 'r') as f:
        lines = f.readlines()
    print("Что хотите изменить?")
    print("1 - Только имя или номер.")
    print("2 - И имя и номер.")
    num = int(input())
    if num == 1:
        stri = input("Введите фамилию контакта или номер который хотите изменить: ")
        found = False
        with open('phone_book.txt', 'w') as f:
            new_str = str(input("Введите новые данные: "))
            for line in lines:
                if stri in line:
                    found = True
                    line = line.replace(stri, new_str)
                f.write(line)
        if found:
            print("Контакт успешно изменен.")
        else:
            print("Такого нет")
    elif num == 2:
        stri = input("Введите фамилию контакта который хотите изменить: ")
        found = False
        with open('phone_book.txt', 'w') as f:
            new_str = str(input("Введите новые данные (имя и телефон): ")+'\n')
            for line in lines:
                if stri in line:
                    found = True
                    stri = line
                    line = line.replace(stri, new_str)
                f.write(line)
        if found:
            print("Строка успешно изменена")
        else:
            print("Такого нет")
    else: 
        print("Ошибка.")

def del_all(file_name):
    mess = str(input("Вы уверены?(yes/no) "))
    if mess == "yes":
        with open('phone_book.txt', 'w') as file_name:
            a = ""
            file_name.write(a)
        file_name.close()
    file_name.close()

def del_cont():
    stri = input("Введите фамилию: ")
    with open('phone_book.txt', 'r') as f:
        lines = f.readlines()  
    found = False
    with open('phone_book.txt', 'w') as f:
        for line in lines:
            if stri in line:
                found = True
                stri = line
                line = line.replace(stri, "")
            f.write(line)
    if found:
        print("Строка успешно удалена")
    else:
        print("Такого нет")