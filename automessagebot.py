import discord
import time




bot_token = "bot_token"
kanal_id = "channel_id"
mesaj = "automatic_message"
gecikme_suresi = 15  # delay from message

intents = discord.Intents.default()  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot connected!")
    kanal = client.get_channel(kanal_id)
    while True:
        await kanal.send(mesaj)
        time.sleep(gecikme_suresi)

client.run(bot_token)