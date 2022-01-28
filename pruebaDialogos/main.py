import pygame, pygame_menu
from pygame_menu import Theme

pygame.init()
surface = pygame.display.set_mode((600, 400))

#Métodos
def set_difficulty(value, difficulty):
    pass

pygame.display.set_caption('Prueba menu')

#TEXTO
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 400
Y = 400
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Fin de la prueba', True, white, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)

def pantallaInicio():

    contadorTiempo = 0
    imagen = pygame.image.load("logo.png")
    #Pantalla en blanco
    while(contadorTiempo<30):
        clock.tick(60)
        surface.fill(white)
        pygame.display.flip()
        contadorTiempo=contadorTiempo+1
    contadorTiempo=0
    #Aparacion logo
    i=0
    while (contadorTiempo < 240):
        clock.tick(60)
        if(i<255):
            i = i + 0.5
            imagen.set_alpha(i)
            print(i)
        surface.blit(imagen, (0, 0))
        pygame.display.flip()
        contadorTiempo=contadorTiempo + 1
    contadorTiempo=0
    #Desaparicion imagen
    while (contadorTiempo < 150):
        clock.tick(60)
        if(i>0):
            i = i - 1
            imagen.set_alpha(i)
            print(i)
        surface.fill(black)
        surface.blit(imagen, (0, 0))
        pygame.display.flip()
        contadorTiempo=contadorTiempo + 1
#Ejecucion pantalla inicio
pantallaInicio()

#Creacion do menu personalizado
fuente = pygame_menu.font.FONT_DIGITAL #Fuente a utilizar
#Menu personalizado
mytheme = Theme(title=False, widget_font=fuente, widget_font_size=12, widget_background_color=(0, 0, 0, 0), widget_padding=25, background_color=(0, 0, 0, 0))

def iniciar():
    while True:
        surface.fill((255,255,255,255))
        surface.blit(text, textRect)
        pygame.display.flip()

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

        pygame.quit()

def nuevaPartida():
    #Creacion do submenu
    submenu = pygame_menu.Menu('', 300, 400,theme=mytheme)
    submenu.add.text_input('Nombre:', input_underline='-', maxchar=(11), input_underline_vmargin=6)
    submenu.add.button('Confirmar', iniciar)
    submenu.add.button('Atras', pygame_menu.events.RESET)
    return submenu

def cargarPartida():
    #Creacion do submenu
    submenu = pygame_menu.Menu('', 300, 400,theme=mytheme)
    #Los datos del selector se obtendrán de la bbdd
    submenu.add.selector('Nombre :', [('Diego Lago', 1), ('Juan Carlos', 2)], onchange=set_difficulty)
    submenu.add.button('Confirmar', iniciar)
    submenu.add.button('Atras', pygame_menu.events.RESET)
    return submenu
#Creacion do menu
menu = pygame_menu.Menu('', 300, 400,theme=mytheme)
menu.add.button('Nueva partida', nuevaPartida())
menu.add.button('Cargar partida', cargarPartida())
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)
    pygame.display.update()