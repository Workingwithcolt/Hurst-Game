import turtle as tim
from turtle import Screen
from main import rgb_colors
import random
count = 0

tim.colormode(255)


table = [10,30,50,70,90]
List = [20,40,60,80,100]
#
# for j in range(1, 20):
#     if (10 * j % 2) != 0:
#         table.append(5 * j)

# for i in range(1, 12):
#     if (10 * i % 2) == 0:
#         List.append(5 * i)
# multiple of 10
print(List)
print(table)
tim.speed(2)
tim.pensize(2)


def forward_dot():
    tim.dot(20,random.choice(rgb_colors))
    tim.penup()
    tim.forward(40)
    tim.pendown()


def backword_dot():
    # tim.dot(10, "red")
    tim.left(90)
    tim.penup()
    tim.forward(40)
    tim.pendown()
    # tim.dot(10, "red")


# list is the combination of even that is multiple of 10 from 1 to 10
# Table is the combination of multiple of 5 from 1 to 10
j = 0
k = 0
for i in range(1, 200):
    count += 1
    # that method will print the dots from the start to the end
    if count == List[k]:
        tim.penup()
        tim.backward(40)
        tim.right(90)
        tim.penup()
        tim.forward(40)
        tim.right(90)
        k += 1
    elif i == table[j]:
        tim.penup()
        tim.backward(40)
        backword_dot()
        tim.dot(20, random.choice(rgb_colors))
        tim.left(90)
        j += 1
    else:
        forward_dot()

screen = Screen()
screen.exitonclick()
