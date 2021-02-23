# 2.   Write   a   function   istrcmp2()   to   compare   two   strings, considering the case sensitivity.
string_1 = input('Please enter a string: ')
string_2 = input('Please enter a string: ')


def istrcmp2():
    if string_1 != string_2:
        print(False)
    else:
        print(True)

istrcmp2()