from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race?: ")
COLORS = ["red","green","white","indigo","orange","brown","blue"]
POSITIONS = [-70, -40, -10, 20, 50, 80, 110]

race_on = False
all_turtles = []

for t in range(0,7):
    turtle_index = Turtle()
    turtle_index.shape("turtle")
    turtle_index.penup()
    turtle_index.goto(x=-230, y=POSITIONS[t])
    turtle_index.color(COLORS[t])
    all_turtles.append(turtle_index)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        distance_rand = random.randint(0,10)
        turtle.forward(distance_rand)







screen.exitonclick()