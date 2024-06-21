import pygame
from settings import *
from player import Player
from controls import handle_input
from level import Level
from highscore import update_highscore

def start_game():
    """
    Start the game loop.
    """
    pygame.init()  # Initialize all the pygame modules

    # Set up the display window with fullscreen mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Pixel Adventure")
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    player = Player()  # Create a Player object
    all_sprites = pygame.sprite.Group()  # Create a group to hold all sprites
    all_sprites.add(player)  # Add the player to the group

    level = Level()  # Create a Level object

    running = True  # Set the running flag to True to start the game loop
    score = 0  # Initialize the score
    start_time = pygame.time.get_ticks()  # Record the start time

    font = pygame.font.Font(None, 36)  # Font for displaying text

    while running:
        # Handle events such as closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the game loop

        # Handle player input and update the running state
        running = handle_input(player, running)

        # Update the player state
        player.update(level)

        # Update the level state
        level.update()

        # Calculate the camera offset to keep the player centered on the screen
        camera_offset = (player.rect.centerx - SCREEN_WIDTH // 2, player.rect.centery - SCREEN_HEIGHT // 2)

        screen.fill(BG_COLOR)  # Fill the screen with the background color

        # Draw the level with the camera offset
        level.draw(screen, camera_offset)

        # Draw all sprites with the camera offset
        for sprite in all_sprites:
            screen.blit(sprite.image, (sprite.rect.x - camera_offset[0], sprite.rect.y - camera_offset[1]))

        # Display the current score
        score_surface = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))

        # Display the elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Time in seconds
        time_surface = font.render(f"Time: {elapsed_time:.2f}", True, (255, 255, 255))
        screen.blit(time_surface, (SCREEN_WIDTH - 200, 10))

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Cap the frame rate at 60 frames per second

    # Save high score for the current level
    update_highscore("1", player.score)  # Replace "1" with the actual level identifier

    pygame.quit()  # Quit pygame when the game loop ends

def show_level_complete_ui():
    """
    Display the UI when the level is complete and handle user input.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Pixel Adventure - Level Complete")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)

    menu_options = ["Next Level", "Back to Menu"]
    selected_option = 0

    running = True
    while running:
        screen.fill(BG_COLOR)

        title_surface = title_font.render("Level Complete!", True, (255, 255, 255))
        screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 100))

        for i, option in enumerate(menu_options):
            color = (255, 255, 0) if i == selected_option else (255, 255, 255)
            option_surface = font.render(option, True, color)
            screen.blit(option_surface, (SCREEN_WIDTH // 2 - option_surface.get_width() // 2, 300 + i * 50))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Next Level
                        from menu import level_selection
                        level_selection()  # For now, go back to level selection
                    elif selected_option == 1:  # Back to Menu
                        from menu import main_menu
                        main_menu()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    from menu import main_menu
    main_menu()
