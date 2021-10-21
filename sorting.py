a = 0
b = 1
array = [5,4,7,101,2]
while b < len(array):
    if array[a] > array[b]:
        v = array[b]
        del array[b]
        array.insert(0,v)
    if b < len(array):
        b += 1
print(array)
