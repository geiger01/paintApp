from turtle import Turtle, Screen

tantan = Turtle()
screen= Screen()

def move_foward():
    tantan.forward(20)

def move_backward():
    tantan.backward(20)



def turn_left():
    
    new_heading=tantan.heading()+20
    tantan.setheading(new_heading)
    

def turn_right():
    new_heading=tantan.heading()-20
    tantan.setheading(new_heading)

def clear():
    tantan.clear()


screen.listen()
screen.onkey(key="s", fun= move_backward)
screen.onkey(key="w", fun= move_foward)
screen.onkey(key="d", fun= turn_right)
screen.onkey(key="a", fun= turn_left)
screen.onkey(key="c", fun= clear)
screen.exitonclick()