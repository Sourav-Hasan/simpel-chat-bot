#coding: utf-8
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot=ChatBot('Test')
bot.set_trainer(ListTrainer)
for _file in os.listdir('files'):
     chats=open('files/'+_file,'r',encoding='utf-8').readlines()
     bot.train(chats)
while True:
     request=input('You : ')
     response=bot.get_response(request)
     if response.confidence>=.50:
          print('Bot : ', response)
     else:
          print('আপনার কথা বুঝিনাই ভাই')


