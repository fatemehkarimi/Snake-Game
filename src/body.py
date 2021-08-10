import pygame

class Body:
    def __init__(self, game_settings, i, j, x, y, direction):
        self.game_settings = game_settings
        self.i = i
        self.j = j
        self.direction = direction
        width, height = self.game_settings.square_size
        self.body_piece = pygame.rect.Rect((x, y, width, height))

    def update_position(self, i, j, x, y):
        self.i = i
        self.j = j
        delta_x = x - self.body_piece.x
        delta_y = y - self.body_piece.y
        self.body_piece = self.body_piece.move(delta_x, delta_y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.game_settings.snake_color, self.body_piece)
