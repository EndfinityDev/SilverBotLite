import os
import discord
import json
import requests
import random
import datetime

import responses
import help

TOKEN =     #Discord bot token
DEEPAI_TOKEN = 

SERVER_ID = 
BOT_CHANNEL_ID = 
GENERAL_ID = 
COMMON_ROLE_ID = 
ADMIN_ROLE_ID = 
QUOTES_CHANNEL_ID = 



client = discord.Client()


@client.event
async def on_ready():
    global SERVER
    global BOT_CHANNEL
    global GENERAL_CHANNEL
    global COMMON_ROLE
    global ADMIN_ROLE
    global QUOTES_CHANNEL
    global RP_CHANNEL
    global rpm
    global ARGCOMMANDS
    print(f'{client.user} is ready!')
    print('Server ID: ' + str(SERVER_ID))
    print('Debug Channel ID: ' + str(BOT_CHANNEL_ID))
    SERVER = client.get_guild(SERVER_ID)
    BOT_CHANNEL = client.get_channel(BOT_CHANNEL_ID)
    GENERAL_CHANNEL = client.get_channel(GENERAL_ID)
    COMMON_ROLE = SERVER.get_role(COMMON_ROLE_ID)
    ADMIN_ROLE = SERVER.get_role(ADMIN_ROLE_ID)
    QUOTES_CHANNEL = client.get_channel(QUOTES_CHANNEL_ID)
    print(str(SERVER))
    print(str(BOT_CHANNEL))
    print(str(GENERAL_CHANNEL))
    print(str(COMMON_ROLE))
    print(str(ADMIN_ROLE))
    print(str(QUOTES_CHANNEL))

    
@client.event
async def on_message_delete(message):
    print(f'User {message.author} deleted a message: {message.content}')
    await BOT_CHANNEL.send(f'Channel: \#{str(message.channel)}; User {message.author}\'s message was deleted: {message.content}')
    
@client.event
async def on_message_edit(before, after):
    if (before.content == after.content): return
    await BOT_CHANNEL.send(f'Channel: \#{str(after.channel)}; User {after.author} edited message:\n Before:\n{before.content}\n After:\n{after.content}')

@client.event
async def on_member_join(member):
    global COMMON_ROLE
    global GENERAL_CHANNEL
    await GENERAL_CHANNEL.send(f'@{member.name} has joined us!')
    await GENERAL_CHANNEL.send(f'{member.name} joined the server')
    await member.add_roles(COMMON_ROLE)
    
    
async def check_nsfw(message, args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        data={
            'image': args.strip(),
        },
        headers={'api-key': DEEPAI_TOKEN}
)
        print(r.json())
        await message.channel.send(r.json())
    except: 
        print("Error Processing check_nsfw request")
        await message.channel.send('An error occurred processing the request')
        
async def moderate(message, args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/content-moderation",
        data={
            'image': args.strip(),
        },
        headers={'api-key': DEEPAI_TOKEN}
)
        print(r.json())
        await message.channel.send(r.json())
    except: 
        print("Error Processing moderation request")
        await message.channel.send('An error occurred processing the request')
        
async def generate_text(message,args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': args,
        },
        headers={'api-key': DEEPAI_TOKEN}
        )
        print(r.json())
        await message.channel.send(r.json()['output'])
    except: 
        print("Error Processing text generation request")
        await message.channel.send('An error occurred processing the request')
        
async def summarize(message,args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/summarization",
        data={
            'text': args,
        },
        headers={'api-key': DEEPAI_TOKEN}
        )
        print(r.json())
        await message.channel.send(r.json()['output'])
    except: 
        print("Error Processing summary generation request")
        await message.channel.send('An error occurred processing the request')
        
async def sentiment(message,args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/sentiment-analysis",
        data={
            'text': args,
        },
        headers={'api-key': DEEPAI_TOKEN}
        )
        print(r.json())
        await message.channel.send(r.json()['output'])
    except: 
        print("Error Processing sentiment generation request")
        await message.channel.send('An error occurred processing the request')
        
async def generate_image(message,args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': args,
        },
        headers={'api-key': DEEPAI_TOKEN}
        )
        print(r.json())
        await message.channel.send(r.json()['output_url'])
    except: 
        print("Error Processing image generation request")
        await message.channel.send('An error occurred processing the request')
        
async def image_difference(message,args):
    args = args.split(';')
    print(args[0])
    print(args[1])
    try:
        r = requests.post(
        "https://api.deepai.org/api/image-similarity",
        data={
            'image1': args[0].strip(),
            'image2': args[1].strip(),
        },
        headers={'api-key': DEEPAI_TOKEN}
        )
        print(r.json())
        await message.channel.send(r.json()['output'])
    except: 
        print("Error Processing difference generation request")
        await message.channel.send('An error occurred processing the request')
        
async def keywords(message,args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/text-tagging",
        data={
            'text': args,
        },
        headers={'api-key': DEEPAI_TOKEN}
        )
        print(r.json())
        await message.channel.send(r.json()['output'])
    except: 
        print("Error Processing keyword generation request")
        await message.channel.send('An error occurred processing the request')
        
        
