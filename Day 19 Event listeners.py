from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
scree.exitonclick()

#keyword Arguments
def my_function(a,b,c):
    #do this with a
    #then do this with b
    #finally do this with c
    my_function(1,2,3)

#positional Arguments
def my_function(a, b, c):
    # do this with a
    # then do this with b
    # finally do this with c
    my_function(c=3, a=1, b=2)

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backrwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()