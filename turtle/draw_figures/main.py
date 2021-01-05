from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()


def move_forwards():
    tur.forward(10)


def move_backwards():
    tur.backward(10)


def turn_left():
    tur.left(10)


def turn_right():
    tur.right(-10)


def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
