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

snake_block = 12

def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display,orange,[x[0],x[1],snake_block,snake_block])

def snakegame():
    game_over = False
    game_end = False
    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    y1_change = 0
                    x1_change = -snake_block
                if event.key == pygame.K_RIGHT:
                    y1_change = 0
                    x1_change = snake_block
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 <0:
            game_end = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(display,green,[foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        
        snake(snake_block,snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            
    pygame.quit()
    quit()