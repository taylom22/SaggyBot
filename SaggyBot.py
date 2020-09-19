import discord
import os
import html
import requests
import random
import re
from bs4 import BeautifulSoup

TOKEN = 'NTM5OTM0MjA3MjM3OTQ3NDAy.XZa7CQ.qVSJ15toa-_TlOlYGd-Mon5kKuk'

client = discord.Client()
options = []

@client.event
async def on_message(message):
    global options
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    
    if 'berg' in message.content:
        msg = 'you know you can follow your boy @ https://www.twitch.tv/bergfps'.format(message)
        await message.channel.send(msg)
        
    if 'kap' in message.content:
        msg = 'Kap is probably busy eating pringles'.format(message)
        await message.channel.send(msg)
        
    if 'carver' in message.content:
        msg = 'Carver. Watch out for that drone.'.format(message)
        await message.channel.send(msg)
        
    if 'tay' in message.content:
        msg = 'Praise be to the creator.'.format(message)
        await message.channel.send(msg)
    
    if 'ranger' in message.content:
        msg = 'Isn\'t Ranger like 35 years old?'.format(message)
        await message.channel.send(msg)
        
    if 'cole' in message.content:
        msg = 'CARRY ME Pinnacole!'.format(message)
        await message.channel.send(msg)

    if 'seb' in message.content:
        msg = 'I think you mean SHELLBY.'.format(message)
        await message.channel.send(msg)

    if 'jenkin' in message.content:
        msg = 'I guess I hate you.'.format(message)
        await message.channel.send(msg)

    if 'leeyroy' in message.content:
        msg = 'LEEEEEEEEEEroyyyyy JENkins!'.format(message)
        await message.channel.send(msg)
    
    if '!stats' in message.content:
        user = message.content.strip('!stats ')
        print(user)
        await stats(user, message)
        
    if '!helpme' in message.content:
        msg = 'Try [!stats (USERNAME)] for stats'+'\n'+'Randomizer Tool:'+'\n'+'[!load (comma separates options)] to load options into the randomizer'+'\n'+'[!run] to run the randomizer'+'\n'+'[!reset] to clear the loaded options'+'\n'+'[!options] to show the loaded options'+'\n'+'[!rand (any number greater than 1)] to generate a random number between 1 and that number'+'\n'+'[!gamecube] to load all multiplayer gamecube games into randomizer'.format(message)
        await message.channel.send(msg)

    if '!load' in message.content:
        x = message.content
        x = x.replace('!load ', '',1)
        v = [x.strip() for x in x.split(',')]
        options.extend(v)
        msg = ', '.join(options)
        mess = 'Current Options: ' + msg.format(message)
        await message.channel.send(mess)

    if '!gamecube' in message.content:
        x = "!load 007 Nightfire, 1080 Avalanche, Beach Spikers, Billy Hatcher, Bomberman Generation, Bust-A-Move, Crash Nitro Kart, Crash Tag Team Racing, Crazy Taxi, Custom Robo, Dark Summit, Digimon World 4, Disney Football, Disney Skateboarding, Disney Basketball, Disney Soccer, Disney Skate, Disney Hide & Sneak, Disney Party, DBZ Budokai, DBZ Budokai 2, F-Zero GX, Fifa Street, Fifa Street 2, Final Fantasy Crystal Chronicles, Fresstyle Street Soccer, Harry Potter Quidditch, Home Run King, Kelly Slater's Pro Surfer, Kirby Air Ride, Mario Golf, Mario Kart, Mario Tennis, Mario Party 4, Mario Party 5, Mario Party 6, Mario Party 7, Mario Strikers, Mario Baseball, MLB Slugfest, Monopoly Party, Naruto Clash of Ninja, Naruto Clash of Ninja 2, NBA Street, NBA Street 2, NBA Street 3, NFL Blitz Pro, NFL Street, NFL Street 2, NHL Hitz, Nick Party Blast, Nicktoons Volcano Island, Nicktoons Unite, Outlaw Golf, Pac Man Fever, Pac Man vs, Pac Man World Rally, Pokemon Colosseum, Pokemon XD, Pool Paradise, Puyo Pop Fever, Rampage, Rayman Arena, Red Card, Rocket Power, Rugrats, Sega Soccer Slam, Shrek Smash N Crash, Sonic Adventure 2 Battle, Sonic Heroes, Sonic Gems, Sonic Riders, Soul Calibur II, Spongebob Lights Camera Pants, SSX 3, SSX Tricky, Starfox Assault, Strike Force Bowling, Super Bubble Pop, Super Monkey Ball, Super Monkey Ball 2, Super Smash Bros Melee, Super Smash Bros Brawl, Project M, Patt's Edition, Swingerz Golf, Teen Titans, Teenage Mutant Ninja Turtles, Teenage Mutant Ninja Turtles 2, Teenage Mutant Ninja Turtles 3, Zelda Four Swords Adventures, LotR Third Age, LotR Return of the King, LotR Two Towers, Powerpuff Girls, Simpsons Road Rage, Simpsons Hit & Run, Timesplitters, Timesplitters 2, TMNT Mutant Melee, Tony Hawk PS3, Tony Hawk PS4, Tony Hawk Underground, Tony Hawk Underground 2, Turok Evolution, Ultimate Muscle, Viewtiful Joe Red Hot Rumble, Wario Ware, Waverace, Worms 3D, Worms Blast, Def Jam Vendetta, NFS Carbon, NFS Underground, NFS Underground 2, NFS Hot Pursuit 2, NFS Most Wanted, Tony Hawk American Wasteland, Tom and Jerry, World Series Poker"
        x = x.replace('!load ', '',1)
        v = [x.strip() for x in x.split(',')]
        options.extend(v)
        msg = ', '.join(options)
        mess = 'Multiplayer Gamecube Games loaded into randomizer'
        await message.channel.send(mess)

    if '!run' in message.content:
        if options:
            winner = random.choice(options)
            msg = winner.format(message)
        else: 
            msg = 'Please load options using !load. For more information, use !help'.format(message)
        await message.channel.send(msg)

    if '!reset' in message.content:
        options = []
        msg = 'Randomizer options cleared'.format(message)
        await message.channel.send(msg)

    if '!remove' in message.content:
        x = message.content
        x = x.replace('!remove ', '',1)
        v = [x.strip() for x in x.split(',')]
        for i in v: 
            if i in options: 
                options.remove(i)
            else: 
                msg = i + ' not in options'.format(message)
                await message.channel.send(msg)
        mess = ', '.join(options)
        msg = 'Current Options: ' + mess.format(message)
        await message.channel.send(msg)

    if '!options' in message.content:
        mess = ', '.join(options)
        msg = 'Options: ' + mess.format(message)
        if len(msg) > 1999: 
            msg = 'List too long to display'
        await message.channel.send(msg)

    if '!rand' in message.content: 
        x = message.content
        x = re.sub("\D", "", x)
        x = int(x)
        result = random.randint(1,x)
        msg = str(result).format(message)
        await message.channel.send(msg)

