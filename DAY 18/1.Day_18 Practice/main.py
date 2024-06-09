import random
import turtle as t

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_col = (r, g, b)
    return rand_col


timmy = t.Turtle()

#Draw a square
# for _ in range(0,4):
#     timmy.right(90)
#     timmy.forward(100)


#Draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#Drawing different shapes
# colors = ["red", "green", "blue", "pink", "violet"]
# shapes = [3, 4, 5, 6, 7, 8, 9, 10]
#
# colors = ["blue", "green", "red", "yellow", "violet"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Generate random walk
# direction = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fastest")
# for _ in range(100):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))



#Draw a spirograph
timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)


draw_spirograph(10)





screen = t.Screen()
screen.exitonclick()
