import queue
import pygame
from collections import deque
from body import Body

class Snake:
    def __init__(self, game_settings, board):
        self.game_settings = game_settings
        self.board = board
        self.snake = deque()

        for i in range(self.game_settings.snake_initial_length):
            self.extend()

    def get_next_head_position(self):
        head = self.snake[0]
        i = head.i
        j = head.j
        if head.direction == "left":
            j -= 1
        elif head.direction == "right":
            j += 1
        elif head.direction == "top":
            i -= 1
        else:
            i += 1

        if i < 0 or j < 0 or i >= self.game_settings.board_size or j >= self.game_settings.board_size:
            raise "index out of range"
        return i, j

    def extend(self):
        head_direction = ""
        if not self.snake:
            i = j = int(self.game_settings.board_size / 2)
            head_direction = "left"
        else:
            i, j = self.get_next_head_position()
            head_direction = self.snake[0].direction

        x, y = self.board.get_square_position(i, j)
        width, height = self.game_settings.square_size
        body_piece = Body(self.game_settings, i, j, x, y, head_direction)
        self.snake.appendleft(body_piece)

    def draw(self, surface):
        for body in self.snake:
            body.draw(surface)

    def move(self, surface):
        direction = self.snake[0].direction
        i, j = self.get_next_head_position()
        x, y = self.board.get_square_position(i, j)
        self.snake.pop()
        head = Body(self.game_settings, i, j, x, y, direction)
        self.snake.appendleft(head)
