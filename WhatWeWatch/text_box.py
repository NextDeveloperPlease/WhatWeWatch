import pygame

class TextBox():
    def __init__(self, x, y, width, height, font:pygame.font.Font, name=None, active_color=pygame.Color('dodgerblue2'), inactive_color=pygame.Color('lightskyblue3')):
        # Input Box Setup
        self.input_rect = pygame.Rect(x, y, width, height)
        self.color_active = active_color
        self.color_inactive = inactive_color
        self.color = self.color_inactive
        self.font = font
        self.name = name

        self.input_text = ''
        self.lines = [['']]
        self.active = False
        self.max_width = width - 10
        self.offset = 0
        # self.max_width = 230
        # self.input_rect.w = 240
        # self.input_rect.h = 40
    
    def update_pos(self, x, y):
        self.input_rect.x = x
        self.input_rect.y = y

    def get_pos(self):
        return (self.input_rect.x, self.input_rect.y)
    
    def get_dim(self):
        return (self.input_rect.width, self.input_rect.height)

    def handle_event(self, event):
        # 1. Handle Mouse Click (Focus)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
                # pygame.key.start_text_input()  # Optional: triggers IME/virtual keyboards
            else:
                self.active = False
                self.color = self.color_inactive
                # pygame.key.stop_text_input()
        # 2. Handle Text Input (Only when active)
        if self.active:
            if event.type == pygame.TEXTINPUT:
                self.input_text += event.text
                fw,fh = self.font.size(self.input_text)
                tw,th = self.font.size(event.text)
                if fw > self.max_width:
                    self.offset = fw - self.max_width
                # line_words = self.lines[-1]
                # fw,fh = self.font.size(' '.join(line_words) + event.text)
                # if fw > self.max_width:
                #     self.lines.append([])
                # if event.text == ' ':
                #     line_words.append('')
                # else:
                #     line_words[-1] += event.text
                # self.lines[-1] = line_words
                
            # 3. Handle System Keys (Backspace, Return)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                    # last_word = self.lines[-1][-1]
                    # if last_word:
                    #     last_word[:-1]
                    #     self.lines[-1][-1] = last_word
                # elif event.key == pygame.K_RETURN:
                    # print(f"Submitted text: {self.input_text}")
                    # self.input_text = ''  # Clear on submit
        # print(self.lines)

    def draw(self, screen):
        # Render text surface
        fw,hw = self.font.size(self.input_text)
        # rendered_text = self.input_text
        # while fw > self.max_width:
        #     rendered_text = rendered_text[1:]
        #     fw,_ = self.font.size(rendered_text)
        # text_surface = self.font.render(rendered_text, True, (255, 255, 255))
        # start = 0
        # if fw // 2 >= 120:
        #     start = fw // 2
        render_area = pygame.Rect(self.offset, 0, fw, hw)
        text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        
        # Auto-resize input box if text overflows
        # self.input_rect.w = min(max(240, text_surface.get_width() + 10), 600)
        
        # Blit text and box onto screen
        screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 2), area=render_area)
        pygame.draw.rect(screen, self.color, self.input_rect, 2)

    def get_text(self):
        return self.input_text

    def get_name(self):
        return self.name