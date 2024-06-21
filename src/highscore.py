import os
import json

HIGHSCORE_FILE = "highscores.json"

def load_highscores():
    """
    Load high scores from a file.
    """
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_highscores(highscores):
    """
    Save high scores to a file.
    """
    with open(HIGHSCORE_FILE, "w") as file:
        json.dump(highscores, file, indent=4)

def update_highscore(level, score):
    """
    Update the high score for a given level.

    Parameters:
        level (str): The level identifier.
        score (int): The new score to compare against the high score.
    """
    highscores = load_highscores()
    if level not in highscores or score > highscores[level]:
        highscores[level] = score
        save_highscores(highscores)
