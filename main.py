from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')



class FishesGame(Widget):
    pass


class FishesApp(App):
    def __init__(self):
        super(FishesApp, self).__init__()
        def proportSize(width):
            
            return (width, width * .58)
        
        self.fish0size = proportSize(400)

    # fish0size = [300, ]
    # fish0size.append(fish0size[0] * .58)
    
    def build(self):
        
        root = FishesGame()
        return root
        


if __name__ == '__main__':
    FishesApp().run()