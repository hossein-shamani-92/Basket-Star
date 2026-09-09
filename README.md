# Basket & Star

A simple arcade game built with Python and Pygame where the player controls a basket to catch falling stars while avoiding bombs.

## Description

Basket & Star is a 2D arcade game developed with Python and Pygame.

The player controls a basket horizontally using the Left and Right Arrow keys. Stars and bombs fall from the top of the screen. Catching stars increases the score, while hitting bombs or missing stars decreases it.

The game ends when the score reaches `-10`.

## Technologies

* Python
* Pygame

## Features

* Horizontal basket movement
* Falling stars
* Falling bombs
* Collision detection
* Score tracking
* Randomized object positions
* Score increase when catching stars
* Score decrease when hitting bombs
* Score decrease when missing stars
* Score-based level-up messages
* Game-over condition
* Space-themed background
* Custom game icon

## How It Works

The game starts with:

* 3 stars
* 3 bombs
* A basket controlled by the player
* An initial score of `0`

### Stars

Stars fall from the top of the screen.

When the basket catches a star:

```text
Score +1
```

The star is then moved back to the top at a random horizontal position.

If a star falls below the screen:

```text
Score -1
```

The star is repositioned at a random horizontal position.

### Bombs

Bombs also fall from the top of the screen.

When a bomb collides with the basket:

```text
Score -1
```

The bomb is then repositioned at the top of the screen.

### Level-Up Event

When the score reaches certain values, the game displays a `level up!` message.

### Game Over

When the score reaches:

```text
-10
```

the game displays the game-over message and stops the game.

## Controls

| Key         | Action                |
| ----------- | --------------------- |
| Left Arrow  | Move the basket left  |
| Right Arrow | Move the basket right |

## Scoring

| Action       | Score |
| ------------ | ----: |
| Catch a star |    +1 |
| Hit a bomb   |    -1 |
| Miss a star  |    -1 |

## Challenges

Some of the main challenges in this project were:

* Handling multiple falling objects
* Detecting collisions between the basket and objects
* Managing the score
* Randomizing object positions
* Handling game-over conditions
* Managing score-based events
* Working with Pygame images and rendering

## What I Learned

Through this project, I practiced:

* Creating a game loop with Pygame
* Handling keyboard input
* Detecting collisions
* Working with images
* Generating random positions
* Managing game state
* Using lists to manage multiple objects
* Implementing score systems
* Creating basic game-over and level-up events

## Status

Completed as a Python and Pygame practice project.

## Future Improvements

* Add sound effects
* Add a start menu
* Add a restart option
* Improve the level system
* Implement consistent difficulty progression
* Add a high-score system
* Improve the game-over screen
* Add more visual effects
* Display the player's name in the game

## Requirements

* Python 3.x
* Pygame

## Installation

```bash
pip install pygame
```

## How to Run

```bash
python main.py
```

Before running the game, make sure the required image files are in the same directory as `main.py`.

## Project Structure

```text
Basket-Star/
│
├── main.py
├── space.jpg
├── bomb.png
├── basket_green.png
├── star.png
└── README.md
```
