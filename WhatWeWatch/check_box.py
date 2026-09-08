import pygame

class CheckBox():
    def __init__(self, x, y, size, name=None, color=pygame.Color('dodgerblue2')):
        # Input Box Setup
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.name = name

        self.active = False
    
    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return (self.rect.x, self.rect.y)

    def get_dim(self):
        return (self.rect.width, self.rect.height)
    
    def handle_event(self, event):
        # 1. Handle Mouse Click (Focus)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active

    def draw(self, screen):
        # Draw the button rectangle
        c_width = 1
        if self.active:
            c_width = 0
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8, width=int(not self.active))
        # Blit the text on top
        # screen.blit(self.text_surf, self.text_rect)

    def get_text(self):
        return self.active

    def get_name(self):
        return self.name