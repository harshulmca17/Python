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

    #changing the turtles attributes
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    #turtle movement
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    #creating second turtle - angie 
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.circle(100)
    

    window.exitonclick()

draw_square()
