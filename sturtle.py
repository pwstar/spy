import turtle
import sys

def forcircle(time,firstRadios,addRadiosEveryTimes) :
    turtle.circle(firstRadios, None, None)
    for i in range(time):
        firstRadios = firstRadios + addRadiosEveryTimes
        if i == time :
            sys.exit()
        turtle.circle(firstRadios, None, None)



