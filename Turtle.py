"""Create a Turtle Program that will draw a 3-dimensional cube"""

import turtle
trump = turtle.Turtle()
for i in range (4):
        trump.forward(150)
        trump.right(90)

trump.left(135)
trump.forward(100)
trump.right(135)
trump.forward(150)
trump.right(45)
trump.forward(100)
trump.right(135)
trump.forward(150)
trump.left(90)
trump.forward(150)
trump.right(135)
trump.forward(100)
trump.right(45)
trump.forward(150)
"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
import turtle
trump = turtle.Turtle()
def AddTen(n):
    n = n + 10
    return n
print ()


l = 14
w = 20
def DrawRectangle(trump, l, w):
    for i in range (4):
        trump.forward(14)
        trump.right(90)
        trump.forward(w)
DrawRectangle (trump, l, w)
