# coding: UTF-8
from time import sleep
from math import sqrt
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


class Dot:
    def __init__(self, window, color, radius, center, velocity):
        self._center = center
        self._color_string = color
        self._radius = radius
        self._velocity = velocity
        self._window = window
    
    def randomize(self):
        random_x = randint(self._radius, self._window.get_width() - self._radius)
        random_y = randint(self._radius, self._window.get_height() - self._radius)
        self._center = [random_x, random_y]
    
    def draw(self):
        surface = self._window.get_surface()
        draw_circle(surface, self.get_color(), self._center, self._radius)
    
    def move(self):
        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            self._center[index] = self._center[index] + self._velocity[index]
            if (self._center[index] <= self._radius) or (self._center[index] + self._radius >= size[index]):
                self._velocity[index] = - self._velocity[index]
    
    def get_color(self):
        return Color(self._color_string)
    
    def get_color_name(self):
        return self._color_string


class Game:
    def __init__(self):
        self.window = Window('Hacking', 500, 400)
        self._adjust_window()
        self._clock = Clock()
        self._close_selected = False
        self._small_dot = Dot(self.window, 'red', 30, [50,75], [1,2])
        self._big_dot = Dot(self.window, 'blue', 40, [200,100], [2,1])
        self._small_dot.randomize()
        self._big_dot.randomize()        
        self._frame_rate = 90
        self._score = 0
        self._is_game_over = False

    def _adjust_window(self):
        self.window.set_font_name('ariel')
        self.window.set_bg_color('black')
        self.window.set_font_name('couriernew')
    
    def play(self):
        while not self._close_selected:
            self._handle_events()
            self._draw()
            self._update()
        
        self.window.close()

    def _handle_events(self):
        event_list = get_events()
        for event in event_list:
            if event.type == QUIT:
                self._close_selected = True
            else:
                self._handle_play_events(event)
    
    def _handle_play_events(self, event):
        if self._is_game_over:
            return
        
        if event.type == MOUSEBUTTONUP:
            self._randomize_dots_position()
        elif event.type == KEYDOWN:
            if event.key == K_p:
                self._randomize_dots_position()
            if event.key == K_q:
                self._close_selected = True

    def _randomize_dots_position(self):
        self._small_dot.randomize()
        self._big_dot.randomize()

    def _draw(self):
        self.window.clear()
        self._draw_scoreboard()
        self._small_dot.draw()
        self._big_dot.draw()
        if self._is_game_over:
            self._draw_game_over()
        self.window.update()
    
    def _draw_game_over(self):
        game_over_message = 'Game Over'
        game_over_y = self.window.get_height() - self.window.get_font_height()
        original_font_color = self.window.get_font_color()
        original_bg_color = self.window.get_bg_color()
        self.window.set_font_color(self._small_dot.get_color_name())
        self.window.set_bg_color(self._big_dot.get_color())
        self.window.draw_string(game_over_message, 0, game_over_y)
        
        self.window.set_font_color(original_font_color)
        self.window.set_bg_color(original_bg_color)
    
    def _draw_scoreboard(self):
        self.window.set_font_size(32)
        self.window.set_font_color('white')
        self.window.draw_string(f'Scoreboard {self._score}', 0, 0)

    def _update(self):
        if not self._is_game_over:
            self._small_dot.move()
            self._big_dot.move()
            played_seconds = get_ticks() // 1000
            self._score = played_seconds

        sleep(0.01)
        self._clock.tick(self._frame_rate)

        if self.isGameOver():
            self._is_game_over = True
        
    def isGameOver(self):
        # when dots collide is game over
        if self.get_distance_between_dots() <= self._small_dot._radius + self._big_dot._radius:
            return True
        
        return False
    
    def get_distance_between_dots(self):
        x1 = self._small_dot._center[0]
        y1 = self._small_dot._center[1]
        x2 = self._big_dot._center[0]
        y2 = self._big_dot._center[1]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    game = Game()
    game.play()

main()
