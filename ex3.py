a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in a:
    if element < 5:
        print(element)
    elif element > 10:
        if element % 5 == 0:
            print(element)
