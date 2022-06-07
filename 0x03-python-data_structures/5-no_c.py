#!/usr/bin/python3
def no_c(my_string):
    x = list(my_string)
    l = []

    for i in x:
        if i.casefold() != 'C'.casefold():
            l.append(i)
    return ("".join(l))
