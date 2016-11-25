# import turtle
#
# def draw_square():
#     window = turtle.Screen()
#     window.bgcolor("white")
#
#     brad = turtle.Turtle()
#     brad.shape("turtle")
#     brad.color("green")
#     brad.speed(2)
#     count = 0
#     while count <= 3:
#         brad.forward(100)
#         brad.right(90)
#         count = count + 1
#     angie = turtle.Turtle()
#     angie.shape("arrow")
#     angie.color("red")
#     angie.circle(100)
#
#     tom = turtle.Turtle()
#     tom.color("blue")
#     tom.shape("circle")
#     count = 0
#     while count <= 2:
#         tom.forward(320)
#         tom.left(120)
#         count = count + 1
#
#     window.exitonclick()
#
# draw_square()

###draw a circle from a bunch of squares (with better code)###

import turtle

def draw_shapes(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #create square brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(10)
    for i in range(1,37):
        draw_shapes(brad)
        brad.right(10)

    window.exitonclick()

draw_art()
