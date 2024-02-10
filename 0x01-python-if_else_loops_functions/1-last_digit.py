#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
digits = []
if num < 0:
    digits.append(number % -10)
    if digits[0] < 6 and digits[0] != 0:
        print(f"Last digit of {num} is {digits[0]} and is less than 6 and not 0")

elif num > 0:
    digits.append(number % 10)
    if digits[0] > 5:
        print(f"Last digit of {num} is {digits[0]} and is greater than 5")

elif num == 0:
    digits.append(number % 10)
    print(f"Last digit of {num} is {digits[0]} and is 0")
