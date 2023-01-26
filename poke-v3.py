# coding: UTF-8
from time import sleep
from random import randint
from pygame import Color
from pygame import MOUSEBUTTONUP
from pygame import QUIT
from pygame import KEYDOWN
from pygame.time import Clock
from pygame.time import get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from pygame import K_p
from pygame import K_q
from uagame import Window


def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()


def create_window():
    window = Window('Hacking', 500, 400)
    window.set_font_name('ariel')
    window.set_bg_color('black')
    window.set_font_name('couriernew')
    return window


def create_dot(window, color, radius, center, velocity):
    dot = Dot()
    dot.color_string = color
    dot.radius = radius
    dot.center = center
    dot.velocity = velocity
    dot.window = window
    return dot


def create_game(window):
    game = Game()
    game.big_dot = create_dot(window, 'blue', 40, [200,100], [2,1])
    game.clock = Clock()
    game.close_selected = False
    game.frame_rate = 90
    game.score = 0
    game.small_dot = create_dot(window, 'red', 30, [50,75], [1,2])
    game.window = window
    
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)

    return game


def play_game(game):
    while not game.close_selected:
        handle_events(game)
        draw_game(game)
        update_game(game)


def handle_events(game):
    event_list = get_events()
    for event in event_list:
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            randomize_dots_center(game)
        elif event.type == KEYDOWN:
            if event.key == K_p:
                randomize_dots_center(game)
            if event.key == K_q:
                game.close_selected = True


def draw_game(game):
    game.window.clear()
    draw_scoreboard(game)
    draw_dot(game.window, game.small_dot)
    draw_dot(game.window, game.big_dot)
    game.window.update()


def update_game(game):
    move_dot(game.small_dot)
    move_dot(game.big_dot)
    sleep(0.01)
    game.clock.tick(game.frame_rate)
    played_seconds = get_ticks() // 1000
    game.score = played_seconds


def draw_scoreboard(game):
    game.window.set_font_size(32)
    game.window.set_font_color('white')
    game.window.draw_string(f'Scoreboard {game.score}', 0, 0)


def draw_dot(window, dot):
    surface = window.get_surface()
    color = Color(dot.color_string)
    draw_circle(surface, color, dot.center, dot.radius)


def randomize_dots_center(game):
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)


def randomize_dot(dot):
    random_x = randint(dot.radius, dot.window.get_width() - dot.radius)
    random_y = randint(dot.radius, dot.window.get_height() - dot.radius)
    dot.center = [random_x, random_y] 


def move_dot(dot):
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        dot.center[index] = dot.center[index] + dot.velocity[index]
        if (dot.center[index] <= dot.radius) or (dot.center[index] + dot.radius >= size[index]):
            dot.velocity[index] = - dot.velocity[index]


class Game:
    # An object in this class represents a compete game
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_dot

    pass


class Dot:
    pass


main()
