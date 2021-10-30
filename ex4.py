number = int(input("Введите число: "))
a = range(1, number+1)
for element in a:
    if number % element == 0:
        print(element)
