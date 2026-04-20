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



        self.root = tk.Tk()
        self.root.geometry(f"{X}x{Y}+200+50")
        self.root.resizable(False, False)

        player_image = Image.open('myphoto.png') #65x99
        player_im_tk = ImageTk.PhotoImage(player_image)
        self.player = tk.Label(image=player_im_tk)
        self.player.place(x = place_x, y = place_y)


        self.root.bind('<e>', self.myfunc_e)
        self.root.bind("<E>", self.myfunc_e)
        self.root.bind('<a>', self.move_left)
        self.root.bind('<A>', self.move_left)
        self.root.bind('<d>', self.move_right)
        self.root.bind('<D>', self.move_right)

        self.root.bind('<space>', self.jump)

        self.root.bind('<Escape>', self.exit) #выход из игры

    def move_left(self, event):
        self.x -= R


        print('left')
    
    def move_right(self, event):
        print('right')

    def jump(self,event):
        print('jump')

    def place(self, event):
        self.player.place(x = place_x, y = place_y)

    

    def myfunc_e(self, event):
        print('Инвентарь в разработке...')

    def exit(self, event):
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
