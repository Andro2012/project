import tkinter as tk
from PIL import Image, ImageTk
from threading import Event, Thread
import time
import os


#Размеры карты
X = 1000
Y = 900

#Регистрация(в разработке)
register = False

R = 15 #Длина ходьбы(x)
JUMP_R = 20 #Длина прыжка(y)

ev = Event()
root = tk.Tk()



#Запрещаем изменять размер окна
root.resizable(False, False)

#Задаем размеры карты
root.geometry(f"{X}x{Y}") 



#Загрузка изображения
try:
    player_image = Image.open('myphoto.png') #65x99
    player_tk = ImageTk.PhotoImage(player_image)
except FileNotFoundError:
    print('Файл игрока не найден!')
    print('Проверьте целостность папки')

#Получение размеров картинки игрока
player_width, player_height = player_image.size
print(f'Размеры фото игрока: x:{player_width}, y:{player_height}')

class Player():
    def __init__(self, pos_x = 100, pos_y = 100):

        #Позиция игрока
        self.x = pos_x
        self.y = pos_y

        #Создаем изображение игрока
        self.player = tk.Label(image=player_tk)
        self.player.place(x = self.x, y = self.y)

        #Получение размеров экрана
        root.after(1000, self.screen_info)

    #Вправо
    def move_right(self, event = None):
        if self.x >= X - player_width:
            self.x = X - player_width
        else:
            self.x += R
        Player.place()
        os.system('cls')
        print(f'x: {self.x}')
        print(f'y: {self.y}')
        
    #Присед(в разработке)
    def move_prised(self, event = None):
        pass
    
    #Влево
    def move_left(self, event = None):
        if self.x <= R:
            self.x = 0
        else:
            self.x -= R
        Player.place()
        os.system('cls')
        print(f'x: {self.x}')
        print(f'y: {self.y}')


    #Прыжок
    def jump(self, event = None):
        self.limit_height = self.y + JUMP_R
        Player.up(self)
        Player.fall(self)

    def up(self, event = None):
        if self.limit_height > self.y:
            for i in range(JUMP_R):
                self.y -= 1
                Player.place()
                Player.coords()
                root.after(100, Player.jump)
        else:
            pass



    def fall(self, event = None):
        if self.y >= self.limit_height:
            for j in range(JUMP_R):
                self.y += 1
                Player.place()
                Player.coords()
                root.after(100, Player.jump)
        else:
            pass
            
    #Обновление позиции игрока
    def place(self, event = None):
        self.player.place(x = self.x, y = self.y)

    #определение размеров экрана
    def screen_info(self, event = None):
        self.screen_width = root.winfo_width()
        self.screen_height = root.winfo_height()
        print(f"screen width: {self.screen_width}")
        print(f"screen height: {self.screen_height}")


    def coords(self, event = None):
        print(f'x: {self.x}')
        print(f'y: {self.y}')

# class Move():
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y

#     def jump(self):
#         # if self.y <= R:
#         #     player.place(x = self.x, y = 0)
#         #     print('jump!!!')
#         # else:
#         #     player.place(x = self.x, y = self.y)
#         #     print('jump!!!')
#         pass

#     def right(self):
#         pass

#     def prised(self):
#         print('prisel')

#     def left(self):
#         print('left')


my_pl = Player()

def func_exit(event):
    root.destroy()
    print('Окно закрыто')

def pos(event):
    print(event)

root.bind('<a>', my_pl.move_left) #влево
root.bind('<A>', my_pl.move_left) #влево
root.bind('<s>', my_pl.move_prised) #присесть
root.bind('<S>', my_pl.move_prised) #присесть
root.bind('<d>', my_pl.move_right) #вправо
root.bind('<D>', my_pl.move_right) #вправо
root.bind('<p>', pos)
root.bind('<space>', my_pl.jump) #прыжок
root.bind('<F1>', my_pl.coords) #Координаты игрока
root.bind('<F2>', my_pl.screen_info)

root.bind('<Escape>', func_exit) #выход из игры


root.mainloop()