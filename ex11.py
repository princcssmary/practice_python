num = int(input("Введите число: "))
a = range(1, num+1)
b = []
for element in a:
    if num % element == 0 and element != 1 and element != num:
        b.append(element)
num_of_devisors = len(b)
if num_of_devisors == 0:
    print("Число простое. У него нет делителей.")
else:
    print("Число не является простым.")

        
        
