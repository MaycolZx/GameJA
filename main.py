import pygame
import sys
import random
import os
# import pandas as pd
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho = 800
alto = 600
window_size = (ancho, alto)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego de Eclipse")
running = True
pathSrc = "./src/"
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def escena_menu():
    # Limpiar el escenario
    screen.fill((0, 0, 0))
    imagenLogo = pygame.image.load('src/BackgroundMenu.png')
    spsheet = pygame.image.load('src/moonSpriteS.png')
    imagenLogoRedimensionada = pygame.transform.scale(imagenLogo, (800, 600))
    animationArray = []
    numFrames = 50
    frameWidth = 100
    frameHeight = 100
    posx = 0
    for i in range(numFrames):
        f1 = spsheet.subsurface(posx, 0, frameWidth, frameHeight)
        animationArray.append(f1)
        posx+= 100

    clock = pygame.time.Clock()
    FPS = 15  # Frames por segundo
    running = True
    current_frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verificar si se hizo clic en el botón "Jugar"
                if 300 <= x <= 500 and 250 <= y <= 300:
                    return 'JUGAR'
                # Verificar si se hizo clic en el botón "Salir"
                elif 300 <= x <= 500 and 450 <= y <= 500:
                    return 'QUIT'

        # Dibujar el frame actual
        posLuna = (190, (alto/2)-100-100)
        screen.blit(animationArray[current_frame],posLuna )
        # Actualizar el frame actual
        current_frame += 1
        if current_frame >= numFrames:
            current_frame = 0
        # Dibujar el Logo
        posLogo = (0, 0)
        screen.blit(imagenLogoRedimensionada,posLogo)
        # Crear un botón "Jugar"
        pygame.draw.rect(screen, RED, (300, 250, 200, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Jugar", True, WHITE)
        screen.blit(texto_jugar, (350, 260))
         # Crear un botón "Opciones"
        pygame.draw.rect(screen, RED, (300, 350, 200, 50))
        texto_salir = font.render("Opciones", True, WHITE)
        screen.blit(texto_salir, (340, 360))
        # Crear un botón "Salir"
        pygame.draw.rect(screen, RED, (300, 450, 200, 50))
        texto_salir = font.render("Salir", True, WHITE)
        screen.blit(texto_salir, (350, 460))

        pygame.display.flip()
        clock.tick(FPS) 

def escena_MiniGames():
    # Limpiar el escenario
    screen.fill((0, 0, 0))
    imagenLogo = pygame.image.load('src/BackgroundMenu.png')
    spsheet = pygame.image.load('src/moonSpriteS.png')
    imagenLogoRedimensionada = pygame.transform.scale(imagenLogo, (800, 600))
    animationArray = []
    numFrames = 50
    frameWidth = 100
    frameHeight = 100
    posx = 0
    for i in range(numFrames):
        f1 = spsheet.subsurface(posx, 0, frameWidth, frameHeight)
        animationArray.append(f1)
        posx+= 100

    clock = pygame.time.Clock()
    FPS = 15  # Frames por segundo
    running = True
    current_frame = 0
    alineamiento = 100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Verificar si se hizo clic en el botón "Jugar"
                if 50 <= x <= 300 and alto-75 <= y <= alto-25:
                    return 'REGRESAR'
                elif alineamiento+50 <= x <= alineamiento+300 and 250 <= y <= 300:
                    return 'MOON-POS'
                elif alineamiento+350 <= x <= alineamiento+550 and 250 <= y <= 300:
                    return 'QUIZ-CH'
                elif alineamiento+50 <= x <= alineamiento+300 and 350 <= y <= 400:
                    return 'QUIZ-GA'
                elif alineamiento+350 <= x <= alineamiento+550 and 350 <= y <= 400:
                    return 'DINAMIC-OS'
                elif alineamiento+50 <= x <= alineamiento+300 and 450 <= y <= 500:
                    return 'FIND-OBJ'
                elif alineamiento+350 <= x <= alineamiento+550 and 450 <= y <= 500:
                    return 'PUZZLE'
                elif ancho-175 <= x <= ancho-25 and alto-75 <= y <= alto-25:
                    return 'CREDITOS'

        # Dibujar el frame actual
        posLuna = (190, (alto/2)-100-100)
        screen.blit(animationArray[current_frame],posLuna )
        # Actualizar el frame actual
        current_frame += 1
        if current_frame >= numFrames:
            current_frame = 0
        # Dibujar el Logo
        posLogo = (0, 0)
        screen.blit(imagenLogoRedimensionada,posLogo)
        # Crear un botón "JuegoMaycol"
        pygame.draw.rect(screen, RED, (alineamiento+50, 250, 250, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Position eclipse", True, WHITE)
        screen.blit(texto_jugar, (alineamiento+50, 260))
        # Crear un botón "JuegoChega"
        pygame.draw.rect(screen, RED, (alineamiento+350, 250, 200, 50))
        texto_Quiz = font.render("Quiz", True, WHITE)
        screen.blit(texto_Quiz, (alineamiento+350, 260))
        # Crear un botón "JuegoGabo"
        pygame.draw.rect(screen, RED, (alineamiento+50, 350, 250, 50))
        texto_Quiz = font.render("QuizDate", True, WHITE)
        screen.blit(texto_Quiz, (alineamiento+50, 360))
        # Crear un botón "JuegoOsc"
        pygame.draw.rect(screen, RED, (alineamiento+350, 350, 200, 50))
        texto_Quiz = font.render("Match", True, WHITE)
        screen.blit(texto_Quiz, (alineamiento+350, 360))
        # Crear un botón "JuegoWill"
        pygame.draw.rect(screen, RED, (alineamiento+50, 450, 250, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Look for Glasses", True, WHITE)
        screen.blit(texto_jugar, (alineamiento+50, 460))
        # Crear un botón "JuegoMau"
        pygame.draw.rect(screen, RED, (alineamiento+350, 450, 200, 50))
        font = pygame.font.Font(None, 36)
        texto_jugar = font.render("Puzzle", True, WHITE)
        screen.blit(texto_jugar, (alineamiento+350, 460))
        # Crear un botón "Regreso"
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, RED, (50, alto-75, 150, 50))
        texto_regresar = font.render("Regresar", True, WHITE)
        screen.blit(texto_regresar, (50, alto-65))
        # Crear un botón "Next-Creditos"
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, RED, (ancho-175, alto-75, 150, 50))
        texto_regresar = font.render("Next", True, WHITE)
        screen.blit(texto_regresar, (ancho-175, alto-65))

        pygame.display.flip()
        clock.tick(FPS) 

escena_actual = escena_menu

while True:
    resultado = escena_actual()
    if resultado == 'QUIT':
        break
    elif resultado == 'JUGAR':
        escena_actual = escena_MiniGames
    elif resultado == 'REGRESAR':
        escena_actual = escena_menu

pygame.quit()