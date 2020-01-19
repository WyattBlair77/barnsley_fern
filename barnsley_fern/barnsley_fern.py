import turtle
import random

pen = turtle.Turtle()
pen.speed(20)
pen.color('green')
pen.penup()

x = 0
y = 0

hyper_params = [0.16,
                0.85,
                0.04,
                0.04,
                0.85,
                1.6,
                0.20,
                0.26,
                0.23,
                0.22,
                1.6,
                0.15,
                0.28,
                0.26,
                0.24,
                0.44]

for n in range(100000):
    pen.goto(85*x, 57*y-275)  # 57 is to scale the fern and -275 is to start the drawing from the bottom.
    pen.pendown()
    pen.dot()
    pen.penup()
    r = random.random()  # to get probability
    r = r * 100
    xn = x
    yn = y
    if r < 1:  # elif ladder based on the probability
        x = 0
        y = hyper_params[0] * yn
    elif r < 86:
        x = hyper_params[1] * xn + hyper_params[2] * yn
        y = -hyper_params[3] * xn + hyper_params[4] * yn + hyper_params[5]
    elif r < 93:
        x = hyper_params[6] * xn - hyper_params[7] * yn
        y = hyper_params[8] * xn + hyper_params[9] * yn + hyper_params[10]
    else:
        x = -hyper_params[11] * xn + hyper_params[12] * yn
        y = hyper_params[13] * xn + hyper_params[14] * yn + hyper_params[15]

