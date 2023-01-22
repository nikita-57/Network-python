list1 = [10,20,30,77]
list2 = ['one', 'dog', 'seven']
list3 = [1, 20, 40, 3]

list1.extend(list3)
list1.insert(1,4)
print(f'{list1}')
print(sorted(list1))