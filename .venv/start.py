import random

import pygame
from sys import exit

width = 800
height = 600
padding = width * 0.05


def random_array(length, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]


def array_of_rectangles(arr):
    array_of_rectangles = []

    available_height = height - 200
    max_val = max(arr) if len(arr) > 0 else 1

    width_of_rectangle = (width - 2 * padding) / len(arr)
    x = padding

    for i in arr:
        scaled_height = (i / max_val) * available_height

        rect = pygame.Rect(x, height - scaled_height, width_of_rectangle, scaled_height)

        array_of_rectangles.append(rect)
        x += width_of_rectangle

    return array_of_rectangles

def draw_rects(arr):
    for c, r in enumerate(rects):
        if c % 2 == 0:
            color = pygame.Color(169, 169, 169)
        else:
            color = pygame.Color("white")
        pygame.draw.rect(screen, color, r)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SLE - SortLimitExceeded")
running = True
clock = pygame.time.Clock()
dt = 0

arr = random_array(50, 1, 200)
rects = array_of_rectangles(arr)

while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                arr = random_array(50, 1, 200)
                rects = array_of_rectangles(arr)


    screen.fill((20, 20, 30))

    draw_rects(arr)


    pygame.display.flip()
