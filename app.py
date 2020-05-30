# ------------------Tic-Tac-Toe------------------
# ---------Created by: Shourya Gupta-------------
# -----------------28/05/2020--------------------


# importing necessary modules
import pygame
from packages.button import Button
from packages.player import Player

pygame.init()
pygame.mixer.music.load('resources/The_Crows_Did_It.mp3')

# creating a game display window
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('resources/game.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Tic-Tac-Toe')

# a game board which will be updated and will keep track of the game progress
game_board = [' '] * 9

# coordinates of the centre of each box in the tic tac toe board image
board_coordinates = [(265, 256), (401, 256), (535, 256),
                     (265, 393), (401, 393), (535, 393),
                     (265, 530), (401, 530), (535, 530)]

# FPS at which the game will run
FPS = 30
intro = []
clock = pygame.time.Clock()

# loading the image sequence of the intro video
# appending them into a list of images in chronological order
for i in range(173):
    if i < 10:
        path = 'resources/intro_frames/welcome_Trim0' + '00' + str(i) + '.png'
    elif 10 <= i <= 99:
        path = 'resources/intro_frames/welcome_Trim0' + '0' + str(i) + '.png'
    else:
        path = 'resources/intro_frames/welcome_Trim0' + str(i) + '.png'

    intro.append(pygame.image.load(path))


# function to run the intro video
def intro_run():
    for j in range(173):
        screen.blit(intro[j], (0, 0))
        clock.tick(FPS)
        pygame.display.update()


intro_run()

# loading necessary images from the resources folder

bg = pygame.image.load('resources/background.png')
opening_grid = pygame.image.load('resources/FRONT_BOARD.png')
play_img = pygame.image.load('resources/play.png')
help_img = pygame.image.load('resources/help.png')
quit_img = pygame.image.load('resources/quit.png')
cross = pygame.image.load('resources/cross.png')
circle = pygame.image.load('resources/circle.png')
back_img = pygame.image.load('resources/back.png')
play_again_img = pygame.image.load('resources/play_again.png')
play_hover = pygame.image.load('resources/play_hover.png')
help_hover = pygame.image.load('resources/help_hover.png')
quit_hover = pygame.image.load('resources/quit_hover.png')
play_again_hover = pygame.image.load('resources/play_again_hover.png')
back_hover = pygame.image.load('resources/back_hover.png')
help_land = pygame.image.load('resources/help_landing_page.png')
quit_land = pygame.image.load('resources/quit_page.png')
board = pygame.image.load('resources/TicTacToe.png')
error_cover_img = pygame.image.load('resources/error_cover.png')
turn_prompt_cover = pygame.image.load('resources/turn_prompt_cover.png')
x_score_cover = pygame.image.load('resources/x_score_cover.png')
o_score_cover = pygame.image.load('resources/o_score_cover.png')

screen.blit(bg, (0, 0))

# creating button objects using Button class
play_button = Button(play_img, play_hover, 330, 15, (255, 0, 0))
help_button = Button(help_img, help_hover, 328, 73, (255, 0, 0))
quit_button_1 = Button(quit_img, quit_hover, 328, 131, (255, 0, 0))
quit_button_2 = Button(quit_img, quit_hover, 328, 408, (255, 0, 0))
back_button = Button(back_img, back_hover, 328, 500, (255, 0, 0))
play_again_button = Button(play_again_img, play_again_hover, 328, 350, (255, 0, 0))
button_open = 0
soft_red = (206, 141, 102)

# move_count tracks the progress of the game
move_count = 0
cross_w, cross_h = cross.get_rect().size
circle_w, circle_h = circle.get_rect().size


# this draws the main menu display on the screen
def open_draw():
    screen.blit(opening_grid, (200, 190))
    play_button.draw_button(screen)
    help_button.draw_button(screen)
    quit_button_1.draw_button(screen)


# defines the help button function
def help_landing():
    screen.blit(help_land, (0, 0))
    back_button.draw_button(screen)
    pygame.display.update()


# defines the quit button function
def quit_landing():
    pygame.mixer.music.fadeout(30)
    screen.blit(quit_land, (0, 0))
    clock.tick(FPS)
    global running
    running = False


# this variable is used to perform tasks only one time in the infinite game loop
# tasks such as incrementation of the score of a player
one_time_only = 1


