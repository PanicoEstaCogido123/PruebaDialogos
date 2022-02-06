#imports
import pygame
import var
from menuInicial import menuInicial

#objetos
pygame.init()
pygame.display.set_caption("Seabass")
pygame.display.set_icon(var.icono)
window = pygame.display.set_mode((600, 400))
menu = menuInicial(window)

#controlador
if __name__ == '__main__':
    menu.bootScreen()
    menu.Menu()
    while True:
        window.fill(var.black)