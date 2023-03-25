import discord

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    print(message.content)
    #if message.channel.id == 1087310970700967947 and message.attachments:
    
    print (message.attachments)



    for attachment in message.attachments:
        print("\n here")
        if attachment.filename.lower().endswith(('.png', '.jpeg', '.jpg', '.gif')):
            print(f"{message.author} uploaded an image in {message.channel}:\n{attachment.url}")



client.run('MTA4ODk0MDYyODk3ODcxMjY4Ng.GfHuS4.N8UNttdj5fRKKAdFSx1_y6PFrrHi0pXIjeSOZU')