# the main game function which handles data and does various game related tasks
def play(key_list):
    global move_count
    global game_board
    global previous_val_of_sum
    global button_open
    global one_time_only

    # this snippet executes only until any player has not made any move
    if move_count == 0:
        # changing the one time only variable to its default value so that the next execution runs like the first one
        one_time_only = 1
        # displaying graphics for the play function
        screen.blit(bg, (0, 0))
        screen.blit(board, (200, 190))
        message_display(p1.get_name(), (10, 20), 50)
        message_display(p1.get_avatar(), (10, 75))
        message_display(p1.get_score(), (10, 110))
        message_display(p2.get_name(), (604, 20), 50)
        message_display(p2.get_avatar(), (661, 75))
        message_display(p2.get_score(), (685, 110))
        pygame.draw.rect(screen, soft_red, (270, 65, 265, 60))
        message_display(f'{p1.name}\'s turn', (280, 75), 40, (255, 255, 255))
    elif move_count % 2 == 0:
        pygame.draw.rect(screen, soft_red, (270, 65, 265, 60))
        message_display(f'{p1.name}\'s turn', (280, 75), 40, (255, 255, 255))
    else:
        pygame.draw.rect(screen, soft_red, (270, 65, 265, 60))
        message_display(f'{p2.name}\'s turn', (280, 75), 40, (255, 255, 255))

    # game begins from here
    # this snippet works on the keys list and checks whether the sum of keys has changed from 0 to 1
    if move_count < 9:
        if previous_val_of_sum == 0 and sum(key_list) == 1:
            screen.blit(error_cover_img, (200, 146))
            if move_count % 2 == 0:
                board_fill(key_list, p1)
                if not game_board_updated:
                    if error_code == 0:
                        full_box_error()
                    elif error_code == 1:
                        wrong_key_error()
                else:
                    move_count += 1
            else:
                board_fill(key_list, p2)
                if not game_board_updated:
                    if error_code == 0:
                        full_box_error()
                    elif error_code == 1:
                        wrong_key_error()
                else:
                    move_count += 1

    # minimum 5 moves are required for any player to win
    # here we calculate which player won and display the graphics post game completion
    if move_count >= 5:
        if move_count % 2 != 0:
            if check_for_win():
                screen.blit(turn_prompt_cover, (265, 60))
                if one_time_only:
                    pygame.draw.rect(screen, (254, 95, 85), (200, 190, 400, 400))
                    message_display('PLAYER X WINS!!', (225, 220), 50, (255, 255, 255))
                    p1.score += 1
                    screen.blit(x_score_cover, (0, 109))

                play_again_button.draw_button(screen)
                quit_button_2.draw_button(screen)
                message_display(p1.get_score(), (10, 110))
                move_count = 9
                one_time_only = 0
                if play_again_button.isClicked():
                    button_open = 1
                    move_count = 0
                    game_board = [' '] * 9
                if quit_button_2.isClicked():
                    quit_landing()
        else:
            if check_for_win():
                screen.blit(turn_prompt_cover, (265, 60))
                if one_time_only:
                    pygame.draw.rect(screen, (254, 95, 85), (200, 190, 400, 400))
                    message_display('PLAYER O WINS!!', (225, 220), 50, (255, 255, 255))
                    p2.score += 1
                    screen.blit(o_score_cover, (655, 109))

                play_again_button.draw_button(screen)
                quit_button_2.draw_button(screen)
                message_display(p2.get_score(), (685, 110))
                move_count = 9
                one_time_only = 0
                if play_again_button.isClicked():
                    button_open = 1
                    move_count = 0
                    game_board = [' '] * 9
                if quit_button_2.isClicked():
                    quit_landing()

    # here we check if the game ended in a draw
    # if yes, we display the necessary graphics and buttons
    if move_count == 9 and not check_for_win():
        screen.blit(turn_prompt_cover, (265, 60))
        if one_time_only:
            pygame.draw.rect(screen, (254, 95, 85), (200, 190, 400, 400))
        message_display('GAME DRAWN!', (243, 220), 50, (255, 255, 255))
        play_again_button.draw_button(screen)
        quit_button_2.draw_button(screen)
        one_time_only = 0
        if play_again_button.isClicked():
            button_open = 1
            move_count = 0
            game_board = [' '] * 9
        if quit_button_2.isClicked():
            quit_landing()


