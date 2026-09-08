import pygame

class Button:
    def __init__(self, text, x, y, width, height, base_color, hover_color, text_color, font:pygame.font, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        self.hover_color = hover_color
        self.current_color = base_color
        self.action = action
        
        # Pre-render text surface
        self.text_surf = font.render(self.text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def get_pos(self):
        return (self.rect.x, self.rect.y)
    
    def get_dim(self):
        return (self.rect.width, self.rect.height)

    def draw(self, surface):
        # Draw the button rectangle
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=8)
        # Blit the text on top
        surface.blit(self.text_surf, self.text_rect)

    def is_hover(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def check_hover(self, mouse_pos):
        # Change color if mouse is hovering over the button
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.base_color

    def handle_event(self, event):
        # Trigger action if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                print("HELLO")
                if self.action:
                    self.action()
                return True
            return False
