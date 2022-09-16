# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pygame


pygame.init()


class Button:
    basic_font = pygame.font.SysFont(None, 24)

    def __init__(self, scr, x, y, func, w=100, h=100, txt=""):
        self.screen = scr
        self.x_coordinate = x
        self.y_coordinate = y
        self.pressed_method = func
        self.height = h
        self.width = w
        self.text = txt

        mouse = pygame.mouse.get_pos()
        if self.x_coordinate < mouse[0] < self.x_coordinate + self.width and \
           self.y_coordinate < mouse[1] < self.y_coordinate + self.height:
            self.mouse_hover()
        else:
            self.normal()

        text = self.basic_font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.x_coordinate + 10, self.y_coordinate + 10))

    def button_pressed(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.x_coordinate < event.pos[0] < self.x_coordinate + self.width and \
                        self.y_coordinate < event.pos[1] < self.y_coordinate + self.height:
                    self.mouse_press()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.x_coordinate < event.pos[0] < self.x_coordinate + self.width and \
                   self.y_coordinate < event.pos[1] < self.y_coordinate + self.height:
                    self.mouse_hover()

    def normal(self):
        normal_image = pygame.image.load("button_img/normal.png")
        normal_image = pygame.transform.scale(normal_image, (self.width, self.height))
        self.screen.blit(normal_image, (self.x_coordinate, self.y_coordinate))

    def mouse_hover(self):
        hovered_image = pygame.image.load("button_img/hover.png")
        hovered_image = pygame.transform.scale(hovered_image, (self.width, self.height))
        self.screen.blit(hovered_image, (self.x_coordinate, self.y_coordinate))

    def mouse_press(self):
        pressed_image = pygame.image.load("button_img/pressed.png")
        pressed_image = pygame.transform.scale(pressed_image, (self.width, self.height))
        self.screen.blit(pressed_image, (self.x_coordinate, self.y_coordinate))
        self.pressed_method()


if __name__ == "__main__":

    screen = pygame.display.set_mode((800, 700))
    game_running = True
    while game_running:
        screen.fill((0, 0, 0))

        def new_game():
            print("Hello, World!")

        button_new_game = Button(screen, 10, 10, new_game, 100, 50, "Нова гра")

        for event in pygame.event.get():
            # Вихід
            if event.type == pygame.QUIT:
                game_running = False
            button_new_game.button_pressed(event)

        pygame.display.update()
