import pygame as pg

from form import Form
from button import Button
from text_box import TextBox
from check_box import CheckBox

class FormPopOut():
    def __init__(self, text, x, y, bw, bh, pw, ph, button_color_base, button_color_hover, popout_color, text_box_active_color, text_box_inactive_color, text_color, font:pg.font.Font, button_font:pg.font.Font):
        self.rect = pg.Rect((x+(bw//2))-(pw//2),y+bh+5,pw,ph)
        self.button = Button(text, x, y, bw, bh, button_color_base, button_color_hover, text_color, button_font)
        self.color = popout_color

        # self.save_button = Button("Submit", 0, 0, pw, 40, button_color_base, button_color_hover, text_color, button_font)
        self.movie_title_text_box = TextBox(0, 0, pw-10, 40, font, 'movie', text_box_active_color, text_box_inactive_color)
        self.is_seen_check_box = CheckBox(0, 0, 10, 'is_seen', text_box_inactive_color)
        self.date_text_box = TextBox(0, 0, pw-10, 40, font, 'date', text_box_active_color, text_box_inactive_color)

        self.form = Form((x+(bw//2))-(pw//2), y+bh+5, pw, ph, button_color_base, button_color_hover, text_color, button_font)
        self.form.add_children([self.movie_title_text_box, self.is_seen_check_box, self.date_text_box])
        # self.form.add_submit_button(self.save_button)
        self.active = False

    def toggle_popout_on(self):
        self.active = True

    def toggle_popout_off(self):
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION or (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
            if self.button.handle_event(event):
                self.toggle_popout_on()

            if not (self.rect.collidepoint(event.pos) or self.button.is_hover(event.pos)):
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.toggle_popout_off()

        if self.active:
            return self.form.handle_event(event)

    def draw(self, screen):
        if self.active:
            pg.draw.rect(screen, self.color, self.rect, border_radius=8)
            self.form.draw(screen)
        self.button.draw(screen)