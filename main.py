from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.core.window import Window


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')



class FishesGame(Widget):
    
    def __init__(self):
        
        super(FishesGame, self).__init__()

        self.fish0x = 100
        self.fish0y = 200
        self.fish0pos = [self.fish0x, self.fish0y]


class FishesApp(App):
    
    def __init__(self):
        
        super(FishesApp, self).__init__()
        
        def proportSize(width):
            
            return (width, width * 0.58)
        
        self.fish0size = proportSize(400)
        self.fish0x = 100
        self.fish0y = 200
        self.fish0pos = [self.fish0x, self.fish0y]

        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)
        
    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        
        if keycode[1] == 'left':
            
            self.fish0x -= 10
            print("left", self.fish0pos[0])

        
        elif keycode[1] == 'right':
            
            self.fish0x += 10
            print("right", self.fish0pos[0])
        
        else:
            
            return False
        
        return True

    

    def build(self):
        
        root = FishesGame()
        return root
        


if __name__ == '__main__':
    FishesApp().run()