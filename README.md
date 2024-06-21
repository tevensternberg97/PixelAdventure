README
Pixel Adventure
Overview
Pixel Adventure is a 2D platformer game where you navigate through various levels, collect items, avoid or defeat enemies, and reach the door to complete each level. Earn points by collecting items and defeating enemies, aiming for the highest score possible.

Controls
Move: Arrow keys or WASD
Jump: Spacebar
Sprint: Shift
Drop through platform: Down Arrow or S
Interact with door: Up Arrow or W
Quit: ESC
Installation Instructions
Prerequisites
Python 3.8 or later
Pygame 2.0 or later
Steps
Download and Unzip

Download the PixelAdventure.zip file.
Extract it to your desired location.
Set Up a Virtual Environment

Open a terminal or command prompt in the extracted PixelAdventure folder.
Run the following command to create a virtual environment:
sh
Copy code
python -m venv venv
Activate the Virtual Environment

Windows:
sh
Copy code
.\venv\Scripts\activate
MacOS/Linux:
sh
Copy code
source venv/bin/activate
Install Dependencies

With the virtual environment activated, run the following command to install the required dependencies:
sh
Copy code
pip install pygame
Run the Game

With the dependencies installed, start the game by running main.py:
sh
Copy code
python src/main.py
Folder Structure
css
Copy code
PixelAdventure/
├── assets/
│   ├── images/
│   │   └── character.png
│   └── sounds/
├── src/
│   ├── controls.py
│   ├── enemy.py
│   ├── laser.py
│   ├── level.py
│   ├── main.py
│   ├── menu.py
│   ├── player.py
│   ├── settings.py
│   └── highscore.py
└── README.md
Additional Notes
Ensure the character.png file is located in the assets/images folder.
High scores are stored in a file named highscores.json in the root directory.
If you encounter any issues, ensure that your Python and Pygame installations are up-to-date.
Enjoy playing Pixel Adventure!
