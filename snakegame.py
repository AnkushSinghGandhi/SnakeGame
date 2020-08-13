import pygame
import time
import random

# pygamge initialization
pygame.init()
clock = pygame.time.Clock()

# colors
orange = (255,123,7)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

# title and size of window
display_height = 400
display_width = 600
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Legend of Snake Game")

snake_block = 10
snake_speed = 9
snake_list = []

# snake structure and position
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display,orange,[round(x[0]),round(x[1]),snake_block,snake_block])

# main function
def snakegame():
    game_over = False
    game_end = False
    # cordinates of snake
    x1 = display_width / 2
    y1 = display_height / 2
    # change in cordinates of snake
    x1_change = 0
    y1_change = 0

    # length of snake
    snake_list = []
    length_of_snake = 1

    # cordinate of food
    foodx = round(random.randrange(0,display_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0,display_height - snake_block) / 10.0) * 10

    while not game_over:
        while game_end == True:
            
            display.fill(blue)
            font_style = pygame.font.SysFont("comicsansms",25)
            msg = font_style.render("You Lost! wanna play again? Press P", True, red)
            display.blit(msg,[(display_width / 6), (display_height / 3)])
            
            # score board
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms",35)
            value = score_font.render("Your Score:" + str(score), True, green)
            display.blit(value,[round(display_width / 3), round(display_height / 5)])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over = True #the window is still open
                    game_end = False #game has been ended

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

        # updating co-ordinates with changed positions
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display,green,[foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        # when lenth of snake exceeds, delete the snake list and it will end the game
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # when snake hits himself game ends
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        
        snake(snake_block,snake_list)
        pygame.display.update()

        # when snake hits the food length of snake was increased by 1
        if (x1 == foodx) and (y1 == foody):
            foodx = round(random.randrange(0,display_width - snake_block) / 10.0) * 10
            foody = round(random.randrange(0,display_height - snake_block) / 10.0) * 10
            length_of_snake +=1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

snakegame()