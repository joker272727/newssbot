import time
#import eventlet
import requests
import logging
import telebot
from time import sleep
from bs4 import BeautifulSoup

URL_SPY = 'http://quote-spy.com/'
FILENAME_VK = 'last_known_id.txt'
#BASE_POST_URL = 'https://vk.com/wall-39270586_'

BOT_TOKEN = '549277681:AAGz364DCYncVsIPKIjW0_jG8qpElQK9Rp8'
CHANNEL_NAME = '@f_news_c'

bot = telebot.TeleBot(BOT_TOKEN)

def get_data(LAST_MES):
    response = requests.get(URL_SPY)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find(id="NewsPanel1").find_all("tr")
    L_MES = content_div[len(content_div) - 1]
    if L_MES != LAST_MES:
        LAST_MES = L_MES
        return LAST_MES
    else:
        return "NULL"


def send_new_posts(item):
    news = item.find_all("td")[1].find("a")
    #bot.send_message(CHANNEL_NAME, "[" + news.text + "](" + news.get("href") + ")" )
    bot.send_message(CHANNEL_NAME, news.get("href"))
    return


if __name__ == '__main__':
    while True:
        LAST_MES = " "
        mes = get_data(LAST_MES)
        if mes != "NULL":
            send_new_posts(mes)
        time.sleep(60 * 4)