async def fillimage(message, args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/highres-inpainting",
        data={
            'image': args.strip(),
        },
        headers={'api-key': DEEPAI_TOKEN}
)
        print(r.json())
        await message.channel.send(r.json()['output_url'])
    except: 
        print("Error Processing image filling request")
        await message.channel.send('An error occurred processing the request')
        
async def caption(message, args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/neuraltalk",
        data={
            'image': args.strip(),
        },
        headers={'api-key': DEEPAI_TOKEN}
)
        print(r.json())
        await message.channel.send(r.json()['output'])
    except: 
        print("Error processing image caption request")
        await message.channel.send('An error occurred processing the request')
        
async def upscalewifu(message, args):
    print(args)
    try:
        r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        data={
            'image': args.strip(),
        },
        headers={'api-key': DEEPAI_TOKEN}
)
        print(r.json())
        await message.channel.send(r.json()['output_url'])
    except: 
        print("Error upscaling wifu image")
        await message.channel.send('An error occurred processing the request')
        
        
async def send_message(message,args):
    if (message.author.roles.count(ADMIN_ROLE)==0): 
        await message.channel.send('You\'re not my dad!')
        return
    _msg=args.split(';')
    _channel = _msg[0]
    _msg=_msg[1]
    await message.delete()
    print(f'Bot message: Channel: {str(client.get_channel(int(_channel)))}; User: {message.author}; Message: {_msg}')
    await client.get_channel(int(_channel)).send(_msg)
    
async def update_responses(message):
    if (message.author.roles.count(ADMIN_ROLE)==0): 
        await message.channel.send('You\'re not an administrator!')
        return
    import responses
    global RESPONSES
    RESPONSES.update(responses.ADDITIONAL_RESPONSES)
    print('UPDATING RESPONSES')
    await message.channel.send('Updating responses')
    
async def save_quote(message):
    for att in message.attachments:
        if (att.content_type == 'image/png' or att.content_type == 'image/jpeg'):
            _jf = open('saved_quotes.json','r')
            _jt = _jf.read()
            _jf.close()
            _jd = json.loads(_jt)
            _jd["quotes"].append(att.url)
            _jt = json.dumps(_jd)
            _jf = open('saved_quotes.json','w')
            _jf.write(_jt)
            print('Added quote: '+att.url)
            _jf.close()
            
async def print_quote(message):
    _jf = open('saved_quotes.json','r')
    _jt = _jf.read()
    _jf.close()
    _jd = json.loads(_jt)
    await message.channel.send(random.choice(_jd["quotes"]))
    
async def remove_quote(message,args):
    if (message.author.roles.count(ADMIN_ROLE)==0): 
        await message.channel.send('You\'re not my dad!')
        return
    _jf = open('saved_quotes.json','r')
    _jt = _jf.read()
    _jf.close()
    _jd = json.loads(_jt)
    _jd["quotes"].remove(args.strip())
    _jt = json.dumps(_jd)
    _jf = open('saved_quotes.json','w')
    _jf.write(_jt)
    _jf.close()
    await message.channel.send('Quote removed!')
    print("Removed: " + args.strip())
    
    
RESPONSES = {
                'update responses' : update_responses,
                'printquote' : print_quote
            }    
            
ARGCOMMANDS = {
                'checknsfw:' : check_nsfw,
                'moderate:'  : moderate,
                'generatetext:' : generate_text,
                'summarize:' : summarize,
                'sentiment:' : sentiment,
                'generateimage:' : generate_image,
                'finddifference:':image_difference,
                'keywords:' : keywords,
                'fillimage:': fillimage,
                'caption:' : caption,
                'upscalewifu:' : upscalewifu,
                'sendmessage:': send_message,
                'removequote:' : remove_quote,
            }
    
@client.event
async def on_message(message):
    if message.author == client.user: return
    
    if message.channel == QUOTES_CHANNEL:
        await save_quote(message)
    
    for keyword,function in RESPONSES.items():
        if (message.content.lower() == keyword): 
            async with message.channel.typing():
                await function(message)
            return
        

    
    for k, v in ARGCOMMANDS.items():
        if (message.content.lower().find(k)==0):
            _args = message.content.replace(k,'')
            async with message.channel.typing():
                await v(message,_args)
            return
            
    _json = open("commands.json",'r')
    _jsonData = json.loads(_json.read())
    _json.close()
    for k,v in _jsonData.items():
        if (message.content.lower() == k): 
            if (type(v)==list or type(v)==tuple):
                await message.channel.send(random.choice(v))
                return
            await message.channel.send(v)
            return

def main():
    RESPONSES.update(responses.ADDITIONAL_RESPONSES)
    ARGCOMMANDS.update(responses.COMMANDS)
    RESPONSES.update(help.COMMANDS)
    client.run(TOKEN)
    







if __name__ == "__main__": main()
