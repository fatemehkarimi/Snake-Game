import queue
import pygame
from collections import deque
from body import Body

class Snake:
    def __init__(self, game_settings, board):
        self.game_settings = game_settings
        self.board = board
        self.snake = deque()

        i = j = int(self.game_settings.board_size / 2)
        for _ in range(self.game_settings.snake_initial_length):
            x, y = board.get_square_position(i, j)
            b = Body(game_settings, i, j, x, y, game_settings.snake_initial_direction)
            self.snake.appendleft(b)
            i, j = self.get_next_head_position()

    def get_next_head_position(self):
        head = self.snake[0]
        board_size = self.game_settings.board_size
        i = head.i
        j = head.j
        if head.direction == "left":
            j = (j + board_size - 1) % board_size
        elif head.direction == "right":
            j = (j + 1) % board_size
        elif head.direction == "up":
            i = (i + board_size - 1) % board_size
        else:
            i = (i + 1) % board_size

        return i, j

    def get_head_postion(self):
        head = self.snake[0]
        return (head.i, head.j)

    def extend(self):
        head_direction = ""
        i, j = self.get_next_head_position()
        head_direction = self.snake[0].direction
        x, y = self.board.get_square_position(i, j)
        width, height = self.game_settings.square_size
        body_piece = Body(self.game_settings, i, j, x, y, head_direction)
        self.snake.append(body_piece)

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

    def set_direction(self, new_direction):
        head = self.snake[0]
        if new_direction in ["left", "right"]:
            if head.direction in ["up", "down"]:
                head.direction = new_direction
        else:
            if head.direction in ["left", "right"]:
                head.direction = new_direction

    def handle_key(self, key):
        if key == pygame.K_LEFT:
            self.set_direction("left")
        elif key == pygame.K_RIGHT:
            self.set_direction("right")
        elif key == pygame.K_UP:
            self.set_direction("up")
        else:
            self.set_direction("down")