from direction import Directions
class GameSettings:
    # game settings
    initial_time_quantom = 300
    message_color = (247, 233, 141)

    # Main window settings
    window_size = (1200, 900)
    window_top_margin = 75
    window_left_margin = 100
    background_color = (40, 30, 39)

    # Board game settings
    board_size = 20
    square_size = (
        (window_size[0] - window_left_margin * 2) / board_size,
        (window_size[1] - window_top_margin * 2) / board_size
    )
    square_color1 = (151, 199, 129)
    square_color2 = (255, 224, 194)

    # Food settings
    food_size = (int(square_size[0]), int(square_size[1]))

    # Snake settings
    snake_initial_length = min(int(board_size / 4), 4)
    snake_speed = 1
    snake_color = (46, 29, 15)
    snake_initial_direction = Directions.LEFT