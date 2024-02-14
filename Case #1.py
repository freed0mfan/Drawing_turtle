# Case-study #1
# Devrlopers: Sokolova S., Tomchuk N., Markelov E.


import turtle as t
import math as m

t.speed(100)

'''
> Each function draws pictures using library "turtle"

> Each function from #FIGURES draws a basic geometric
figure according to its name

> Each function from #PICTURES draws a combination 
of figures looks like object in its name
'''


# FIGURES
def prlgrm(x, y, length, height, acute_angle, color='BLACK', angle_round=0):
    '''
    :param x: bottom left corner coordinate x
    :param y: bottom left corner coordinate y
    :param length: side length of a parallelogram
    :param height: height of a parallelogram
    :param acute_angle: acute angle of a parallelogram
    :param color: color of a figure
    :param angle_round: angle of rotating a figure clockwise
    :return: None
    '''

    t.up()
    t.setposition(x, y)
    t.down()
    t.rt(angle_round)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.fd(length)
        t.lt(acute_angle)
        t.fd(height / (m.sin(acute_angle)))
        t.lt(180 - acute_angle)
    t.end_fill()
    t.seth(0)


def rhomb(x, y, side, acute_angle, color='BLACK', angle_round=0):
    '''
    :param x: bottom corner coordinate x
    :param y: bottom corner coordinate y
    :param side: side length of a rhombus
    :param acute_angle: acute angle of a rhombus
    :param color: color of a figure
    :param angle_round: angle of rotating a figure clockwise
    :return: None
    '''
    t.lt(90 - (acute_angle / 2))
    prlgrm(x, y, side, side * m.sin(acute_angle), acute_angle, color, angle_round)
    t.seth(0)


def rectangle(x, y, length, height, color='BLACK', angle_round=0):
    '''
    :param x: bottom left corner coordinate x
    :param y: bottom left corner coordinate y
    :param length: side length of a rectangle
    :param height: height of a rectangle
    :param color: color of a figure
    :param angle_round: angle of rotating a figure clockwise
    :return: None
    '''
    prlgrm(x, y, length, height, 90, color, angle_round)
    t.seth(0)


def equal_trapeze(x, y, base_down, base_up, height, color='BLACK', angle_round=0):
    '''
    :param x: bottom left corner coordinate x
    :param y: bottom left corner coordinate y
    :param base_down: lower base length of a trapeze
    :param base_up: upper base length of a trapeze
    :param height: height of a trapeze
    :param color: color of a figure
    :param angle_round:  angle of rotating a figure clockwise
    :return: None
    '''
    t.teleport(x, y)
    lt_rt_sides = m.sqrt(height ** 2 + ((base_down - base_up) / 2) ** 2)
    angle = m.degrees(m.asin(height / lt_rt_sides))
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.lt(angle - angle_round)
    t.fd(lt_rt_sides)
    t.rt(angle)
    t.fd(base_up)
    t.rt(angle)
    t.fd(lt_rt_sides)
    t.end_fill()
    t.seth(0)


def triangle_90(x, y, height, base, color='BLACK', angle_round=0):
    '''
    :param x: bottom left corner coordinate x
    :param y: bottom left corner coordinate y
    :param height: 1st leg of an orthogonal triangle
    :param base: 2nd leg of an orthogonal triangle
    :param color: color of a figure
    :param angle_round: angle of rotating a figure clockwise
    :return: None
    '''
    hypotenuse = m.sqrt(height ** 2 + base ** 2)
    angle = m.degrees(m.acos(height / hypotenuse))
    t.color(color)
    t.fillcolor(color)
    t.teleport(x, y)
    t.begin_fill()
    t.lt(90 - angle_round)
    t.fd(height)
    t.rt(180 - angle)
    t.fd(hypotenuse)
    t.end_fill()
    t.seth(0)


def square(x, y, a, color='RED', angle_round=0):
    '''
    :param x: bottom left corner coordinate x
    :param y: bottom left corner coordinate y
    :param a: side length of a square
    :param color: color of a figure
    :param angle_round: angle of rotating a figure clockwise
    :return: None
    '''
    t.teleport(x, y)
    t.color(color)
    t.fillcolor(color)
    t.rt(angle_round)
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.lt(90)
    t.end_fill()
    t.seth(0)


def circle(x, y, radius, color='RED'):
    '''
    :param x: the lowest point of a circle coordinate x
    :param y: the lowest point of a circle coordinate y
    :param radius: radius of a circle
    :param color: color of a figure
    :return: None
    '''
    t.teleport(x, y)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.seth(0)


# PICTURES
def rocket():
    rectangle(-500, -200, 50, 90, '#483D8B')
    circle(-475, -147, 17, '#ADD8E6')
    circle(-475, -197, 17, '#ADD8E6')
    triangle_90(-475, -100, 75, 26, '#800000')
    triangle_90(-475, -100, 26, 75, '#800000', -90)
    triangle_90(-475, -100, 75, 15, '#FF0000')
    triangle_90(-475, -100, 15, 75, '#FF0000', -90)
    prlgrm(-450, -175, 50, 33, 45, '#808080', 90)
    prlgrm(-525, -200, -50, -33, -45, '#808080', -90)


