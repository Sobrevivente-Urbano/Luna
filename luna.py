# -*- coding: latin-1 -*-

import bs4
import sys
import os
import aiml
import time
import requests
from bs4 import BeautifulSoup as soup

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles="/etc/luna/std-startup.xml",
                 commands="load aiml b")


def news(pesquisa):
    pesquisa = pesquisa
    pesquisa = pesquisa.replace("/news ", "")
    pesquisa = pesquisa.replace("/News ", "")
    pesquisa = pesquisa.replace(" ", "%20")

    url = str("https://news.google.com/rss/search?q=" +
              pesquisa + "&hl=pt-BR&gl=BR&ceid=BR:pt-419")

    response = requests.get(url)
    xml = response.content.decode('utf-8')
    soup_page = soup(xml, "xml")
    news_list = soup_page.findAll("item")

    contador = 10
    
    if(len(news_list) > contador):
        for c in range(contador):
            print(" ")
            print(news_list[c].title.text)
    else:
        for c in range(len(news_list)):
            print(" ")
            print(news_list[c].title.text)

os.system("banner")

while True:
    message = input("> ")

    if message == "sair":
        exit()
    elif message[0:4] == "news":
        news(message)
        print()
    elif message[0:4] == "News":
        news(message)
        print()
    elif message[0:5] == "clear":
        os.system("clear")
        os.system("banner")
    elif message[0:3] == "cls":
        os.system("clear")
        os.system("banner")
    else:
        ai_response = kernel.respond(message)
        print(">> " + ai_response)
