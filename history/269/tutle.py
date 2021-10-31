# from turtle import *
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t2.setposition(50, -50)
t2.rt(90)
t1.pensize(1)
t1.color(0, 0, 0)
for i in range(0, 180):
    t1.forward(2)
    t1.right(2)

t2.color(255, 255, 255)
t2.pensize(5)
for i in range(0, 180):
    t2.forward(2)
    t2.right(2)
#
# hideturtle()
# while True:
#     pensize(1)
#     color(0,0,0)
#     for i in range(0, 180):
#         forward(2)
#         right(2)
#     color(255,255,255)
#     pensize(5)
#     for i in range(0, 180):
#         forward(2)
#         right(2)
