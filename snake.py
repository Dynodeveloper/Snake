from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)] #define la posicion inicial de la serpiente
MOVE_DISTANCE = 20 #define la distancia recorrida
UP = 90 #define los grados que gira hacia esa posicion
DOWN = 270 #define los grados que gira hacia esa posicion
LEFT = 180 #define los grados que gira hacia esa posicion
RIGHT = 0 #define los grados que gira hacia esa posicion

class Snake: #crea la clase de la serpiente

    def add_segment(self, position): #define la funcion de agregar segementos (crea la serpiente)
        new_segment = Turtle("circle") #define la forma de cada segmento
        new_segment.color("black") #define el color de cada segmento
        new_segment.penup() #elim ina el trazo de movimiento
        new_segment.goto(position) #define la posicion hacia la que se mueve la serpiente
        self.segments.append(new_segment) #agrega el metodo de agrwegar segmentos y crear una sola serpiente

    def create_snake(self): #define la funcion de creacion de serpiente
        for position in STARTING_POSITIONS:
            self.add_segment(position) #define el metodo para gregar segmentos a la serpiente

    def __init__(self): #define lafuncion de si misma
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]





    def extend(self):
        self.add_segment(self.segments[-1].position()) #define la funcion para alargar la serpiente

    def move(self): #define la funcion de movimiento
        for seg_num in range(len(self.segments)- 1, 0, -1):

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)