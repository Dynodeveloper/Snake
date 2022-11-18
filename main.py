from turtle import Screen #importa libreria grafica
from snake import Snake #del archivo snake importa la clase Snake 
from food import Food # de el archivo food importa la clase Food
from scoreboard import Scoreboard #
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("darkgrey")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() #especifica el numero de conexiones no aceptadas que el sistema permitirá ants de rechazar nuevas conexiones
screen.onkey(snake.up, "Up") #vincula el evento a realizar con la tecla especificada 
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        
screen.exitonclick()
