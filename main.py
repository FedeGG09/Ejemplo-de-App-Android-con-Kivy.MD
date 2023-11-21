from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty
import random

class WelcomeScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class EndScreen(Screen):
    pass

class CustomResponsiveLayout(BoxLayout):
    current_screen = StringProperty("")

    def __init__(self, **kwargs):
        super(CustomResponsiveLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()
        self.add_widget(self.mobile_view)
        self.add_widget(self.tablet_view)
        self.add_widget(self.desktop_view)

    def on_size(self, instance, value):
        
        if self.width < 768:
            self.current_screen = "mobile"
        elif self.width < 1024:
            self.current_screen = "tablet"
        else:
            self.current_screen = "desktop"
        
        self.switch_view()

    def switch_view(self):
        
        if self.current_screen == "mobile":
            self.mobile_view.visible = True
            self.tablet_view.visible = False
            self.desktop_view.visible = False
        elif self.current_screen == "tablet":
            self.mobile_view.visible = False
            self.tablet_view.visible = True
            self.desktop_view.visible = False
        else:
            self.mobile_view.visible = False
            self.tablet_view.visible = False
            self.desktop_view.visible = True

class MobileView(BoxLayout):
    visible = ListProperty([True, False, False])

    def __init__(self, **kwargs):
        super(MobileView, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Mobile View"))
        self.add_widget(Button(text="Mobile Button"))

class TabletView(BoxLayout):
    visible = ListProperty([False, True, False])

    def __init__(self, **kwargs):
        super(TabletView, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Tablet View"))
        self.add_widget(Button(text="Tablet Button"))

class DesktopView(BoxLayout):
    visible = ListProperty([False, False, True])

    def __init__(self, **kwargs):
        super(DesktopView, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Desktop View"))
        self.add_widget(Button(text="Desktop Button"))

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_name = ""  
        self.score = 0  
        self.time_limits = {
            "easy": 30,
            "medium": 20,
            "hard": 15
        }
        self.remaining_attempts = 5  

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.screen_manager = ScreenManager()

      
        welcome_screen = WelcomeScreen(name="welcome")
        welcome_label = MDLabel(text="Bienvenido al juego de aprendizaje de inglés", halign="center", font_style="H2")
        welcome_name = MDTextField(hint_text="Nombre", size_hint=(0.8, None), height="48dp")
        easy_button = MDFillRoundFlatButton(text="Fácil", pos_hint={"center_x": 0.3, "center_y": 0.2}, on_release=lambda x: self.start_game("easy"))
        medium_button = MDFillRoundFlatButton(text="Medio", pos_hint={"center_x": 0.5, "center_y": 0.2}, on_release=lambda x: self.start_game("medium"))
        hard_button = MDFillRoundFlatButton(text="Difícil", pos_hint={"center_x": 0.7, "center_y": 0.2}, on_release=lambda x: self.start_game("hard"))
        welcome_screen.add_widget(welcome_label)
        welcome_screen.add_widget(welcome_name)
        welcome_screen.add_widget(easy_button)
        welcome_screen.add_widget(medium_button)
        welcome_screen.add_widget(hard_button)

   
        game_screen = GameScreen(name="game")
        self.game_image = Image(source="", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.7})
        game_textfield = MDTextField(hint_text="Escribe aquí", size_hint=(0.8, None), height="48dp", pos_hint={"center_x": 0.5, "center_y": 0.4})
        self.time_label = MDLabel(text="", halign="center", font_style="H2")
        next_button = MDFillRoundFlatButton(text="Siguiente", pos_hint={"center_x": 0.5, "center_y": 0.2}, on_release=self.check_answer)
        game_feedback = MDLabel(text="", halign="center", font_style="H2")
        game_screen.add_widget(self.game_image)
        game_screen.add_widget(game_textfield)
        game_screen.add_widget(self.time_label)
        game_screen.add_widget(next_button)
        game_screen.add_widget(game_feedback)

      
        end_screen = EndScreen(name="end")
        end_label = MDLabel(text="Juego Terminado", halign="center", font_style="H2")
        end_score = MDLabel(text=f"Puntuación {self.player_name}: {self.score}", halign="center", valign="top")

      
        restart_button = MDFillRoundFlatButton(text="Volver a Jugar", pos_hint={"center_x": 0.3, "center_y": 0.3}, on_release=lambda x: self.restart_game())

  
        exit_button = MDFillRoundFlatButton(text="Salir", pos_hint={"center_x": 0.7, "center_y": 0.3}, on_release=self.exit_app)

        end_screen.add_widget(end_label)
        end_screen.add_widget(end_score)
        end_screen.add_widget(restart_button)
        end_screen.add_widget(exit_button)

        self.screen_manager.add_widget(welcome_screen)
        self.screen_manager.add_widget(game_screen)
        self.screen_manager.add_widget(end_screen)

        return self.screen_manager

    def start_game(self, difficulty):
        self.player_name = self.screen_manager.get_screen("welcome").children[1].text
        self.current_level = 0
        self.score = 0
        self.current_difficulty = difficulty

        
        self.load_words_for_difficulty(difficulty)

        self.load_next_question()
        self.screen_manager.current = "game"

    def load_words_for_difficulty(self, difficulty):
        if difficulty == "easy":
            words = [
                ("apple", "manzana", "manzana.jpg"),
                ("dog", "perro", "perro.png"),
                ("cat", "gato", "gato.png"),
                ("ball", "pelota", "pelota.jpg"),
                ("book", "libro", "libro.png"),
                ("house", "casa", "casa.jpg"),
                ("sun", "sol", "sol.jpg"),
                ("flower", "flor", "flor.jpg"),
                ("car", "coche", "coche.jpg"),
                ("clock", "reloj", "reloj.jpg"),
                ("moon", "luna", "luna.jpg"),
                ("tree", "árbol", "arbol.jpg"),
                ("fish", "pez", "pez.jpg"),
                ("star", "estrella", "estrella.jpg"),
                               
            ]
        elif difficulty == "medium":
            words = [
                ("computer", "computadora", "computadora.jpg"),
                ("mountain", "montaña", "montaña.jpg"),
                ("bicycle", "bicicleta", "bicicleta.jpg"),
                ("bird", "pájaro", "pajaro.jpg"),
                ("strawberry", "frutilla", "frutilla.jpg"),
                ("tshirt", "remera", "remera.jpg"),
                ("elephant", "elefante", "elefante.jpg"),
                ("guitar", "guitarra", "guitarra.jpg"),
                ("island", "isla", "isla.jpg"),
                ("jacket", "chaqueta", "campera.jpg"),
                ("kite", "cometa", "kite.jpg"),
                ("lollipop", "chupetín", "chupetín.jpg"),
                ("drum", "bateria", "bateria.jpg"),
                ("octopus", "pulpo", "pulpo.jpg"),
                ("pencil", "lápiz", "lápiz.jpg"),
         
            ]
        elif difficulty == "hard":
            words = [
                ("table", "mesa", "mesa.jpg"),
                ("strawberry", "frutilla", "frutilla.jpg"),
                ("lollipop", "chupetín", "chupetín.jpg"),
                ("dog", "perro", "perro.jpg"),
                ("butterfly", "mariposa", "mariposa.jpg"),
                ("shoes", "zapatos", "zapatos.jpg"),
                ("snikers", "zapatos", "zapatillas.jpg"),
                ("hat", "sombrero", "sombrero.jpg"),
                ("duck", "pato", "pato.jpg"),
                ("cake", "pastel", "pastel.jpg"),
                ("sunglasses", "gafas de sol", "gafas_de_sol.jpg"),
                ("kite", "cometa", "kite.jpg"),
                ("strawberry", "frutilla", "frutilla.jpg"),
                ("lollipop", "chupetín", "chupetín.jpg"),
                ("elephant", "elefante", "elefante.jpg"),

            ]

   
        self.words_and_images = random.sample(words, 5)

    def load_next_question(self):
        if self.current_level < len(self.words_and_images):
            _, translation, image = self.words_and_images[self.current_level]

            # Limpia el cuadro de texto
            game_textfield = self.screen_manager.get_screen("game").children[1]
            game_textfield.text = ""

   
            self.game_image.source = image

            game_textfield.hint_text = f"Escribe la palabra '{translation}' en inglés."

         
            self.time_limit = self.time_limits[self.current_difficulty]
            self.remaining_time = self.time_limit
            self.update_time_label()
            Clock.schedule_interval(self.update_time, 1)

        else:
            self.screen_manager.get_screen("end").children[1].text = f"Puntuación de {self.player_name}: {self.score}"
            self.screen_manager.current = "end"

    def update_time_label(self):
        self.time_label.text = f"Tiempo restante: {self.remaining_time}"

    def update_time(self, dt):
        self.remaining_time -= 1
        self.update_time_label()
        if self.remaining_time <= 0:
          
            Clock.unschedule(self.update_time)
            self.check_answer(None)

    def check_answer(self, obj):
        user_answer = self.screen_manager.get_screen("game").children[1].text.strip().lower()

        if self.current_level < len(self.words_and_images):
            _, translation, _ = self.words_and_images[self.current_level]

            
            if user_answer == translation:
                feedback = "¡Correcto!"
            else:
                feedback = "¡Incorrecto!"
                self.remaining_attempts -= 1  

            if self.remaining_attempts <= 0:
                # Sin intentos restantes, el juego termina
                self.game_over()
                return

            # Muestra la retroalimentación visual en un widget apropiado
            game_feedback = self.screen_manager.get_screen("game").children[4]
            game_feedback.text = feedback

            if feedback == "¡Correcto!":
                self.score += 1  

        self.current_level += 1
        self.load_next_question()

    def game_over(self):
        self.screen_manager.get_screen("end").children[1].text = f"Juego Terminado. Puntuación de {self.player_name}: {self.score}"
        self.screen_manager.current = "end"

    def exit_app(self, obj):
        self.stop()

    def restart_game(self):
        self.remaining_attempts = 5  
        self.screen_manager.current = "welcome"  
        self.player_name = ""  
        self.score = 0  
        self.load_words_for_difficulty(self.current_difficulty)  

if __name__ == "__main__":
    MyApp().run()