@client.event
async def on_member_join(member):
    print("Sup. Everyone welcome " + member.name)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
async def stats(user, message):
        page = requests.get("https://r6.tracker.network/profile/pc/" + user)
        soup = BeautifulSoup(page.content, 'html.parser')

        stats = soup.find_all('div', class_='trn-defstat__value')

        level = stats[0].text.strip('\n')
        maxmmr = stats[1].text.strip('\n')
        corank = stats[2].text.strip('\n')
        avgmmr = stats[3].text.strip('\n')
        wins = stats[5].text.strip('\n')
        winperc = stats[6].text.strip('\n')
        kills = stats[7].text.strip('\n')
        kd = stats[8].text.strip('\n')
        
        embed = discord.Embed(title="%s's Stats" %user, color=0x00ff00)
        embed.add_field(name="Level", value=level, inline=True)
        embed.add_field(name="Top MMR", value=maxmmr, inline=True)
        embed.add_field(name="Rank", value=corank, inline=True)
        embed.add_field(name="AVG MMR", value=avgmmr, inline=True)
        embed.add_field(name="Wins", value=wins, inline=True)
        embed.add_field(name="Win %", value=winperc, inline=True)
        embed.add_field(name="Kills", value=kills, inline=True)
        embed.add_field(name="K/D", value=kd, inline=True)
        await message.channel.send(embed=embed)

client.run(TOKEN)