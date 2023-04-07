import discord
import re



####################################################################
# Config here
# All channel ids that the bot should look at here
# Seperate with comma
channel_id = [1087310970700967947]
# replace this
#
# When it shows my token, then you are fired
token = "token here"




# For regex
url_pattern = re.compile(r'https?://\S+')



# Idk what this does, but it only worked when I copy pasted it
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    # When msg is from ourselves
    if message.author == client.user:
        return

    # print(message.content)
    # Check if channel is general
    if message.channel.id != 1087310970700967947:
        return
    
    ############################
    # IMAGE CHECKING
    ############################

    has_image = False

    # Check for attachments
    if message.attachments:

        # Check if msg has an img attached
        for attachment in message.attachments:
            if attachment.filename.lower().endswith(('.png', '.jpeg', '.jpg', '.gif')):
                has_image = True
            
                               
    # Check for Image link
    if url_pattern.search(message.content):
        url = url_pattern.search(message.content).group(0)
        # Check if the URL ends with a valid image file extension
        if any(url.endswith(extension) for extension in ('.png', '.jpg', '.jpeg', '.gif')):
            has_image = True



    if has_image:
        # Has image

        # Debug
        print(f"{message.author} uploaded an image in {message.channel}")
        
        # Ban message to server
        embedVar = discord.Embed(description=f"***{message.author} was banned. Reason: meme in {client.get_channel(message.channel.id)}***", color=0x43b582)
        await message.channel.send(embed=embedVar)

        # Ban message to DM
        embedVar = discord.Embed(title=f"You have been banned from {message.guild.name} for posting a meme in {client.get_channel(message.channel.id)}", color=0x43b582)
        await message.author.send(embed=embedVar)



client.run(token)
