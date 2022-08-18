import discord
import json
import os
import datetime

HELPCOMMANDS = {
# command/syntax : description
    "checknsfw:[url]" : "Checks the image from url for NSFW content",
    "generatetext:[prompt]" : "Generates a text based on the promt",
    "summarize:[text]" : "Summarizes the provided text",
    "sentiment:[text]" : "Identifies the text's sentiment",
    "generateimage:[prompt]": "Generates an image based on the prompt",
    "finddifference:[url];[url]": "Finds the difference between two images",
    "keywords:[text]": "Picks out key words from the text",
    "upscalewifu:[url]" : "Upscales provided image",
}

HELPRESPONSES = {
    
}


async def displayHelp(message):
    _jf = open("help.json")
    _jd = json.loads(_jf.read())
    _jf.close()
    _embed = discord.Embed()
    _embed.colour = discord.Colour.random()
    for k,v in _jd.items():
        _embed.add_field(name=k,value=v,inline=False)
    await message.channel.send(embed=_embed)
    print(f'{datetime.datetime.now()}|| User {message.author} requested help')
    
    
    
COMMANDS = {
    "bruh help me" : displayHelp,
}