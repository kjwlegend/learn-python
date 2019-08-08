# Learn Python - Full Course for Beginners [Tutorial]
# URL: https://www.youtube.com/watch?v=rfscVS0vtbw

from youtube.student import Student
from youtube.Question import Question
from youtube.Chef import Chef
from youtube.ChineseChef import ChineseChef

myChef = Chef()
myChineseChef = ChineseChef()

myChef.make_chicken()
myChineseChef.make_chinese_dish()
student1 = Student("jingwei", "marketing", 3, False)
student2 = Student("Jingwei222", "Acount", 4, True)
#
# print(student1.gpa)
# print(student2.is_on_probation)
print(student2.on_honor_roll())
question_prompts = [
    "The answer for Q1 is: \na\nb\nc",
    "The answer for Q2 is: a\nb\nc",
    "The answer for Q3 is: a\nb\nc"
]
print(question_prompts)


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("you got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

#
# character_name = "jingwei"
# character_age = 29.99
# is_male = True
# is_tall = True
#
# friends = ["Tom","jignwei","Kong","Yuki", "Bad guy"]
# print(friends[1:])
#
# # Tuples are mutable objects that can not be chagned.
# coordinates = [(4,3),(22,11),(1923,18828)]
#
# print(coordinates)
#
# # functinos
#
# def say_hi(name):
#     print("Hello " + name)
#
# say_hi("jingwei")
#
# def test(num):
#     return num * num * num
#
# print(test(4))
#


# if is_male or is_tall:
#     print("You are male or tall or both")
# elif is_male and not(is_tall):
#     print("You are short male")
# elif not(is_male) and is_tall:
#     print("option 3")
# else:
#     print("You are neither male nor tall")
#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(3090,2,56))
#
# monthConversions = {
#     "Jan": "January",
#     "Feb": "Feburary",
#     "Mar": "March",
# }
# print(monthConversions.get("Lv","Not a valid key"))
#
# #
# # secret_word = "jingwei"
# # guess = ""
# # guess_count = 0
# # guess_limit = 3
# # out_of_guesses = False
# #
# # while guess != secret_word and not(out_of_guesses):
# #     if guess_count < guess_limit:
# #         guess = input("Enter the guess: ")
# #         guess_count += 1
# #     else:
# #         out_of_guesses = True
# # if out_of_guesses:
# #     print("out of guesses, YOU LOSE!")
# # else:
# #     print("You win")
#
# #
# len(friends)
# for index in range(len(friends)):
#     print(friends[index])
#
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
#
# print(raise_to_power(2,8))
#
#
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# print(number_grid[3][0])
#
# for row in number_grid:
#     for col in row:
#         print(col)
#
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate("jingwei"))
#
#
# try:
#     value = 10 / 0
#     number = int(input("input a number:" ))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("invalid number")
#
#
