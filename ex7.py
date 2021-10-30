a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for element in a:
    if element % 2 == 0:
        b.append(element)
        
print(b)


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [elem for elem in a if elem % 2 == 0]
print(b)
