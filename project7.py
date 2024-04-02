import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor('Light Green')
turtle_screen.title('Python Shrinking Applications')

turtle_instance = turtle.Turtle()
turtle_instance.color('blue')

def ShrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

ShrinkingSquare(200)
ShrinkingSquare(170)
ShrinkingSquare(140)
ShrinkingSquare(110)
ShrinkingSquare(90)
ShrinkingSquare(65)
ShrinkingSquare(40)
ShrinkingSquare(20)

turtle.done()