import discord
client = discord.Client() #Brings the bot online somehow

@client.event 
async def on_message(message):

    #Checks for 'hello' in any casing 
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
         await message.channel.send("Howdy hoe")

    #Check for message author via Discord ID
    if str(message.author) == "Skillz#6565":
        await message.channel.send("Nice ass :)")
    

client.run("Token")


