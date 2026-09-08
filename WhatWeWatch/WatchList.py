import sys
import pygame as pg

from WatchListStorage import WatchList
from button import Button
from text_box import TextBox
from check_box import CheckBox
from form import Form
from form_popout import FormPopOut

class Game:
    def __init__(self):
        # 1. Initialize Pygame modules
        pg.init()
        
        # 2. Configure display settings
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.watch_list = WatchList("watch_list.csv")

        # Colors (R, G, B)
        self.BG_COLOR = (30, 30, 40)
        self.BUTTON_COLOR = (75,75,75)
        self.HOVER_COLOR = (100, 92, 85)
        self.TEXT_COLOR = (255, 255, 255)

        # Pop-out colors
        self.POPOUT_COLOR = (50,50,50)
        self.ACTIVE_COLOR = (90,90,90)
        self.INACTIVE_COLOR = (65,65,65)

        # Fonts
        self.INPUT_FONT = pg.font.SysFont("Arial", 32)
        self.FONT = pg.font.SysFont("Arial", 20)

        # self.save_button = Button("Save", 600, 400, 100, 100, self.BUTTON_COLOR, self.HOVER_COLOR, self.TEXT_COLOR, self.FONT, self.watch_list.save)
        # self.save_button = Button("Save", 600, 400, 100, 100, self.BUTTON_COLOR, self.HOVER_COLOR, self.TEXT_COLOR, self.FONT)
        # self.movie_title_text_box = TextBox(0, 0, 240, 40, self.FONT, 'movie')
        # # self.is_seen_text_box = TextBox(50, 100, 240, 40, self.FONT, 'is_seen')
        # self.is_seen_check_box = CheckBox(0, 0, 10, 'is_seen')
        # self.date_text_box = TextBox(0, 0, 240, 40, self.FONT, 'date')

        # self.form = Form(50,50)
        # self.form.add_children([self.movie_title_text_box, self.is_seen_check_box, self.date_text_box])
        # self.form.add_submit_button(self.save_button)
        self.form_popout = FormPopOut('Add', 200, 100, 40, 40, 200, 200, self.BUTTON_COLOR, self.HOVER_COLOR, self.POPOUT_COLOR, self.ACTIVE_COLOR, self.INACTIVE_COLOR, self.TEXT_COLOR, self.INPUT_FONT, self.FONT)

        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("My Pygame Window")
        
        # 3. Setup clock for framing and timing
        self.clock = pg.time.Clock()
        self.is_running = True

    def handle_events(self):
        """Process keyboard, mouse, and window events."""
        for event in pg.event.get():
            # self.movie_title_text_box.handle_event(event)
            # movie_title_text = self.movie_title_text_box.get_text()
            
            # self.is_seen_text_box.handle_event(event)
            # is_seen_text = self.is_seen_text_box.get_text()
            
            # self.date_text_box.handle_event(event)
            # date_text = self.date_text_box.get_text()
            # movie_info = {
            #     'movie':movie_title_text,
            #     'is_seen':is_seen_text,
            #     'date':date_text
            # }

            # self.save_button.handle_event(event)
            # form_data = self.form.handle_event(event)
            form_data = self.form_popout.handle_event(event)
            if form_data:
                self.watch_list.add_to_watchlist(form_data)
                self.watch_list.print_list()

            if event.type == pg.QUIT:
                self.is_running = False
            
            if event.type == pg.KEYDOWN:
                # if event.key == pg.K_RETURN:
                #     print("You pressed enter")
                    # self.watch_list.add_to_watchlist(movie_info)
                if event.key == pg.K_ESCAPE:
                    self.is_running = False

    def update(self, dt):
        """Update game logic, physics, and positions here."""
        # dt is delta time (seconds since last frame)
        pass

    def draw(self):
        """Render elements onto the screen."""
        # Clear screen with a background color (RGB)
        self.screen.fill((30, 30, 30))
        
        # --- Draw your game elements here ---
        # self.movie_title_text_box.draw(self.screen)
        # self.is_seen_text_box.draw(self.screen)
        # self.date_text_box.draw(self.screen)
        # self.save_button.draw(self.screen)
        # self.form.draw(self.screen)
        self.form_popout.draw(self.screen)
        
        # Flip the display buffer to show changes
        pg.display.flip()

    def run(self):
        """Main game loop."""
        # watch_list = WatchList("watch_list.csv")
        # watch_list.print_list()
        # watch_list.add_to_watchlist("Iron Man 2", False, '8/16/26')
        # watch_list.print_list()
        # watch_list.save_watchlist("watch_list.csv")
        while self.is_running:
            # Maintain frame rate and calculate delta time
            # tick(FPS) returns elapsed milliseconds since last call
            dt = self.clock.tick(self.FPS) / 1000.0 
            
            self.handle_events()
            self.update(dt)
            self.draw()
            
        # Clean up window and exit safely
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
