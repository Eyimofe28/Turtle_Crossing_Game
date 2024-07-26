# Turtle Crossing Game

## Project Overview

This project is a Python implementation of a Turtle Crossing game using the Turtle graphics library. The objective is to move the turtle from the bottom to the top of the screen while avoiding moving cars. The game progresses in levels, with cars increasing in speed and number as levels advance.

## Features

- **Turtle Movement**: Control the turtle using the `Up` arrow or `w` key to move it forward.
- **Car Movement**: Cars move from right to left across the screen, with their speed and frequency increasing as levels progress.
- **Score Keeping**: The scoreboard displays the current level and updates as the player progresses.
- **Game Over**: The game ends when the turtle collides with a car, displaying a game over message.

## Dependencies

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)

## File Descriptions

### `main.py`

The main file containing the game setup, main loop, and collision detection logic.

### `crossing_cars.py`

A module defining the `Car` class, which handles car creation, movement, and speed adjustments.

### `crossing_scoreboard.py`

A module defining the `ScoreBoard` class, which handles the display and update of the current level and game over message.

### `turtle_movement.py`

A module defining the `Object` class, which handles the turtle's movement.

## Getting Started

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Run the Project**: Execute the `main.py` file to start the game.
   ```bash
   python main.py
   ```

## Code Explanation

### Main Game Setup (`main.py`)

The main game file sets up the game environment, creates the turtle, cars, and scoreboard, and contains the main game loop.

### Car Class (`crossing_cars.py`)

The `Car` class handles the creation, movement, and speed adjustments of the cars.

### ScoreBoard Class (`crossing_scoreboard.py`)

The `ScoreBoard` class handles the display and update of the current level and the game over message.

### Object Class (`turtle_movement.py`)

The `Object` class handles the movement of the turtle.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code follows the project’s coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This comprehensive readme should help you understand the structure and functionality of my Turtle Crossing game application. If you have any questions or need further assistance, please feel free to ask :)
