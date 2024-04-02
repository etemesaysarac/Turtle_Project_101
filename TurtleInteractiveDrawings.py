import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('light blue')
drawing_board.title('Interactive Drawing Board Project')

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() + 10)
 #   turtle_instance.right(100)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()-10)
 #   turtle_instance.left(100)

def clear_screen():
    turtle_instance.clear()

def turtle_instance_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
#To do process faster, we add some spesific rules while returning home!

# What if we don't want Turtle to draw while coming back home or like this...
def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key='space')
drawing_board.onkey(fun=rotate_angle_right,key='Up')
drawing_board.onkey(fun=rotate_angle_left,key='Down')
drawing_board.onkey(fun=clear_screen,key='c')
drawing_board.onkey(fun=turtle_instance_home,key='h')
drawing_board.onkey(fun=turtle_pen_down,key='d')
drawing_board.onkey(fun=turtle_pen_up,key='u')

turtle.mainloop()