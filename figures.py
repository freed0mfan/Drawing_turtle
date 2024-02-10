import turtle as t
import math

def prlgrm(x, y, length, height, acute_angle, color='BLACK', angle_round=0):
    t.up()
    t.setposition(x, y)
    t.down()
    t.color(color)
    t.fillcolor(color)
    t.lt(angle_round)
    t.begin_fill()
    for i in range(2):
        t.fd(length)
        t.lt(acute_angle)
        t.back(height / (math.sin(acute_angle)))
        t.lt(180 - acute_angle)
    t.end_fill()

def rhomb(x, y, side, acute_angle, color='BLACK', angle_round=0):
    t.lt(90 - (acute_angle / 2))
    prlgrm(x, y, side, side * math.sin(acute_angle), acute_angle, color, angle_round)
def rectangle(x, y, length, height, color='BLACK', angle_round=0):
    t.lt(90)
    prlgrm(x, y, height, length, 90, color, angle_round)
    t.rt(90)


t.done()