import turtle

def draw_square():
    '''
    Objective : To draw a square
    Input Parameters : None
    Output : The square is printed on screen
    '''

    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_square()
