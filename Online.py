from telethon import TelegramClient, events, sync
from telethon import TelegramClient, sync
from telethon import events
import requests
from time import sleep
c = requests.session()
def css():
	api_id =  17888302 
	api_hash =  661d599c6c35f03cff84d80c65a06e0c 
	client = TelegramClient( session , api_id, api_hash)
	client.start()
	while True:
	     client.send_message( heroshema111 , hi  )
	     sleep(30)
	  #   return
	#client.disconnect()

css()
