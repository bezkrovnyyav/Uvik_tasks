
data = [1, 3, 5, 7, 10, 11, 34, 50]
element = 10

first = 0
last = len(data) - 1
middle = (first + last) // 2

while element != data[middle] and first <= last:
    if  element > data[middle]:
        first = middle + 1
    elif  element < data[middle]:
        last = middle - 1
    middle = (first + last) // 2

if element == data[middle]:
    print(middle)
else:
    print("No such number in the list")
