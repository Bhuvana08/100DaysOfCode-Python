from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.forward(-10)


def turn_anticlockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.reset()



screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_anticlockwise, key="a")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()

# W - forwards
# S - backwards
# A - Counter-clockwise
# D - Clockwise
# c = Clear screen
