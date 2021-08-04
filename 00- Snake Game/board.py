
import pygame
from game_settings import GameSettings

class Board:
    def __init__(self, game_settings):
        self.board_size = game_settings.board_size
        self.square_size = game_settings.square_size
        self.square_colors = [game_settings.square_color1, game_settings.square_color2]
        self.squares = []

        top_margin = game_settings.window_top_margin
        left_margin = game_settings.window_left_margin

        for i in range(self.board_size):
            for j in range(self.board_size):
                x = left_margin + j * self.square_size[0]
                y = top_margin + i * self.square_size[1]
                s = pygame.rect.Rect((x, y, self.square_size[0], self.square_size[1]))
                self.squares.append(s)


    def draw(self, surface):
        toggle = True
        for i in range(self.board_size):
            for j in range(self.board_size):
                if j % 2:
                    color = self.square_colors[toggle]
                else:
                    color = self.square_colors[(toggle + 1) % 2]
                pygame.draw.rect(surface, color, self.squares[i * self.board_size + j])
            toggle = not toggle

    def get_square_position(self, i, j):
        return (
            self.squares[i * self.board_size + j].x,
            self.squares[i * self.board_size + j].y)
