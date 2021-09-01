list_example = []
print(bool(list_example))
list_example1 = [16, 2, 1, 2, 3]
print(bool(list_example1))
print(list_example1)
print(list_example1[0])
print(list_example1[1])
print(list_example1[1:3])
list_example1[0] = 11
print(list_example1)
print(dir(list_example1))
print(list_example1.index(11))
print(list_example1.count(2))
list_example1.clear()
print(list_example1)
list_example3 = [1, 2, 3, 4, 5]
list_example4 = list_example3.copy()
print(list_example4)
print(id(list_example3))
print(id(list_example4))
list_example5 = list_example3
print(list_example5)
print(id(list_example3))
print(id(list_example5))
list_example3.append(100)
print(list_example3)
list_example5.insert(2,200)
print(list_example5)
list_example6=[1,2]
list_example7=[3,4]
list_example7.append(list_example6)
print(list_example7)
list_exampl=[11,22]
list_exampl.extend(list_example6)
print(list_exampl)
list_exampl.remove(2)
print(list_exampl)
list_exampl.pop()
print(list_exampl)
list_example6.reverse()
print(list_example6)
list_example5.sort()
print(list_example5)

