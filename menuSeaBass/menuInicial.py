import pygame, pygame_menu
from pygame_menu import Theme
import var

class menuInicial:
    def __init__(self, window):
        self.cerrarMenu = None
        self.clock = pygame.time.Clock()
        self.window = window
        self.contador = 0
        self.i = 0
        '''
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        text = self.font.render(self.font, True, var.white, var.blue)
        '''
        self.fuente = pygame_menu.font.FONT_DIGITAL
        self.mytheme = Theme(title=False, widget_font=self.fuente, widget_font_size=12,
                             widget_background_color=(0, 0, 0, 0), widget_padding=25, background_color=(0, 0, 0, 0))
        self.is_running = True
        self.nombre=""

    def bootScreen(self):
        # Pantalla en blanco
        while self.contador < 30:
            self.clock.tick(60)
            self.window.fill(var.white)
            self.contador = self.contador + 1
            pygame.display.flip()
        # Aparacion logo
        self.contador = 0
        while self.contador < 240:
            self.clock.tick(60)
            if self.i < 255:
                self.i = self.i + 0.5
                var.logoPanico.set_alpha(self.i)
            self.window.blit(var.logoPanico, (0, 0))
            self.contador = self.contador + 1
            pygame.display.flip()
        # Desaparicion imagen
        self.contador = 0
        while self.contador < 150:
            self.clock.tick(60)
            if self.i > 0:
                self.i = self.i - 1
                var.logoPanico.set_alpha(self.i)
            self.window.fill(var.black)
            self.window.blit(var.logoPanico, (0, 0))
            self.contador = self.contador + 1
            pygame.display.flip()

    def Menu(self):
        #Creacion del menu principal
        self.menu = pygame_menu.Menu('', 300, 400, theme=self.mytheme)
        self.menu.add.button('Nueva partida', menuInicial.nuevaPartida)#A submenu nueva partida
        self.menu.add.button('Cargar partida', menuInicial.cargarPartida)#A submenu cargar partida

        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.window)
        while self.cerrarMenu == False:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.window)
            pygame.display.update()

    def nuevaPartida(self):
        # Creacion do submenu
        submenu = pygame_menu.Menu('', 300, 400, theme=self.mytheme)
        submenu.add.text_input('Nombre:', input_underline='-', maxchar=11, input_underline_vmargin=6, onchange=menuInicial.MyTextValue)
        submenu.add.button('Confirmar', menuInicial.guardarNombre)
        submenu.add.button('Atras', pygame_menu.events.RESET)
        return submenu

    def cargarPartida(self):
        # Creacion do submenu
        submenu = pygame_menu.Menu('', 300, 400, theme=self.mytheme)
        # Los datos del selector se obtendrán de la bbdd
        listadoJugadores = [('Diego Lago', 1), ('Juan Carlos', 2)]
        submenu.add.selector('Nombre :', listadoJugadores)
        submenu.add.button('Confirmar', menuInicial.iniciar)
        submenu.add.button('Atras', pygame_menu.events.RESET)
        return submenu

    def MyTextValue(self, name):
        print("Nombre: " + name)
        self.nombre = name

    def guardarNombre(self):
        print("Nombre final:"+self.nombre)
        menuInicial.iniciar(self)

    def iniciar(self):
        print("cerrar")
        self.cerrarMenu = True