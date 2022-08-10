import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1000, height=600)
is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
sprinters = []

x = -480
y = -150

for _ in range(6):
    cursor = Turtle()
    cursor.shape("turtle")
    color = random.choice(colors)
    cursor.color(f"{color}")
    colors.remove(color)
    cursor.penup()
    cursor.goto(x, y)
    cursor.pendown()
    y += 65
    sprinters.append(cursor)

user_bet = screen.textinput(title="Make your bet", prompt="Who do you think will win the turtle race?").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in sprinters:
        if turtles.xcor() > 460:
            is_race_on = False
            winner = turtles.pencolor()
            if winner == user_bet:
                print(f"You win!!, {winner} is the winner")
            else:
                print(f"You lost!, {winner} is the winner")
        turtles.penup()
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

# screen.exitonclick()
