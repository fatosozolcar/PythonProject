import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Shrinking Square")

turtle_instance = turtle.Turtle()
turtle_instance.color("pink")

turtle_instance.forward(100)
turtle_instance.left(90)

def shrinking_square(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size -= 5


shrinking_square(200)
shrinking_square(100)
shrinking_square(50)

turtle.done()
