set_example1={}
print(bool(set_example1))
set_example = {1, 2, 5, 3, 8, 44,22 }
print(set_example)
print(bool(set_example))
print(set_example,type(set_example))

list_examle=[11,2,21,3]
set_example2=set(list_examle)
print(set_example2)

list_examle1=[1,2,1,3,1,4,2,3,4]
set_example3=set(list_examle1)
print(set_example3)

print(dir(set))

a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(a.intersection(b))