<center> <h1>JUEGO SNAKE</h1> </center>

<img src="https://miro.medium.com/max/1400/1*spTwLANfg8qPWZ0-5bt1pQ.png">

<hr>
<h2>EXPLICACON DE PROYECTO</h2>

<P>El videougo <b>"SNAKE"</b> fue desarrollado en 1976 por gremlin nokia para sus dispositivos android, esta vez replicaremos dicho juego en el lenguaje python</P>

<h2>Creacion del proyecto</h2>

<p>Para la creacion de este proyecto iniciaremos por crear una carpeta madre llamada "SNAKE" en la cual encontraremos los codigos funcionales, un readme y una carpeta con imagenes</p>

<img src="img/folders.PNG">

<h3>Archivos</h3>
<li>main.py
<li>food.py
<li>scoreboard.py
<li>snake.py

<hr>

<h2>Main.py</h2>

<p>En este archivo se inicializaran las tareas principales, será la cabeza principal del juego, donde estará la logica del mismo y su interfaz, iniciamos con unas importaciones</p>

<img src="img/imp.PNG">

<ol>
<li><p>En primer lugar tenemos turtle como libreria, esto nos permite crear la pantala en la que se observarán los sucesos, lo que viene siendo la interfaz</p>
<li><p>Los siguientes dos imports se importa las clases correspondientes( Snake,Food,Scoreboard ) de los archivos correspondientes <p>
<li><p>Por ultimo se importa la libreria time permite reconocer el tiempo real desde el inicio hasta el final del juego

<h3>Ventana

<img src="img/Screen.PNG">

<p> En esta seccion se definen los parametros de la interfaz o pantalla principal

<h3>Funcion Principal

<p>En esta seccion se definen todas las funciones basicas para el correcto desempeño del programa

<img src="img/funcionM.PNG">

<hr>

<h2> Food.py

<p> en ete archivo se definiran los atributos o funciones referentes a la comida de la serpiente, para esto al igual que en el anterior se debn de importar archivos

<br>

<img src="img/foodimp.PNG">

<p> en primer lugar se immporta Turtle para el grafico de la comida y luego se importa random para la aparicion aleatoria de la comida

<H3>Clase y atributos

<img src="img/class_food.PNG">

<p> se definen los atributos de la comida en si misma como su reaparicion , forma, color, entre otros

<h2>Scoreboard.py

<p> en este archivo se define la funcionalidad de el marcador y su apariencia, en este caso solo se importa turtle para su aparicion grafica

<h3>Formato

<p> se define la ubicacion del objeto o programa y su fuente 

<img src="img/font.PNG">


<h3> Funcionalidad

<img src="img/class_score.PNG">

<p>Se deinen los parametros de la clase marcador y se crean las funciones necesarias para su correcto funcionamiento 

<hr>

<H2>Snake.py

<p> En este archivo se define todo lo relacionado con la serpiente en si misma, su forma, color y lo mas importante, su movimiento, de igual forma a lo anterior se importa turtle para generar los graficos

<h3> Variables

<img src="img/snake.PNG">

<p>Define lo necesario para el movimiento de la serpiente

<h3> Clase y movimiento

<p> en esta parte del codigo se define las funciones con condiciones al igual que las funciones de extender al momento de entrar en contacto con la comida, es la parte esencial del juego

<img src="img/snake_class.PNG">

<p> con esto finalizado el juego funciona correctamente.


