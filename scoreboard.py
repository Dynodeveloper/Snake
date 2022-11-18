from turtle import Turtle  
ALIGNMENT = "center"
FONT = ("Comic sans", 22, "italic")

class Scoreboard(Turtle): #se crea la clase con el atributo turtle

    def __init__(self): # se define la funcion de la misma clase
        super().__init__()
        self.score = 0 #define el marcador inicial como cero 
        self.color("black") #se define el color del marcador
        self.penup() #elimina el trazo 
        self.goto(0, 270) #define lugar de aparicion 
        self.hideturtle() #esconde el objeto
        self.update_scoreboard() #se actualiza el marcador

    def update_scoreboard(self): #define funcion de el marcador
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT) #escribe el marcador

    def game_over(self): #define la funcion del juego terminado
        self.goto(0, 0) #define la ubicacion 
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)# escribe Game over con los parametros de alineacion de fuente

    def increase_score(self): #define la funcion de aumento en el marcador 
        self.score+= 1 #define la operacion de suma
        self.clear()#llama el metodo clear para limpiar el anterior puntaje
        self.update_scoreboard() #actualiza el marcador 