#!/usr/bin/pyhton3
def remove_char_at(str, n):
    j=0
    str2 = ''
    for i in str:
        if j == n:
            i =''
        j+=1
        str2 = str2 + i
    return (str2)

