import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('green')
drawing_board.title('Python Turtle')

turtle_instance = turtle.Turtle()
#polygon
num_sides = 6
angle = 360.0 / num_sides
side_lenght = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_lenght)

turtle.done()