#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = 0
    for x in set(my_list):
        sum_list += x

    return sum_list
