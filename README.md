# Pypuyo
A pip package to make Puyo-Puyo-ish games.<br>
https://pypi.org/project/pypuyo/
# Examples
- A GUI example(https://github.com/nnamaco/pypuyo-example)
- A shell CLI example(https://github.com/nnamaco/pypuyo-example-cli)
# Usage
## Quickstart
1. Create game instance by:
```
game = pypuyo.Game()
```
2. Go to next frame by:
```
game.update()
```
3. Get array by:
```
game.get()
```
## Documentation
### Classes
`Game`:
|method      |desciption                    |arguments                                        |
|----        |----                          |----                                             | 
|`__init__`  |Constructor.                  |`width`: Width of the game.<br>`height`: Height of the game.<br>`types`: Array of possible puyos to fall.<br>`frames_to_fall`: Frames that take puyos to fall.|
|`move_right`|Move falling puyos right.     |-                                                |
|`move_left` |Move falling puyos right.     |-                                                |
|`spin_right`|Move falling puyos right.     |-                                                |
|`spin_left` |Move falling puyos right.     |-                                                |
|`is_over`   |Returns boolean `is_gameover`.|-                                                |
|`update`    |Update game to next frame.    |-                                                |
|`get`       |Get game as array.            |-                                                |
# License
This software is released under the MIT License, see LICENSE.
