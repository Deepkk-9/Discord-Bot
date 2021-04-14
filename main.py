import discord
import os
import requests
import json
import urllib
from keep_alive import keep_alive

client = discord.Client()

def get_meme():
  response = urllib.request.urlopen("https://zenquotes.io/api/random")

  json_data = json.loads(response.read())
  # meme = json_data[0] ['q'] + [" -"] + json_data[0] ['a']
  inspire = "_" + json_data[0]['q']  + "_ - " + json_data[0]['a']
  return (inspire)

#Function to return random meme images URL
def random_meme():
  url =  "https://some-random-api.ml/meme"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  path = data["image"]
  return path

#Function to return random jokes 
def random_joke():
  url = "https://some-random-api.ml/joke"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  joke = data["joke"]
  return joke


@client.event
async def on_ready():
  print('We have logged in as {0.user}' .format(client))

@client.event
async def on_message(message):

  msg = message.content

  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('>>> Hello! , Want to enjoy some memes or jokes ?, write $meme or $joke to enjoy some of them!')

  if message.content.startswith('$inspire'):
    inspire = get_meme()
    await message.channel.send(">>> " + inspire)

#Condition to return random meme
  if msg.startswith('$meme'):
    meme = random_meme()
    await message.channel.send(meme)

#Condition to return random jokes
  if msg.startswith('$joke'):
    joke = random_joke()
    await message.channel.send(">>> " + joke)

keep_alive()

client.run(os.getenv('TOKEN'))
 
