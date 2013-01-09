'''
Created on 06/01/2013

@author: Jose
'''
import pygame
from pygame.locals import *
class Clase1:
    def juego(self): 
        flag=0
        
        pygame.init()
         
        pantalla = pygame.display.set_mode((470,300),0,32)
        pygame.display.set_caption("Cuentos de Navidad")
        fondo = pygame.image.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/fondo1.jpg").convert()
        pantalla.blit(fondo, (0, 0))
 
        reloj = pygame.time.Clock()
         
        pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo0.ogg")
        pygame.mixer.music.play(1)
        
        
        while True:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    exit()
                if eventos.type == pygame.KEYDOWN:
                    if eventos.key == pygame.K_ESCAPE:
                        exit()
                    if eventos.key == pygame.K_LEFT:
                        if flag == 0:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo1.ogg")
                            pygame.mixer.music.play(1)
                            flag=1
                        elif flag == 1:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo11.ogg")
                            pygame.mixer.music.play(1)
                            flag=3
                        
                    if eventos.key == pygame.K_RIGHT:
                        if flag == 0:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo2.ogg")
                            pygame.mixer.music.play(1)
                            flag=2
                        elif flag == 1:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo12.ogg")
                            pygame.mixer.music.play(1)
                            flag=4
                        elif flag == 2:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo21.ogg")
                            pygame.mixer.music.play(1)
                            flag=5
                        elif flag == 3:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo11f.ogg")
                            pygame.mixer.music.play(1) 
                        elif flag == 4:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo12f.ogg")
                            pygame.mixer.music.play(1)  
                        elif flag == 5:
                            pygame.mixer.music.load("C:/Users/josc__000/Documents/GitHub/Proyecto-Python/Proyecto_python_Lenguaje/sonidos/nodo21f.ogg")
                            pygame.mixer.music.play(1)    
                                             
                    if eventos.key == pygame.K_UP:
                        pygame.mixer.music.unpause()
                    if eventos.key == pygame.K_DOWN:
                        pygame.mixer.music.pause()
            reloj.tick(20)
            pygame.display.update()