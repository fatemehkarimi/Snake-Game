import pygame
from game_settings import GameSettings
from board import Board
from food import Food
from snake import Snake

def main():
    g_settings = GameSettings()
    screen = pygame.display.set_mode(g_settings.window_size)
    screen.fill(g_settings.background_color)
    logo = pygame.image.load('img/logo.png')
    pygame.display.set_caption('Snake Game')
    pygame.display.set_icon(logo)

    board = Board(g_settings)
    food = Food(g_settings)
    snake = Snake(g_settings, board)

    board.draw(screen)
    food.initiate_food(board)
    food.draw(screen)
    snake.draw(screen)
    pygame.display.flip()

    running = True
    extended = False
    while running:
        pygame.time.wait(300)
        snake.move(screen)
        board.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]:
                    snake.handle_key(event.key)

        snake_head = snake.get_head_postion()
        if snake_head == food.current_location:
            snake.extend()
            snake.draw(screen)
            food.initiate_food(board)


if __name__ == '__main__':
    main()