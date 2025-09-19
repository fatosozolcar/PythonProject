import turtle


drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Python Turtle")
#Square

'''
turtle_instance_3 = turtle.Turtle()
a=turtle_instance_3.forward(100)
b=turtle_instance_3.left(90)
c=turtle_instance_3.forward(100)
d=turtle_instance_3.left(90)
e=turtle_instance_3.forward(100)
f=turtle_instance_3.left(90)
g=turtle_instance_3.forward(100)
'''

turtle_instance_4 = turtle.Turtle()

for i in range(4):
    turtle_instance_4.forward(100)
    turtle_instance_4.left(90)



turtle.done()