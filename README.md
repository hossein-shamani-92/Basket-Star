# Basket & Star

A simple arcade game built with Python and Pygame where the player controls a basket to catch falling stars while avoiding bombs.

## Overview

The game places the player in a space-themed environment with falling stars and bombs.

The player controls a basket using the Left and Right Arrow keys. Catching stars increases the score, while hitting bombs or missing falling stars decreases it.

The game also includes score-based level progression and a game-over condition.

## Features

* Basket movement using keyboard controls
* Falling stars
* Falling bombs
* Collision detection
* Score tracking
* Score penalties for bombs and missed stars
* Randomized positions for falling objects
* Increasing difficulty based on the score
* Level-up messages
* Game-over state
* Space-themed background
* Custom game icon and assets

## Controls

| Key         | Action            |
| ----------- | ----------------- |
| Left Arrow  | Move basket left  |
| Right Arrow | Move basket right |

## Gameplay

The player controls the basket horizontally across the screen.

Stars continuously fall from the top of the screen. Catching a star increases the score by `1`.

Bombs also fall from the top of the screen. If the basket collides with a bomb, the score decreases by `1`.

Missing a star also decreases the score.

The falling objects are repositioned to random locations after being collected, missed, or collided with.

## Scoring

* Catching a star: `+1`
* Hitting a bomb: `-1`
* Missing a star: `-1`

## Assets

```text
space.jpg
bomb.png
basket_green.png
star.png
```

## Requirements

* Python 3.x
* Pygame

## Installation

```bash
pip install pygame
```

## Run

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file if necessary.

## Project Structure

```text
Basket-And-Star/
│
├── main.py
├── space.jpg
├── bomb.png
├── basket_green.png
└── star.png
```

## Technologies

* Python
* Pygame

## Concepts Demonstrated

* Game loops
* Keyboard input
* Collision detection
* Random number generation
* Object movement
* Score management
* Lists
* Conditional logic
* Game-state handling
* Image rendering
