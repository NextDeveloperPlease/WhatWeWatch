import pygame as pg

from typing import List
from button import Button
from text_box import TextBox

class Form():
    def __init__(self, x, y, margin=5, padding=5, debug=False):
        self.x = x
        self.y = y
        self.children:List[TextBox] = []
        self.submit_button:Button = None
        self.debug_flag = debug
        self.x_margin = self.y_margin = margin
        self.x_padding = self.y_padding = padding

    def add_child(self, child:TextBox):
        x, y = child.get_pos()
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

    def add_children(self, a_children:List[TextBox]):
        for child in a_children:
            self.add_child(child)

    def add_submit_button(self, button:Button):
        self.submit_button = button

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