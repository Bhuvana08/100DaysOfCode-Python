# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r,g,b)
#     colors_list.append(new_color)
# print(colors_list)

import turtle as t
import random
t.colormode(255)

colors_list = [(239, 233, 236), (199, 162, 97), (155, 61, 74), (162, 70, 54), (132, 162, 188), (222, 206, 123), (210, 85, 59), (198, 139, 160), (64, 37, 52), (43, 38, 62), (56, 50, 101), (69, 84, 140), (193, 83, 121), (134, 177, 159), (77, 125, 98), (84, 152, 115), (156, 169, 72), (111, 43, 50), (107, 45, 39), (78, 54, 40), (220, 174, 185), (99, 106, 166), (229, 175, 165), (160, 199, 216), (181, 187, 215), (169, 203, 193), (87, 148, 153)]


def random_color():
    return random.choice(colors_list)


timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random_color())
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()
