import turtle
import time

screen = turtle.Screen()
screen.setup(600,600)
t = turtle.Turtle('turtle')
t.speed(3)
time = time.time()

def prawy():
    t.setheading(0)
    t.fd(50)

def lewo():
    t.setheading(180)
    t.fd(50)

def gora():
    t.setheading(90)
    t.fd(50)

def dol():
    t.setheading(270)
    t.fd(50)

def spac(x):
    print(round(time.time()-x,2))


turtle.listen()

turtle.onkey(prawy, 'Right')
turtle.onkey(lewo, 'Left')
turtle.onkey(gora, 'Up')
turtle.onkey(dol, 'Down')
turtle.onkeypress(spac, 'space')

turtle.mainloop()