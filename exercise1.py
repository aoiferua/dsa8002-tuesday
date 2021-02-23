# 1. Write a function istrcmp() to compare two strings, ignoring the case.
string_1 = input('Please enter a string: ')
string_2 = input('Please enter a string: ')


def istrcmp():


    if string_1.lower() == string_2.lower():
        print('The strings are the same!')
    else:
        print('The strings are NOT the same!')

istrcmp()