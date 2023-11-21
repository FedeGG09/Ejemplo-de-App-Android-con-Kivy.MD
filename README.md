# Ejemplo-de-App-Android-con-Kivy.MD
Códigos y descripción para armar un juego sencillo y funcional para Android con Python


Propuesta de aplicación:
“"Spanglish”
Curso: Python Intermedio Para Desarrollo De Aplicaciones 
Federico Guillermo Gravina y Fanny Eugenia Sánchez Caballero
gravinadavilafederico@gmail.com

fannyfitz8@gmail.com 

Visión general
"Spanglish es una aplicación educativa y entretenida, diseñada para ayudar a niños y niñas a mejorar sus habilidades de comprensión de imágenes, conceptos y escritura  de forma pedagógica.

Objetivos
El objetivo general de la aplicación es proporcionar a los usuarios una plataforma interactiva y entretenida que les permita mejorar sus habilidades.



Solución Propuesta
Acá añadir una descripción general de la solución propuesta (lenguaje de programación y frameworks utilizados, entorno de desarrollo, etc.)

Pantalla de Inicio (Main Screen):
Implementación de la interfaz gráﬁca: Se importan las bibliotecas necesarias, kivymd, kivy, random, y se definen las clases como WelcomeScreen, GameScreen, EndScreen, CustomResponsiveLayout, MobileView, TabletView, DesktopView y MyApp.
Definición de CustomResponsiveLayout:
Se crea una clase llamada CustomResponsiveLayout, que es una caja de diseño que cambia su contenido según el tamaño de la ventana de la aplicación. Contiene tres vistas: MobileView, TabletView y DesktopView. Las vistas se utilizan para mostrar diferentes elementos según el tamaño de la pantalla.
Definición de las vistas MobileView, TabletView y DesktopView:
Cada vista contiene una etiqueta y un botón, y se muestran o se ocultan según la vista actual seleccionada en CustomResponsiveLayout.
Descripción de la lógica del programa implementado
Clase MyApp y el método build:

MyApp es la clase principal de la aplicación y contiene la lógica principal.
El método build se encarga de construir la interfaz gráfica de la aplicación y configurar las pantallas.
Dentro de build, se configura el tema de la aplicación y se crea un ScreenManager para gestionar las pantallas.
Las pantallas, como WelcomeScreen, GameScreen y EndScreen, se agregan al ScreenManager para su posterior uso.
Método start_game:
Se llama cuando el jugador elige una dificultad en la pantalla de bienvenida.
Inicializa las variables del juego, como el nombre del jugador, la puntuación, la dificultad y el nivel actual.
Llama al método load_words_for_difficulty para cargar palabras basadas en la dificultad seleccionada.
Llama al método load_next_question para mostrar la primera pregunta en la pantalla de juego.
Método load_words_for_difficulty:
Carga palabras y sus traducciones en función de la dificultad seleccionada (fácil, medio o difícil).
Las palabras y sus imágenes se almacenan en la lista words_and_images.
Método load_next_question:
Carga la siguiente pregunta en la pantalla de juego.
Muestra una imagen y una traducción en la pantalla.
Configura un límite de tiempo para responder a la pregunta.
Métodos update_time_label y update_time:
Actualizan la etiqueta que muestra el tiempo restante en la pantalla de juego.
update_time disminuye el tiempo restante en cada segundo y llama a check_answer cuando se agota el tiempo.
Método check_answer:
Verifica la respuesta proporcionada por el jugador en la pantalla de juego.
Compara la respuesta con la traducción esperada.
Muestra un mensaje de retroalimentación ("¡Correcto!" o "¡Incorrecto!") en la pantalla.
Aumenta la puntuación si la respuesta es correcta.
Controla los intentos restantes y llama a game_over si se agotan.
Método game_over:
Muestra la pantalla de finalización del juego cuando se quedan sin intentos.
Muestra la puntuación del jugador en la pantalla final.
Método exit_app:
Sale de la aplicación cuando se presiona el botón "Salir" en la pantalla de finalización del juego.
Método restart_game:
Reinicia el juego al estado inicial, permitiendo al jugador seleccionar una nueva dificultad.
Restablece los intentos, el nombre del jugador y la puntuación.
Llama a load_words_for_difficulty para cargar nuevas palabras según la dificultad actual.
Definición de EndScreen:
EndScreen es una instancia de la clase Screen de KivyMD.
Se utiliza para mostrar información relacionada con el final del juego, como la puntuación del jugador y proporciona opciones para reiniciar el juego o salir de la aplicación.
Contenido de EndScreen:
La pantalla EndScreen contiene varios elementos visuales, como etiquetas (MDLabel) y botones (MDFillRoundFlatButton), que se utilizan para mostrar información relevante al jugador.
Elementos en EndScreen:
MDLabel para mostrar el título "Juego Terminado", que informa al jugador que el juego ha concluido.
MDLabel para mostrar la puntuación del jugador en la forma "Puntuación [nombre del jugador]: [puntuación]". El nombre del jugador se obtiene de la entrada del jugador al principio del juego.
Dos botones:
"Volver a Jugar" (MDFillRoundFlatButton): Al hacer clic en este botón, se llama al método restart_game, que reinicia el juego permitiendo al jugador seleccionar una nueva dificultad y restableciendo las variables del juego.
"Salir" (MDFillRoundFlatButton): Al hacer clic en este botón, se llama al método exit_app, que cierra la aplicación.

Cabe destacar, además, que se priorizó el desarrollo del aspecto funcional de la aplicación y no así su estética. 
