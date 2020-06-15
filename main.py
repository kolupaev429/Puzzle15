# -*- coding: utf-8 -*-
# !/usr/bin/env python

import numpy as np
import pygame
from random import sample
import button as btn

# Ініцалізація модулю pygame
pygame.init()

# Створення вікна заданих розмірів
screen = pygame.display.set_mode((800, 700))
# Установка заголовку
pygame.display.set_caption("П’ятнашки")
# Установка іконки ігового вікна
icon = pygame.image.load("img/logo.png")
pygame.display.set_icon(icon)
# Створення стандартних кольорів
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SOFT_YELLOW = (238, 232, 170)

# Створення масиву ігрового поля
game_board = np.zeros((4, 4), dtype=int)
# Позиція нуля на ігровому полі
zero_position_x = 3
zero_position_y = 0
# Ліва верхня точка ігрового поля
initial_point_x = 100
initial_point_y = 75


# Функції, що забезпечують логіку гри
def game_board_randomizer():
    """ Функція, що заповнює масив game_board випадковими значеннями від 0 до 15.
        Значення вибираються таким чином, щоб існував спосіб переведення отриманої позиції у виграшну. """

    random_list = sample(range(1, 16), k=15)
    number_of_irregular_pairs = 0
    for i in range(14):
        current_number = random_list[i]
        for j in range(i + 1, 15):
            if current_number > random_list[j]:
                number_of_irregular_pairs += 1

    if number_of_irregular_pairs % 2 == 0:
        random_list[0], random_list[1] = random_list[1], random_list[0]

    random_list.append(0)
    number = 0
    regular_direction = True
    for i in range(4):
        for j in range(4):
            game_board[i, j] = random_list[number]
            if regular_direction and number % 4 == 3:
                number += 5
                regular_direction = not regular_direction
            elif not regular_direction and number % 4 == 0:
                number += 3
                regular_direction = not regular_direction

            if regular_direction:
                number += 1
            else:
                number -= 1


def game_board_descriptor():
    """ Функція, що відображує на екрані заповнене ігрове поле. """

    for i in range(4):
        for j in range(4):
            try:
                number_image = pygame.image.load("img/n_" + str(game_board[i, j]) + ".png")
                screen.blit(number_image, (initial_point_x + 150 * j, initial_point_y + 150 * i))
            except pygame.error:
                pass


player_won = False


def new_game():
    global player_won
    game_board_randomizer()
    player_won = False


game_board_randomizer()
game_running = True

# Головний цикл гри
while game_running:
    screen.fill(WHITE)
    button_new_game = btn.Button(screen, 160, 10, new_game, 200, 60, "Нова гра")
    button_exit = btn.Button(screen, 450, 10, exit, 200, 60, "Вихід")
    for event in pygame.event.get():
        button_new_game.button_pressed(event)
        button_exit.button_pressed(event)
        # Вихід
        if event.type == pygame.QUIT:
            game_running = False
        # Натиснення клавіш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if (zero_position_x - 1) >= 0:
                    game_board[zero_position_x, zero_position_y] = game_board[zero_position_x - 1, zero_position_y]
                    game_board[zero_position_x - 1, zero_position_y] = 0
                    zero_position_x, zero_position_y = zero_position_x - 1, zero_position_y

            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if (zero_position_x + 1) <= 3:
                    game_board[zero_position_x, zero_position_y] = game_board[zero_position_x + 1, zero_position_y]
                    game_board[zero_position_x + 1, zero_position_y] = 0
                    zero_position_x, zero_position_y = zero_position_x + 1, zero_position_y

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if (zero_position_y - 1) >= 0:
                    game_board[zero_position_x, zero_position_y] = game_board[zero_position_x, zero_position_y - 1]
                    game_board[zero_position_x, zero_position_y - 1] = 0
                    zero_position_x, zero_position_y = zero_position_x, zero_position_y - 1

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if (zero_position_y + 1) <= 3:
                    game_board[zero_position_x, zero_position_y] = game_board[zero_position_x, zero_position_y + 1]
                    game_board[zero_position_x, zero_position_y + 1] = 0

                    zero_position_x, zero_position_y = zero_position_x, zero_position_y + 1

    if player_won:
        pygame.time.wait(100)
        winning_image = pygame.image.load("img/winning_img.jpg")
        screen.blit(winning_image, (initial_point_x + 100, initial_point_y + 150))
    else:
        game_board_descriptor()
        winning_board = np.array([[1, 2, 3, 4],
                                  [5, 6, 7, 8],
                                  [9, 10, 11, 12],
                                  [13, 14, 15, 0]], dtype=int)
        if np.array_equal(game_board, winning_board):
            player_won = True
    pygame.display.update()
