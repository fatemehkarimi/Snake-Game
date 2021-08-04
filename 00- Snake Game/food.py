from game_settings import GameSettings
import pygame
import random

class Food:
    def __init__(self, game_settings):
        self.game_settings = game_settings

        f1 = pygame.image.load('img/food_1.png')
        f2 = pygame.image.load('img/food_2.png')
        f3 = pygame.image.load('img/food_3.png')
        f4 = pygame.image.load('img/food_4.png')
        f5 = pygame.image.load('img/food_5.png')
        f6 = pygame.image.load('img/food_6.png')

        f1 = pygame.transform.scale(f1, game_settings.food_size)
        f2 = pygame.transform.scale(f2, game_settings.food_size)
        f3 = pygame.transform.scale(f3, game_settings.food_size)
        f4 = pygame.transform.scale(f4, game_settings.food_size)
        f5 = pygame.transform.scale(f5, game_settings.food_size)
        f6 = pygame.transform.scale(f6, game_settings.food_size)

        self.food_icons  = [f1, f2, f3, f4, f5, f6]

    def next_location(self, board):
        i = random.randint(0, self.game_settings.board_size - 1)
        j = random.randint(0, self.game_settings.board_size - 1)
        self.current_location = (i, j)
        return board.get_square_position(i, j)

    def draw(self, surface, board):
        self.current_food = random.randint(0, len(self.food_icons) - 1)
        position = self.next_location(board)
        surface.blit(self.food_icons[self.current_food], position)
