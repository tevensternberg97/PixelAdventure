import pygame
import sys
from settings import *
from highscore import load_highscores

def main_menu():
    """
    Display the main menu and handle user input for navigating the menu.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Pixel Adventure - Main Menu")
    clock = pygame.time.Clock()

    # Load high scores
    highscores = load_highscores()
    highscore_text = "High Scores:\n" + "\n".join([f"Level {level}: {score}" for level, score in highscores.items()])

    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)

    def draw_text(surface, text, position, font, color=(255, 255, 255)):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            surface.blit(text_surface, (position[0], position[1] + i * font.get_height()))

    menu_options = ["Start Game", "Controls", "Quit"]
    selected_option = 0

    running = True
    while running:
        screen.fill(BG_COLOR)

        title_surface = title_font.render("Pixel Adventure", True, (255, 255, 255))
        screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 100))

        for i, option in enumerate(menu_options):
            color = (255, 255, 0) if i == selected_option else (255, 255, 255)
            option_surface = font.render(option, True, color)
            screen.blit(option_surface, (SCREEN_WIDTH // 2 - option_surface.get_width() // 2, 300 + i * 50))

        draw_text(screen, highscore_text, (50, 500), font)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game
                        level_selection()
                    elif selected_option == 1:  # Controls
                        show_controls()
                    elif selected_option == 2:  # Quit
                        pygame.quit()
                        sys.exit()

def level_selection():
    """
    Display the level selection menu and handle user input for selecting a level.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Pixel Adventure - Level Selection")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)

    levels = ["Level 1"]
    selected_level = 0

    running = True
    while running:
        screen.fill(BG_COLOR)

        title_surface = title_font.render("Select a Level", True, (255, 255, 255))
        screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 100))

        for i, level in enumerate(levels):
            color = (255, 255, 0) if i == selected_level else (255, 255, 255)
            level_surface = font.render(level, True, color)
            screen.blit(level_surface, (SCREEN_WIDTH // 2 - level_surface.get_width() // 2, 300 + i * 50))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_level = (selected_level + 1) % len(levels)
                elif event.key == pygame.K_UP:
                    selected_level = (selected_level - 1) % len(levels)
                elif event.key == pygame.K_RETURN:
                    if selected_level == 0:  # Start Level 1
                        from main import start_game
                        start_game()
                    # Add more levels as needed

    pygame.quit()
    sys.exit()

def show_controls():
    """
    Display the controls information screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Pixel Adventure - Controls")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)

    controls_text = """
    Controls:
    Arrow keys or WASD - Move
    Space - Jump
    Shift - Sprint
    Down Arrow or S - Drop through platform
    Up Arrow or W - Interact with door
    ESC - Quit
    """

    running = True
    while running:
        screen.fill(BG_COLOR)

        title_surface = title_font.render("Controls", True, (255, 255, 255))
        screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 100))

        draw_text(screen, controls_text, (50, 300), font)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    main_menu()

    pygame.quit()
    sys.exit()

def draw_text(surface, text, position, font, color=(255, 255, 255)):
    """
    Draw multi-line text on the screen.

    Parameters:
        surface (pygame.Surface): The surface to draw on.
        text (str): The text to draw.
        position (tuple): The (x, y) position to start drawing.
        font (pygame.font.Font): The font to use.
        color (tuple): The color of the text.
    """
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (position[0], position[1] + i * font.get_height()))

if __name__ == "__main__":
    main_menu()
