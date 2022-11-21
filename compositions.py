import turtle
from logics import *

def composition_no_1():
    turtle.pensize(9)
    turtle.color("blue")
    draw_horizontal_lines(2)
    turtle.color("gray")
    draw_horizontal_lines(3)
    turtle.color("black")
    draw_vertical_lines(3)
    turtle.color("gray")
    draw_vertical_lines(2)
    turtle.color("pink")
    draw_vertical_lines(12)

def pink_composition_no_1():
    turtle.Screen().bgcolor("pink")
    turtle.pensize(9)
    turtle.color("blue")
    draw_horizontal_lines(2)
    turtle.color("gray")
    draw_horizontal_lines(3)
    turtle.color("black")
    draw_vertical_lines(3)
    turtle.color("gray")
    draw_vertical_lines(2)
    turtle.color("pink")
    draw_vertical_lines(12)

def composition_arched_lines_without_lifting_pen():
    turtle.color("blue")
    draw_horizontal_line_of_arcs(10, 50, 12)
    turtle.color("pink")
    draw_vertical_line_of_arcs(10, 50, 12)

def composition_with_grid():
    turtle.color("blue")
    draw_arched_grid_without_lifting_pen(12)