# defines the function of the back button
def back_button_landing():
    screen.blit(bg, (0, 0))
    global button_open
    button_open = 0


# encapsulates the text functions of pygame
def message_display(message, pos, size=30, color=soft_red):
    text = pygame.font.Font('fonts/TCB_____.TTF', size)
    text_surf = text.render(message, True, color)
    screen.blit(text_surf, pos)


# returns the coordinates on the display where either X or O needs to placed
def avatar_placing(position):
    avatar_coordinates = []
    for k in range(len(board_coordinates)):
        avatar_x = board_coordinates[k][0] - cross_w // 2
        avatar_y = board_coordinates[k][1] - cross_h // 2
        temp = (avatar_x, avatar_y)
        avatar_coordinates.append(temp)

    return avatar_coordinates[position]


# Shows an error message if the player tries to fill an already full box
def full_box_error():
    pygame.draw.rect(screen, (255, 0, 0), (250, 155, 300, 30))
    message_display('Already full. Choose another box!', (255, 160), 20, (255, 255, 255))


# Shows an error message if the player presses the wrong key
def wrong_key_error():
    pygame.draw.rect(screen, (255, 0, 0), (250, 155, 300, 30))
    message_display('You pressed a wrong key!', (290, 160), 20, (255, 255, 255))


# full_box_error is 0
# wrong_key_error is 1
error_code = 0

# this is used to check whether the game board is updated or not
game_board_updated = 0


# used to fill the boxes in the board as the game progresses
# changes the error_code variable according to the error
# if the game_board is updated, changes the respective variable to 1
def board_fill(key_pressed, player_active):
    global game_board
    global error_code
    global game_board_updated

    if key_pressed[pygame.K_KP7]:
        if game_board[0] == ' ':
            game_board[0] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(0))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP8]:
        if game_board[1] == ' ':
            game_board[1] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(1))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP9]:
        if game_board[2] == ' ':
            game_board[2] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(2))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP4]:
        if game_board[3] == ' ':
            game_board[3] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(3))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP5]:
        if game_board[4] == ' ':
            game_board[4] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(4))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP6]:
        if game_board[5] == ' ':
            game_board[5] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(5))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP1]:
        if game_board[6] == ' ':
            game_board[6] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(6))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP2]:
        if game_board[7] == ' ':
            game_board[7] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(7))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    elif key_pressed[pygame.K_KP3]:
        if game_board[8] == ' ':
            game_board[8] = player_active.avatar
            screen.blit(player_active.avatar_img, avatar_placing(8))
            error_code = 0
            game_board_updated = 1
        else:
            game_board_updated = 0
    else:
        error_code = 1
        game_board_updated = 0


# used to determine the win status of a player
def check_for_win():
    if (game_board[0] == game_board[1] == game_board[2] and game_board[1] != ' ') or \
            (game_board[3] == game_board[4] == game_board[5] and game_board[4] != ' ') or \
            (game_board[6] == game_board[7] == game_board[8] and game_board[7] != ' ') or \
            (game_board[0] == game_board[3] == game_board[6] and game_board[3] != ' ') or \
            (game_board[1] == game_board[4] == game_board[7] and game_board[4] != ' ') or \
            (game_board[2] == game_board[5] == game_board[8] and game_board[5] != ' ') or \
            (game_board[0] == game_board[4] == game_board[8] and game_board[4] != ' ') or \
            (game_board[2] == game_board[4] == game_board[6] and game_board[4] != ' '):
        return True

    return False


p1 = Player('X', cross)
p2 = Player('O', circle)

running = True
previous_val_of_sum = 0

pygame.mixer.music.play(-1)
# every button has its code
# 1 = play button
# 2 = help button
# 3 = quit button
# 0 = open_draw function, which means no button has been pressed from the main menu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if play_button.isClicked() or button_open == 1:
        play(keys)
        button_open = 1
    elif (help_button.isClicked() or button_open == 2) and not back_button.isClicked():
        help_landing()
        button_open = 2
    elif quit_button_1.isClicked() or button_open == 3:
        quit_landing()
        button_open = 3
    elif back_button.isClicked():
        back_button_landing()
    elif not button_open:
        open_draw()
    previous_val_of_sum = sum(keys)
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
