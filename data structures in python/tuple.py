tuple_example=()
tuple_example1=(1,2,3)
print(tuple_example)
print(tuple_example1)
print(bool(tuple_example))
print(bool(tuple_example1))
tuple_example2=(1,2,[4,5])
print(tuple_example2)
print(tuple_example2[2])
print(tuple_example2[2][1])
#below code will not work as tuple are immutable
'''
tuple_example1=(1,2,3)
tuple_example[1]=44
print(tuple_example)
'''
print(dir(tuple_example))
print(tuple_example1.count(1))
print(tuple_example1.index(3))
print(tuple_example1.__len__())

print(tuple_example1[:])
print(tuple_example1[:1])
print(tuple_example1[1:])
a=1,2,3
print(a,type(a))