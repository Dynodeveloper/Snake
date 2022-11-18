from turtle import Screen #importa libreria grafica
from snake import Snake #del archivo snake importa la clase Snake 
from food import Food # de el archivo food importa la clase Food
from scoreboard import Scoreboard #del archivo scoreboad se importa la clase Scoreboard
import time #da el tiempo real de una accion 

screen = Screen() #se llama la screen y se le asignan parametros
screen.setup(width=600, height=600) #se modifica el tamaño de la pantalla
screen.bgcolor("darkgrey") #se define el color de fondo 
screen.title("My Snake Game") #se define el titulo de la ventana
screen.tracer(0) #reconoce las animaciones de turtle

#se le asigna nombre a cada clase importada
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() #especifica el numero de conexiones no aceptadas que el sistema permitirá ants de rechazar nuevas conexiones
screen.onkey(snake.up, "Up") #vincula el evento a realizar con la tecla especificada 
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True #se crea igualdad 
while game_is_on: #se crea el while que da inicio al juego
    screen.update()#inserta los elementos del diccionario, da camino a el inicio de animaciones
    time.sleep(0.2) #velocidad del objeto
    snake.move() #mueve un archivo de directorio

    # Detectar colision con comida
    if snake.head.distance(food) < 15: #ciclo para reconocer el choque
            food.refresh() #llama la funcion refresh de food
            snake.extend() #llama la funcion extend de snake
            scoreboard.increase_score() #llama la funcion increase de scoreboard

    # Detectar colision con bordes.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor() < -290: #ciclo para reconocer el choque
        game_is_on = False #accion a realizar (finalizar juego)
        scoreboard.game_over()#llama la funcion game_over de scoreboard

    # Detecta colision consigo misma.
    for segment in snake.segments: #para cada segmento en la serpiente haga
        if segment == snake.head: #confirmacion para saber si la cabeza de la serpiente se encuentra con un segemento de la misma
            pass #de lo contrario continue
        elif snake.head.distance(segment) < 10: #si la distancia entre la cabeza de la serpiente y un segmento de la misma es menor a 10 haga
            game_is_on = False #finalizacion del juego
            scoreboard.game_over()
        
screen.exitonclick() #en escreen se llama la funcion predefinda exitonclick
