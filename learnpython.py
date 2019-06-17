# Learn Python - Full Course for Beginners [Tutorial]
# URL: https://www.youtube.com/watch?v=rfscVS0vtbw

from math import *

character_name = "jingwei"
character_age = 29.99
is_male = True
is_tall = True

friends = ["Tom","jignwei","Kong","Yuki", "Bad guy"]
print(friends[1:])

# Tuples are mutable objects that can not be chagned.
coordinates = [(4,3),(22,11),(1923,18828)]

print(coordinates)

# functinos

def say_hi(name):
    print("Hello " + name)

say_hi("jingwei")

def test(num):
    return num * num * num

print(test(4))


if is_male or is_tall:
    print("You are male or tall or both")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("option 3")
else:
    print("You are neither male nor tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3090,2,56))

monthConversions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
}
print(monthConversions.get("Lv","Not a valid key"))


secret_word = "jingwei"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, YOU LOSE!")
else:
    print("You win")

#
# complex_list = {
#     names:["1","abdij"],
#     ages: [1,2,3]
# }
#
# print(complex_list)
#
