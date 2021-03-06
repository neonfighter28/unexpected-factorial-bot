import discord
import re
import math

TOKEN = "insertyourtokenhere"
class DiscordClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        print("-------------------------------------------")
        print("Ready to listen!")

    async def on_message(self, message):   
        if message.author == self.user: 
            return 
        print("  Received a message: [", message.content, "]")
        m = re.search("[\d]*[!]", message.content)
        try:
            f = format(math.factorial(int(m[0][:-1])), "E")
            s = "I didn't expect this factorial! Did you really mean '" + f + "' ?"
        except OverflowError:
            s = "Your factorial made my Integer overflow :/"
        
        if m != None:
            await message.channel.send(s)


if __name__ == "__main__":
    print("\n Unexpected Factorial bot by /u/NeonFighter28")
    print("-------------------------------------------\n")
    print("Logging in on Discord")
    client = DiscordClient()
    client.run(TOKEN)
