**A simple GUI of the Tic-Tac-Toe game.**

_This script uses the pygame library in order to make the interface._

Explanation of some pieces of the code:

**game_board** (var):
This variable keeps the track of the input provided by the user in the form of keys bound to the graphical board in the GUI.

**board_coordinates** (const):
This is a list of tuple where each tuple represents the (x, y) of the centre of each box in the graphical board. This makes sure that each avatar is being placed at a pre-decided place.

**play()**:

_Major function of the game where all the complex stuff happens._

_Params: key_list(list) : Provides the list of the status of all keys on the keyboard._

First if the game hasn't been started yet i.e. the move_count (var) is zero, it will blit every necessary graphic on the display.

Next part of the function works on the logic that the sum of the key_list should be 1 (this shows that at a point of time only one key has been pressed on the keyboard, which is required in this game). It also checks that the previous value of sum should be zero as the pygame.key module works on millisecond and humans don't react that fast which results in capturing the press event of a single key multiple times that might break our game.
If no error has been occurred in this process then move_count increments by 1 and this one move of the respective player.

**Gameloop (while running):**

On every iteration it checks for the keys that were pressed.
Also checks for the status of each button. Each button has been assigned a code. This helps us keep track of the dynamic behaviour of our button. If a button has been clicked for the first time, .isClicked() returns true and the button_open (var) changes its value accordingly. 