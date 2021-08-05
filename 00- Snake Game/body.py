import pygame

class Body:
    def __init__(self, game_settings, i, j, x, y, direction):
        self.game_settings = game_settings
        self.i = i
        self.j = j
        self.direction = direction
        width, height = self.game_settings.square_size
        self.body_piece = pygame.rect.Rect((x, y, width, height))

    def draw(self, surface):
        pygame.draw.rect(surface, self.game_settings.snake_color, self.body_piece)