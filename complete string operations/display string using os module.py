import os
size = os.get_terminal_size().columns

string = input("enter your string")
print(string.center(size).title())
print(string.ljust(size).title())
print(string.rjust(size).title())
