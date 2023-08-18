# Задача 34:  Винни-Пух попросил Вас посмотреть, 
# есть ли в его стихах ритм. Поскольку разобраться 
# в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в 
# порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def phrase_check(str):
    vowel_list = [ "у", "е", "ы", "а", "о", "э", "я", "и", "ю", "ё"]
    qual_char = []
    for i in range(len(str)):
        qual_char.append(list(filter(lambda x: x in vowel_list, str[i])))
    if len(set((list(map(len, qual_char))))) != 1:
        print("Пам парам")
    else:
        print("Парам пам-пам")
phrase = (input("Введите фразу: ").split())
phrase_check(phrase)