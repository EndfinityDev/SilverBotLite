import os
import discord
import random
    
async def hi_response(message):
    print(f'{message.author}: {message.content}')
    await message.channel.send(random.choice(["Hi","hi","Howdy","Henlo","aboba"]))

async def testattachment(message, args=None):
    for a in message.attachments:
        print(f'Type: {a.content_type}, URL: {str(a)}')


ADDITIONAL_RESPONSES = {
        'hi' : hi_response
    }
    
COMMANDS = {
            
            }