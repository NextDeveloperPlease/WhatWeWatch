import pygame as pg

from typing import List
from button import Button
from text_box import TextBox

class Form():
    def __init__(self, x, y, pw, ph, button_color_base = None, button_color_hover = None, text_color = None, button_font = None, submit_text:str = "submit", margin=5, padding=5, debug=False):
        self.x = x
        self.y = y
        self.pw = pw
        self.ph = ph
        self.button_color_base = button_color_base
        self.button_color_hover = button_color_hover
        self.text_color = text_color
        self.button_font = button_font
        self.submit_text = submit_text
        self.children:List[TextBox] = []
        self.debug_flag = debug
        self.x_margin = self.y_margin = margin
        self.x_padding = self.y_padding = padding
        self.submit_button : Button = None
        if self.button_color_base:
            self.default_submit_button_init()

    def add_child(self, child:TextBox):
        x, y = child.get_pos()
        _, ch = child.get_dim()
        prior_x = self.x + self.x_margin
        prior_y = self.y
        prior_height = 0
        if len(self.children) > 0:
            prior_x, prior_y = self.children[-1].get_pos()
            _, prior_height = self.children[-1].get_dim()

        new_x = prior_x + x
        new_y = (prior_y + prior_height) + y + self.y_margin
        child.update_pos(new_x, new_y)
        self.children.append(child)
        self.update_submit_pos(new_y, ch)

    def add_children(self, a_children:List[TextBox]):
        for child in a_children:
            self.add_child(child)

    def add_submit_button(self, button:Button, left:bool = False):
        self.submit_button = button

    def default_submit_button_init(self):
        sx = self.x + 2 * (self.pw//3)
        # _, prior_y = self.children[-1].get_pos()
        # _, prior_height = self.children[-1].get_dim()
        sy = self.y_margin
        self.submit_button = Button(self.submit_text, sx, sy, self.pw//3, 40, self.button_color_base, self.button_color_hover, self.text_color, self.button_font)

    def update_submit_pos(self, prior_y, prior_height):
        ny = (prior_y + prior_height) + self.y_margin
        nx, _ = self.submit_button.get_pos()
        self.submit_button.update_pos(nx, ny)

        # bx, by = button.get_pos()
        # x_dim, _ = button.get_dim()
        # _, prior_y = self.children[-1].get_pos()
        # prior_width, prior_height = self.children[-1].get_dim()
        # px = self.x + x_dim // 3
        # py = (prior_y + prior_height) + by + self.y_margin
        # self.submit_button.update_pos(px, py)

    def draw(self, screen):
        for child in self.children:
            child.draw(screen)

        self.submit_button.draw(screen)

    def package_data(self):
        data = {}
        for child in self.children:
            data[child.get_name()] = child.get_text()
        return data

    def handle_event(self, event):
        for child in self.children:
            child.handle_event(event)

        if self.submit_button:
            if self.submit_button.handle_event(event):
                print("HELLO 2")
                return self.package_data()

        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_RETURN:
        #         print("You pressed enter")
        #         package = self.package_data()
        #         return package