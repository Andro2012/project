 import tkinter as tk
from PIL import Image, ImageTk
from threading import Event, Thread

R = 10
place_x = 0
place_y = 0
X = 1000
Y = 900
register = False
ev = Event()

class Player_class():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{X}x{Y}")

        player_image = Image.open('myphoto.png') #65x99
        player_tk = ImageTk.PhotoImage(player_image)
        self.player = tk.Label(image=player_tk)
        self.player.place(x = place_x, y = place_y)


        self.root.bind('<e>', self.myfunc_e)
        self.root.bind("<E>", self.myfunc_e)
        self.root.bind('<a>', self.move_left)
        self.root.bind('<A>', self.move_left)
        self.root.bind('<d>', self.move_right)
        self.root.bind('<D>', self.move_right)

        self.root.bind('<Escape>', Player.exit) #выход из игры

    def move_left(self):
        pass
    
    def move_right(self):
        pass

    def jump(self):
        pass

    def myfunc_e(event):
        print('В разработке...')
        print(event)  

    def exit(self):
        self.root.destroy()
        print('Игра закрыта')
        

class Settings():
    def __init__(self):
        self.settings = Player_class()

    def start(self):
        self.settings.root.mainloop()


main_settings = Settings()
main_settings.start()



