import tkinter as tk
from PIL import Image, ImageTk
from threading import Event, Thread

R = 10
place_x = 500
place_y = 450
X = 1000
Y = 900
register = False
ev = Event()

class Player_class():
    def __init__(self, x = place_x, y = place_y):
        self.x = x
        self.y = y

        self.is_jumping = False

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width = 500, height = 400)
        self.root.geometry(f"{X}x{Y}+200+50")
        self.root.resizable(False, False)

        self.player_image = Image.open('myphoto.png') #65x99
        self.player_im_tk = ImageTk.PhotoImage(self.player_image)
        self.player = tk.Label(image = self.player_im_tk)
        self.player.place(x = place_x, y = place_y)


        self.root.bind('<e>', self.myfunc_e)
        self.root.bind("<E>", self.myfunc_e)
        self.root.bind('<a>', self.move_left)
        self.root.bind('<A>', self.move_left)
        self.root.bind('<d>', self.move_right)
        self.root.bind('<D>', self.move_right)

        self.root.bind('<space>', self.jump)

        self.root.bind('<Escape>', self.exit) #выход из игры

    def move_left(self, event = None):
        if self.x <= R:
            self.x = 0
            self.place()
        else:
            self.x -= R
            self.place()

        print('left')
    
    def move_right(self, event = None):
        if self.x >= X - R:
            self.x = X - R
            self.place()
        else:
            self.x += R
            self.place()


        print('right')

    def jump(self,event = None):

        if self.is_jumping:
            return
        
        else:
            self.jump_frames = 40

            print("UP")
            for i in range(self.jump_frames):
                self.root.after(100, self.jump_up)
                
            print("FALL")
            for i in range(self.jump_frames):
                self.root.after(100, self.jump_falling)

            print('jump')

    def jump_up(self, event = None):
        if self.is_jumping:
            return
        
        else:
            if self.jump_frames > 0:
                self.y -= 1
                self.place()
                self.root.after(20, self.jump_up)
                self.jump_frames -= 1
            else:
                self.jump_frames = 40
                self.jump_falling()

    def jump_falling(self, event = None):
        if self.jump_frames > 0:
            self.y += 1
            self.place()
            self.root.after(20, self.jump_falling)
            self.jump_frames -= 1
        else:
            self.is_jumping = False


    def place(self, event = None):
        self.player.place(x = self.x, y = self.y)

    

    def myfunc_e(self, event = None):
        print('Инвентарь в разработке...')

    def exit(self, event = None):
        self.root.destroy()
        print('Игра закрыта')
        

class Settings():
    def __init__(self, admin_panel = False):
        self.settings = Player_class()

    def start(self):
        self.settings.root.mainloop()




if __name__ == "__main__":
    main_settings = Settings()
    main_settings.start()
