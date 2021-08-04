class GameSettings:
    # Main window settings
    window_size = (1200, 800)
    window_top_margin = 75
    window_left_margin = 100
    background_color = (40, 30, 39)

    # Board game settings
    board_size = 15
    square_size = (
        (window_size[0] - window_left_margin * 2) / board_size,
        (window_size[1] - window_top_margin * 2) / board_size
    )
    square_color1 = (178, 142, 154)
    square_color2 = (76, 70, 114)

    #Food settings
    food_size = (int(square_size[0]), int(square_size[1]))