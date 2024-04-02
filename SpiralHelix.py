import turtle

turtle_screen = turtle.Screen()
turtle_screen = turtle.bgcolor('Light green')


turtle_instance = turtle.Turtle()
turtle_instance.color('blue')

for i in range(10):
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)


turtle.done()
