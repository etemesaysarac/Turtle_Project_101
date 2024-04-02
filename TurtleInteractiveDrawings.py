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
    turtle_instance.home()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key='space')
drawing_board.onkey(fun=rotate_angle_right,key='Up')
drawing_board.onkey(fun=rotate_angle_left,key='Down')
drawing_board.onkey(fun=clear_screen,key='c')
drawing_board.onkey(fun=turtle_instance_home,key='h')

turtle.mainloop()