def dog():
    prlgrm(-200, -150, 75, 50, 64, '#A0522D')
    triangle_90(-100, -200, 25, 50, 'BLACK', -90)
    triangle_90(-100, -150, 28, 53, '#8B4513', -90)
    triangle_90(-100, -150, -28, -53, '#8B4513', 90)
    triangle_90(-175, -100, m.sqrt(100 * 100 + 50 * 50), m.sqrt(25 * 25 + 50 * 50), '#8B4513', -(180 - 90 + 64))
    triangle_90(-225, -200, 25, 25, 'BLACK', -90)
    square(-237.5, -75, 35, '#A0522D')
    triangle_90(-237.5, -50, 50, 25, '#8B4513')
    triangle_90(-237.5, -50, 45, 20, '#BC8F8F')
    rectangle(-280, -66, 280 - 237.5, 20, '#8B4513')
    triangle_90(-280, -43, 25, 25, 'BLACK', -180)
    triangle_90(-100, -50, 50, 50, '#A0522D', 90)


def carpenter():
    square(-150, -350, 50, '#228B22')
    triangle_90(-150, -300, 50, 25, '#006400', -180)
    triangle_90(-250, -400, 50, 25, '#006400')
    triangle_90(-350, -400, 25, 50, '#006400', -90)
    triangle_90(-450, -300, 25, 50, '#006400', 90)
    rectangle(-225, -400, m.sqrt(50 * 50 + 75 * 75), m.sqrt(50 * 50 + 25 * 25), '#228B22', 64 - 90)
    rectangle(-350, -400, 100, 50, '#228B22')
    rectangle(-450, -350, m.sqrt(50 * 50 + 75 * 75), m.sqrt(50 * 50 + 25 * 25), '#228B22', 90 - 64)
    rectangle(-550, -350, 100, 50, '#228B22')
    triangle_90(-590, -325, m.sqrt(25 * 25 + 50 * 50), m.sqrt(25 * 25 + 50 * 50), '#006400', 45)


def heart(x, y, k=1):
    triangle_90(x, y + 2 * k, 2 * k, 2 * k, 'RED', 90)
    triangle_90(x, y + 2 * k, 2 * k, 2 * k, 'RED', 180)
    square(x - 2 * k, y + 2 * k, 2 * k, 'RED')
    square(x, y + 2 * k, 2 * k, 'RED')
    triangle_90(x - 2 * k, y + 3 * k, k, k, 'RED', 180)
    triangle_90(x + 2 * k, y + 3 * k, k, k, 'RED', 90)
    square(x - 3 * k, y + 3 * k, k, 'RED')
    square(x + 2 * k, y + 3 * k, k, 'RED')
    equal_trapeze(x - 3 * k, y + 4 * k, 3 * k, k, k, 'RED')
    equal_trapeze(x, y + 4 * k, 3 * k, k, k, 'RED')


def fish(x, y, k=1):
    triangle_90(x, y + k, k, k, 'TURQUOISE', 90)
    equal_trapeze(x - k, y + 2 * k, 3 * k, k, k, 'AQUAMARINE')
    equal_trapeze(x + 2 * k, y + 2 * k, 3 * k, k, k, 'AQUAMARINE', 180)
    triangle_90(x, y + 3 * k, k, k, 'TURQUOISE')
    triangle_90(x - k, y + 2 * k, k * m.sqrt(2), k * m.sqrt(2), 'TURQUOISE', 225)


def tree(x, y, k=1):
    square(x, y, k, 'BROWN')
    equal_trapeze(x - k, y + k, 3 * k, 1.5 * k, 1.25 * k, 'GREEN')
    equal_trapeze(x - 0.75 * k, y + 2 * k, 2.5 * k, k, 1.25 * k, 'GREEN')
    triangle_90(x + 0.5 * k, y + 3 * k, 1.25 * k, 0.85 * k, 'GREEN')
    triangle_90(x + 0.5 * k, y + 3 * k, 0.85 * k, 1.25 * k, 'GREEN', 270)


def car(x, y, k=1):
    rectangle(x, y, 13 * k, 2 * k, color='LAVENDER')
    equal_trapeze(x + 2 * k, y + 2 * k, 9 * k, 5 * k, 2 * k, color='#FEFBEA')
    circle(x + 2 * k, y - k, radius=k, color='BLACK')
    circle(x + 11 * k, y - k, radius=k, color='BLACK')


def home(x, y, k=1):
    square(x, y, 4 * k, color='BLUE')
    circle(x + k, y + 2.5 * k, radius=0.5 * k, color='WHITE')
    rectangle(x + 2 * k, y, k, 2 * k, color='BROWN')
    triangle_90(x + 2 * k, y + 7 * k, k * m.sqrt(18), k * m.sqrt(18), color='GREEN', angle_round=135)


def wheelchair(x, y, k=1):
    rectangle(x, y, 8 * k, 2 * k, color='PINK')
    square(x + 2 * k, y + 2 * k, 2 * k, color='#C6A1CF')
    triangle_90(x + 2 * k, y + 2 * k, 2 * k, 2 * k, color='#C6A1CF', angle_round=270)
    circle(x + 2 * k, y - 2 * k, radius=k, color='BLACK')
    circle(x + 6 * k, y - 2 * k, radius=k, color='BLACK')


carpenter()
dog()
rocket()
heart(0, 50, 20)
fish(200, 50, 30)
tree(-200, 50, 30)
car(300, -200, 30)
home(100, -200, 20)
wheelchair(0, -300, 20)

t.up()
t.setposition(0, 0)
t.done()
