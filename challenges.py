# Import math Library
from math import pi

#1
# radius = float(input("Radius? "))
# print(f"The area is {round(pi*radius**2, 2)}")

#2
# user_input = input("CSV? ")
# my_list = user_input.split(",")
# my_tuple = tuple(my_list)

# print(my_list)
# print(my_tuple)

#3
# ui = input("Filename? ")
# extension = ui[ui.index("."):len(ui)]
# print(extension)

#4
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])

#5
# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)

#6
# un = str(input("Integer? "))
# print(int(un) + int(un + un) + int(un + un + un))

#7
# print(abs.__doc__)

#8
# from calendar import month
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(month(y, m))

#9
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)

#10
# ml1 = [6, 8 ,19, -1, 2, 45]
# ml2 = [1, 8 ,19, 21, 23, 45]

# def in_asc_order(list):
#     return sorted(list) == list

# print("Sorted") if in_asc_order(ml2) else print("Unsorted")

#11
# ml1 = [6, 8 ,19, -1, 4, 45]
# def index_equals_value(arr):
#     for index, value in enumerate(arr):
#         if index == value:
#             return index
#     return -1

# print(index_equals_value(ml1))

#12
sentence = "the lazy dog jumped over the quick brown fox"
to_array = [chr(ord(char)+2) for char in sentence]
encoded_sentence = "".join(to_array)
print(encoded_sentence)
