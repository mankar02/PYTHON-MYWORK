x=3
y=4
type_a=print(type(x))
type_b=print(type(y))
print(type_a is type_b)
print(type_a is not type_b)

list_example=[1,2,3,4,5]
print(5 in list_example)

birth_year=[1990.1991,1992,1993,1994]
my_birthyear=1996
print(my_birthyear in birth_year)

vowels=['a','e','i','o','u']
check='e'
if check in vowels:
    print("it is vowel")
else:
    print("it is consonants")
