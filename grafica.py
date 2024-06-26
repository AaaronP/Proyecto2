import os, sys
import random

# Elimina el print por defecto de pygame
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")

import pygame

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__


ANCHO, ALTO = 400, 400
TAMANO_CELDA = 40

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

colores = {}


def generar_color_aleatorio():
    # obtemos colores aleatorios
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def obtener_color(valor):
    # verificamos que no existan colores iguales
    if valor not in colores:
        colores[valor] = generar_color_aleatorio()
    return colores[valor]


def dibujar_tablero(matriz):
    # Dimensiones del tablero
    FILAS = len(matriz)
    COLUMNAS = len(matriz[0])

    # iniciamos el app
    pygame.init()

    # definimos las dimensiones del tablero y cuadros
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Tablero de Katamino")

    reloj = pygame.time.Clock()
    corriendo = True

    # Termina hasta que se cierra el app
    while corriendo:
        pantalla.fill(BLANCO)

        # Dibujar celdas del tablero
        for fila in range(FILAS):
            for col in range(COLUMNAS):
                valor = matriz[fila][col]

                if valor != ".":
                    color = obtener_color(matriz[fila][col])
                    pygame.draw.rect(
                        pantalla,
                        color,
                        (
                            col * TAMANO_CELDA,
                            fila * TAMANO_CELDA,
                            TAMANO_CELDA,
                            TAMANO_CELDA,
                        ),
                    )
                pygame.draw.rect(
                    pantalla,
                    NEGRO,
                    (
                        col * TAMANO_CELDA,
                        fila * TAMANO_CELDA,
                        TAMANO_CELDA,
                        TAMANO_CELDA,
                    ),
                    1,
                )

        # eventListener
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
