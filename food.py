from turtle import Turtle #se importa la libreria turrtle para realizar graficos
import random #se importa random para la aparicion aleatoria de la comida


class Food(Turtle): #se crea la clase Food con el atributo Turtle

    def __init__(self): #se define funcion 
        super().__init__() 
        self.shape("turtle") #define la forma del objeto
        self.penup() #elimina el trazo de la animacion o movimiento
        self.shapesize(stretch_len=1,stretch_wid=1) #define el tamaño de el objeto
        self.color("white") #define el color 
        self.speed("fastest") #define la velocidad de aparicion
        self.refresh() #llama el metodo refresh para la reparicion


    def refresh(self): #define la funcion refresh para la aparicion del objeto
        random_x = random.randint(-280, 280) #define limites en eje x para la reaparicion
        random_y = random.randint(-280, 280) #define limites en eje y para la reaparicion
        self.goto(random_x, random_y) #llama el metodo goto con los limites previamente establecidos
