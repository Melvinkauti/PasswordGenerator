import random

# create strings that contain all possible characters for the passwords
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*(){}[]:;''|<>?/"

# set up boolean for selecting the values we want in our password
upper, lower, nums, syms = True, True, True, False

# create an empty string
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 5

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)


