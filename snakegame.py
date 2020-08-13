import pygame
import time
import random

pygame.init()

orange = (255,123,7)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

display_height = 400
display_width = 600

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Legend of Snake Game")

snake_list = []
snake_block = 12

def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display,orange,[x[0],x[1],snake_block,snake_block])

def snakegame():
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        pygame.display.update()
    pygame.quit()
    quit()