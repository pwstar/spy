import turtle
import sys

def forcircle(time,FirstRadios,AddRadiosEveryTimes) :
    turtle.circle(FirstRadios, None, None)
    for i in range(time):
        FirstRadios = FirstRadios + AddRadiosEveryTimes
        if i == time :
            sys.exit()
        turtle.circle(FirstRadios, None, None)



