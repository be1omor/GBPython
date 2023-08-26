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
                file_name.write('\n'+ stri + " ")
                n = str(input("Добавьте номер телефона: "))
                file_name.write(n + "\n")
            file_name.close()

    file_name.close()

def show_all(file_name):
    file_name = open('phone_book.txt', 'r')
    for line in file_name:
        print(line)
    file_name.close()

def change_contact(file_name):
    stri = input("Введите фамилию: ")
    new_str = str(input("Введите новые данные: "))
    with open('phone_book.txt', 'r') as f:
        lines = f.readlines()  
    found = False
    with open('phone_book.txt', 'w') as f:
        for line in lines:
            if stri in line:
                found = True
                line = line.replace(stri, new_str)
            f.write(line)
    if found:
        print("Строка успешно изменена")
    else:
        print("Такого нет")


def del_all(file_name):
    mess = str(input("Вы уверены?(yes/no) "))
    if mess == "yes":
        with open('phone_book.txt', 'w') as file_name:
            a = ""
            file_name.write(a)
        file_name.close()
    file_name.close()