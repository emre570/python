list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

list3 = []

for num in list1:
    if(num % 2 == 0):
        list3.append(num)

for num in list2:
    if(num % 2 == 1):
        list3.append(num)

print(list1)
print(list2)
print(list3)