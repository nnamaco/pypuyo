# pypuyo
A pip package to make Puyo-Puyo-ish games.
```python
>>> import pypuyo as ppy
>>> game = ppy.start(width=3, height=3, frames_to_fall=1)
>>> game.update()
>>> game.update()
>>> print(game.get())
[[None, "Yellow", None]
 [None, None, None]
 [None, None, None]]
>>> game.update()
>>> print(game.get())
[[None, "Yellow", None]
 [None, "Blue", None]
 [None, None, None]]
```
# Installation
### pip
`$ python3 -m pip install pupuyo`
# Cloning repo
`$ git clone https://github.com/nnamaco/pypuyo/`
# Examples
- A GUI example -> https://github.com/nnamaco/pypuyo-example
- A shell CLI example -> https://github.com/nnamaco/pypuyo-example-cli<br>
  (Still making)
# Usage
## Quickstart
1. Create game instance by:
```python
game = pypuyo.Game()
```
2. Go to next frame by:
```python
game.update()
```
3. Get array by:
```python
game.get()
```
## Documentation
### Methods
|method      |desciption                    |arguments                                        |
|----        |----                          |----                                             | 
|`start`     |Returns new `Game` instance.    |`width`: Width of the game.<br>`height`: Height of the game.<br>`types`: Array of possible puyos to fall.<br>`frames_to_fall`: Frames that take puyos to fall.|
### Class `Game`
|method      |desciption                    |arguments                                        |
|----        |----                          |----                                             | 
|`move_right`|Move falling puyos right.     |-                                                |
|`move_left` |Move falling puyos right.     |-                                                |
|`spin_right`|Move falling puyos right.     |-                                                |
|`spin_left` |Move falling puyos right.     |-                                                |
|`is_over`   |Returns boolean `is_gameover`.|-                                                |
|`update`    |Update game to next frame.    |-                                                |
|`get`       |Get game as array.            |-                                                |
# License
This software is released under the MIT License, see LICENSE.
