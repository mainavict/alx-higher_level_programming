#!/usr/bin/python3
j = 123

upper = False
for i in range(0,26):
    if upper == False:
        if j <=123 and j>=97:
            j -=1
        elif j<=90 and j >=65:
            j = j+32 -1
        upper = True

    elif upper == True:
         j -=33
         upper = False

    print('{:c}'.format(j),end='')
