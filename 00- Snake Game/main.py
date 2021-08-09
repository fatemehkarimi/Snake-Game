import pygame
from game_settings import GameSettings
from board import Board
from food import Food
from snake import Snake

def show_game_over_message(surface, game_settings):
    window_width = game_settings.window_size[0]
    window_height = game_settings.window_size[1]

    font = pygame.font.SysFont('monospace', window_width // 50)
    message = font.render('Game Over! press space to restart the game.', True,
                    game_settings.message_color)
    message_rect = message.get_rect(center=(window_width // 2, int(window_height * 0.95)))
    surface.blit(message, message_rect)
    pygame.display.update()

def show_score(surface, game_settings, score):
    window_width = game_settings.window_size[0]
    window_height = game_settings.window_size[1]

    font = pygame.font.SysFont('monospace', window_width // 50)
    message = font.render(str(score), True, game_settings.message_color)
    message_rect = message.get_rect(center=(int(window_width * 0.05), int(window_height * 0.95)))
    surface.blit(message, message_rect)
    pygame.display.update()


def main():
    pygame.init()
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
    game_over = False
    score = 0
    time_quantom = g_settings.initial_time_quantom

    show_score(screen, g_settings, score)
    while running:
        pygame.time.wait(time_quantom)
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_over = False
                    score = 0
                    screen.fill(g_settings.background_color)
                    food.initiate_food(board)
                    snake.initiate_snake()
            continue

        screen.fill(g_settings.background_color)
        snake.move(screen)
        board.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        show_score(screen, g_settings, score)
        pygame.display.update()

        arrow_keys_handled = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not arrow_keys_handled:
                if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]:
                    snake.handle_key(event.key)
                    arrow_keys_handled = True

        snake_head = snake.get_head_postion()
        if snake_head == food.current_location:
            snake.extend()
            food.initiate_food(board)
            score += g_settings.feed_score

        if snake.snake_collide_with_self():
            game_over = True
            show_game_over_message(screen, g_settings)


if __name__ == '__main__':
    main()