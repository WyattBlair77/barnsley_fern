'''
This is a script to construct the Barnsley fern, a fractal discovered by mathematician Michael Barnsley.
Due to its 'flexible' nature, in that by changing the hyper-parameters you can construct different ferns,
the structure is classified as a super-fractal!

The script works by iteratively applying one of four linear functions, weighted randomly, to an initial starting position:
pos = [x_n,y_n].

Function X is applied with probability p = hp['p'][X], and if we let a = hp['a'][X], b = hp['b][X]... etc.,
it looks like [[a,b],[c,d]].[x_n,y_n] + [e,f] = [x_n+1, y_n+1]

Function 0 (hp[x][0]): the stem
Function 1 (hp[x][1]): successively smaller leaflets
Function 2 (hp[x][2]): largest left hand leaflet
Function 3 (hp[x][3]): largest right hand leaflet

Disclaimer: My code was heavily influenced by the code on the Wikipedia page regarding this subject
'''

# imports
import numpy as np
import turtle
import random

pen = turtle.Turtle()
pen.speed(10000)
pen.color('green')
pen.penup()

# initial pos
x = 0
y = 0

pos = np.array([x, y])

# hyper-params
barnsley = {
    'a': [0, 0.85, 0.20, -0.15],
    'b': [0, 0.04, -0.26, 0.28],
    'c': [0, -0.04, 0.23, 0.26],
    'd': [0.16, 0.85, 0.22, 0.24],

    'e': [0, 0, 0, 0],
    'f': [0, 1.60, 1.60, 0.44],

    'p': [0.01, 0.85, 0.07, 0.07]}

mutant1 = {
    'a': [0, 0.95, 0.035, -0.04],
    'b': [0, 0.005, -0.2, 0.2],
    'c': [0, -0.005, 0.16, 0.16],
    'd': [0.25, 0.93, 0.04, 0.04],

    'e': [0, -0.002, -0.09, 0.083],
    'f': [-0.4, 0.5, 0.02, 0.12],

    'p': [0.02, 0.84, 0.07, 0.07]}

fern_choices = [barnsley, mutant1]

hp = fern_choices[1]
iterations = 100000

seed_list = []
for i, count in zip(range(len(hp['p'])), ['0', '1', '2', '3']):
    seed_list += (int(hp['p'][i] * 100) * [count])

for i in range(iterations):
    # actually draw things
    pen.goto(85 * pos[0], 57 * pos[1] - 275)  # 57 is to scale the fern and -275 is to start the drawing from the bottom.
    pen.pendown()
    pen.dot()
    pen.penup()

    # initialize transformation and offset_vector

    seed = random.choice(seed_list)
    transformation = np.array([[hp['a'][int(seed)], hp['b'][int(seed)]], [hp['c'][int(seed)], hp['d'][int(seed)]]])
    offset_vector = np.array([hp['e'][int(seed)], hp['f'][int(seed)]])

    # apply iteration
    pos = np.matmul(transformation, pos)
    pos += offset_vector

