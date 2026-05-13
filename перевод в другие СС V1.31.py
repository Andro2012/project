#подсказки:
    #Выбор СС(S)
    #Ввод числа(d)

import os
import platform

    #функции

    #очищение экрана
def clear():

    #определение ОС
    os_name = platform.system()
    print(os_name)

    #если ОС Windows
    if os_name == "Windows":
        os.system("cls")

    #если ОС Linux
    elif os_name =="Linux":
        os.system("clear")

    #если ОС Mac os
    elif os_name == "Darwin":
        os.system("clear")

    else:
        print("Возникла ошибка!!! обратитесь в ТП!!!")
    print("КОНСОЛЬ ОЧИЩЕНА ")


#ЗАПУСК ЦИКЛА
while True :
    s = input("Выберите СС (2,8,10,16): ")



    #Десятичная СС(10)
    if s == "10" :
        try:
            d = int(input("Введите ваше число: "))
            bin10 = bin(d)[2:]
            oct10 = oct(d)[2:]
            hex10 = hex(d)[2:]
            print("Ваше число в десятичной : " , d)
            print("Число в двоичной : " , str(bin10))    
            print("Число в восьмеричной : " , str(oct10))
            print("Число в шестнадцатиричной : " , str(hex10))
            print("")
        except ValueError:
            print("Введено не число!")
            
    #Двоичная СС(2)
    elif s == "2" :
        try:
            d = int(input("Введите ваше число: "))
            int2 = int(str(d) , 2)
            oct2 = oct(int2)[2:]
            hex2 = hex(int2)[2:]
            print("Ваше число в двоичной : " , d)  
            print("Число в десятичной: " , str(int2))
            print("Число в восьмеричной : " , str(oct2))
            print("Число в шестнадцатиричной : " , str(hex2))
            print("")
        except ValueError:
            print("Введено не число!")
    
    #Восьмеричная СС(8)
    elif s == "8" :
        try:
            d = int(input("Введите ваше число: "))
            int8 = int(str(d) , 8)
            bin8 = bin(int8)[2:]
            hex8 = hex(int8)[2:]
            print("Ваше число в восьмеричной :" , d)  
            print("Число в десятичной: " , str(int8))
            print("Число в двоичной : " , str(bin8))
            print("Число в шестнадцатиричной : " , str(hex8))
            print("")
        except ValueError:
            print("Введено не число!")

    #16-ричная СС(16)
    elif s == "16" :
        try:
            d = input("Введите ваше число: ")
            int16 = int(str(d) , 16)
            bin16 = bin(int16)[2:]
            oct16 = oct(int16)[2:]
            print("Ваше число в 16-ричной : " , d)  
            print("Число в десятичной : " , str(int16))
            print("Число в двоичной : " , str(bin16))
            print("Число в восьмеричной : " , str(oct16))
            print("")
        except ValueError:
            print("Введено не число!")

    #очищение экрана
    elif s  == "clear":
       clear()

    #тык
    elif s == "":
        print("тык")
        
    #для разработчика:(secret)

    #Версия(version)
    elif s == "version" or s == "ver":
        while True :
            print("V1.31")
            exit = input("Выйти? (да/нет): ")
            if exit == "да":
                break
            elif exit == "нет":
              pass
            elif exit == "":
                print("тык")
            elif exit == "clear":
                clear()
                break
            else :
                print("Такой команды не существует!!!")
    else:
        print("Попробуйте ещё раз!")