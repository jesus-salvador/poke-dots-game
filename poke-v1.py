# coding: UTF-8
from time import sleep
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from uagame import Window

def main():
    window = create_window()
    clock = Clock()
    
    small_color = 'red'
    small_radius = 30
    small_center = [50,75]
    small_velocity = [1,2]
    
    big_color = 'blue'
    big_radius = 40
    big_center = [200,100]
    big_velocity = [2,1]
    
    play_game(window, small_color, small_center, small_radius, small_velocity, big_color, big_center, big_radius, big_velocity, clock)
    window.close()


def create_window():
    window = Window('Hacking', 400, 500)
    window.set_bg_color('black')
    return window


def play_game(window, small_color, small_center, small_radius, small_velocity, big_color, big_center, big_radius, big_velocity, clock):
    close_selected = False
    while not close_selected:
        close_selected = handle_events()
        draw_game(window, small_color, small_center, small_radius, big_color, big_center, big_radius)
        update_game(window, small_center, small_radius, small_velocity, big_center, big_radius, big_velocity, clock)


def handle_events():
    closed = False
    event_list = get_events()
    for event in event_list:
        if event.type == QUIT:
            closed = True
    return closed


def draw_game(window, small_color, small_center, small_radius, big_color, big_center, big_radius):
    window.clear()
    draw_dot(window, small_color, small_center, small_radius)
    draw_dot(window, big_color, big_center, big_radius)
    window.update()

def update_game(window, small_center, small_radius, small_velocity, big_center, big_radius, big_velocity, clock):
    frame_rate = 90
    move_dot(window, small_center, small_radius, small_velocity)
    move_dot(window, big_center, big_radius, big_velocity)
    sleep(0.01)
    clock.tick(frame_rate)

def draw_dot(window, color_string, center, radius):
    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)

def move_dot(window, center, radius, velocity):
    size = (window.get_width(), window.get_height())
    for index in range(0, 2):
        center[index] = center[index] + velocity[index]
        if (center[index] <= radius) or (center[index] + radius >= size[index]):
            velocity[index] = - velocity[index]
main()
