# coding: UTF-8
from time import sleep
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from uagame import Window


def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()


def create_window():
    window = Window('Hacking', 400, 500)
    window.set_bg_color('black')
    return window


def create_dot(color, radius, center, velocity):
    dot = Dot()
    dot.color_string = color
    dot.radius = radius
    dot.center = center
    dot.velocity = velocity
    return dot


def create_game(window):
    game = Game()
    game.big_dot = create_dot('blue', 40, [200,100], [2,1])
    game.clock = Clock()
    game.close_selected = False
    game.frame_rate = 90
    game.small_dot = create_dot('red', 30, [50,75], [1,2])
    game.window = window

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


def draw_game(game):
    game.window.clear()
    draw_dot(game.window, game.small_dot)
    draw_dot(game.window, game.big_dot)
    game.window.update()


def update_game(game):
    move_dot(game.window, game.small_dot)
    move_dot(game.window, game.big_dot)
    sleep(0.01)
    game.clock.tick(game.frame_rate)


def draw_dot(window, dot):
    surface = window.get_surface()
    color = Color(dot.color_string)
    draw_circle(surface, color, dot.center, dot.radius)


def move_dot(window, dot):
    size = (window.get_width(), window.get_height())
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
