a = 0
b = 1
array = []
nb1 = int(input())
nb2 = int(input())
nb3 = int(input())
array.append(nb1)
array.append(nb2)
array.append(nb3)
while b < len(array):
    if array[a] > array[b]:
        v = array[b]
        del array[b]
        array.insert(0,v)
    if b < len(array):
        b += 1
print(array)
