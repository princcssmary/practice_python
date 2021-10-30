import random
while True:
    a = random.randint(1, 9)
    b = int(input("Попробуй угадать число, которое я загадал! Введи число от 1 до 9: "))
    if b == a:
        print("Ты угадал! Поздравляю! Еще раз?")
        c = input("")
        if c == "Нет":
            break
    elif b != a:
        print("Не угадал! Еще раз?")
        c = input("")
        if c == "Нет":
            break
