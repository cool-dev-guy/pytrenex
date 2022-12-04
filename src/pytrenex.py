from browser import document
class pygame:
    def __init__(self):
        print("started pygame -version")
        self.window_h = "300px"
        self.window_w = "500px"
    def init(self):
        print('hi')

class Display(pygame):
    def __init__(self):
        self.renderer = document["renderer"]
    def init(self):
        self.init_status = False
    def set_mode(self,size=(0,0), flags=0, depth=0, display=0, vsync=0):
        self.window_h = f'{size[0]}px'
        self.window_w = f'{size[1]}px'
        self.renderer.attrs["width"] = self.window_w
        self.renderer.attrs["height"] = self.window_h
        print(self.window_h,self.window_w)
    def get_init(self):
        return self.init_status

def init():
    global display
    display = Display()
    display.init()
