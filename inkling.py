#!/usr/bin/python3

import discord
import asyncio
import time

client = discord.Client()
can_send = True
start_time = time.time() 

@client.event
@asyncio.coroutine
def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")

@client.event
@asyncio.coroutine
def on_message(message):
	global can_send
	global start_time
	delay = 600
	if message.content.startswith("woomy"):
		elapsed_time = time.time() - start_time
		if elapsed_time >= delay:
			can_send = True
		if can_send:
			yield from client.send_message(message.channel, "@here: " + message.author.name + " wants to play!")
			can_send = False
			start_time = time.time()

client.run("token")
