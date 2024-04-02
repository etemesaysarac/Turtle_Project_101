import turtle

turtle_screen = turtle.Screen()
turtle_screen = turtle.bgcolor('Light green')
turtle.speed(0) #fastest=0

turtle_instance = turtle.Turtle()
turtle_instance.color('blue')
turtle_colors = ['red', 'blue', 'orange', 'yellow', 'purple', 'green']

for i in range(5):
    turtle_instance.color(turtle_colors [i % 6])
    turtle_instance.pencolor(turtle_colors [i % 3])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)

turtle.mainloop()
#turtle.done()
