print("program to convert string in uppercase or lowercase")
string_required=input("please enter your string")
case_required=input("please enter whether you want UPPER CASE or lower case say UPPER CASE or say lower case")
if string_required.islower():
    if case_required == "lower case":
        print("the string you entered is already lowercase")
    else:
        if case_required=="UPPER CASE":
            print(f"the upper case of your string is {string_required.upper()}")
else:
    if string_required.isupper():
        if case_required == "UPPER CASE":
            print("the string you entered is already uppercase")
        else:
            if case_required == "lower case":
                print(f"the lowercase of your string is {string_required.lower()} ")










