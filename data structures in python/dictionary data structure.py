dict_example = {}
print(dict_example, type(dict_example))
print(bool(dict_example))

dict_example1 = {'name': 'manisha', 'age': 25, 'work': 'DC'}
print(dict_example1)
print(dict_example1['name'])
print(dict_example1.get('work'))
# print(dict_example1['salary'])
print(dict_example1.get('salary'))
print(dir(dict_example1))
dict_example1.clear()
print(dict_example1)

dict_example2 = {'roll number': 1, 'class': 10, 'subject': 'maths'}
print(dict_example2)
dict_example2['marks'] = 29
print(dict_example2)
dict_example2['roll number'] = 2
print(dict_example2)
print(dict_example2.keys())
print(dict_example2.values())
print(dict_example2.items())
y = dict_example2.copy()
print(y)
print(id(y))
print(id(dict_example2))
dict_example3 = {'mobile': 'samsung'}
dict_example2.update(dict_example3)
print(dict_example2)
dict_example2.pop('class')
print(dict_example2)
dict_example2.popitem()
print(dict_example2)

keys_example = ['A', 'B', 'C']
dict_example4 = dict.fromkeys(keys_example)
print(dict_example4)
dict_example4['A'] = "1"
print(dict_example4)

dict_example5 = {}
dict_example5.setdefault('password', 'ASD')
print(dict_example5)
dict_example5.setdefault('password', 'QWE')
print(dict_example5)


