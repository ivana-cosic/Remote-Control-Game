# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:51:26 2020

@author: ProBook
"""
import serial
import pygame
import sys
import random

ser = serial.Serial("COM4", 9600)
pygame.init()

# specifications
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
score = 0
MyFont = pygame.font.SysFont("monospace", 35)

# player
Red = (255, 0, 0)
player_p_x = WIDTH / 2
player_size = [50, 50]
player_p_y = HEIGHT - player_size[0]
player_p = [player_p_x, player_p_y]
player_speed = 50

# enemy
enemy_width = [50]
enemy_height = 50
enemy_p = [random.randint(0, WIDTH - enemy_height), 0]
BLUE = (0, 0, 255)
enemy_speed = 10
enemy_list = [enemy_p]
enemy_num = 10
enemy_spawn_chance = 0.1

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# functions

def set_level(score):
    enemy_speed = 10
    enemy_num = 10
    enemy_spawn_chance = 0.1
    if score < 20 :
        pass
    elif score < 30 :
        enemy_speed = 15
        enemy_num = 15
        enemy_spawn_chance = 0.3

    elif score < 100 :
        enemy_speed = 17
        enemy_num = 20
        enemy_spawn_chance = 0.5
    return (enemy_speed, enemy_num, enemy_spawn_chance)


def drop_enemies(enemy_list, enemy_width):
    delay = random.random()
    if len(enemy_list) < enemy_num and delay < enemy_spawn_chance :
        x_pos = random.randint(0, WIDTH - enemy_height)
        y_pos = 0
        #enemy_size1 = random.randint(10, 50)
        enemy_size1 = 50
        enemy_width.append(enemy_size1)
        enemy_list.append([x_pos, y_pos])
        #return enemy_size1


# drawing enemies
def draw_enemies(enemy_list, enemy_width, enemy_height):
    for idx, enemy_p in enumerate(enemy_list):
        pygame.draw.rect(screen, BLUE, (enemy_p[0], enemy_p[1], enemy_width[idx], enemy_height))


# moving enemies
def update_enemy_pos(enemy_list, score, enemy_speed, enemy_width):
    for idx, enemy_p in enumerate(enemy_list):
        if 0 <= enemy_p[1] <= HEIGHT:
            enemy_p[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            enemy_width.pop(idx)
            score += 1
    return score


# multi collision check
def collision_check(enemy_list, player_p, enemy_width):
    for idx, enemy_p in enumerate(enemy_list):
        if collision(player_p, enemy_p, enemy_width[idx]):
            return True
    return False


# single collision function
def collision(player_p, enemy_p, enemy_width1):
    p_x = player_p[0]
    p_y = player_p[1]
    e_x = enemy_p[0]
    e_y = enemy_p[1]

    if ((e_x > p_x) and (e_x < (p_x + player_size[0]))) or ((p_x > e_x) and (p_x < (e_x + enemy_width1))):
        if ((e_y > p_y) and (e_y < (p_y + player_size[0]))) or ((p_y > e_y) and (p_y < (e_y + enemy_height))):
            return True
    return False


# movement and quitting
def movement(player_p_x, dugme):
    if dugme == 1886389754 and 0 < player_p_x:
        player_p_x -= player_speed
    elif dugme == 1886422394  and player_p_x < WIDTH - player_size[0]:
        player_p_x += player_speed
            
    return player_p_x


# game flow
game_over = False

while not game_over:
    dugme = int(ser.readline())
    print(dugme)
    if dugme !=3:
        player_p_x = movement(player_p_x, dugme)
        
        
    player_p = [player_p_x, player_p_y]

    screen.fill(BLACK)

    enemy_speed, enemy_num, enemy_spawn_chance = set_level(score)
    score = update_enemy_pos(enemy_list, score, enemy_speed, enemy_width)

    text = "Score: " + str(score)
    label = MyFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 300, HEIGHT - 40) )

    # enemy_size = drop_enemies(enemy_list)
    drop_enemies(enemy_list, enemy_width)
    draw_enemies(enemy_list, enemy_width, enemy_height)
    if collision_check(enemy_list, player_p, enemy_width):
        game_over = True

    pygame.draw.rect(screen, Red, (player_p_x, player_p_y, player_size[0], player_size[1]))

    clock.tick(30)
    pygame.display.update()
    
print("Your score: " + str(score))
ser.close()
sys.exit()
