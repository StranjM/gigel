from pydoc import cli 
import sys
from turtle import color
from warnings import warn_explicit 
import discord
from discord.ext import tasks
from discord.ext import commands
from discord.utils import get
import random

intents = discord.Intents.default()
intents.members = True
intents.all()

client = commands.Bot(command_prefix="g", intents = intents, help_commands = None)

@client.event
async def on_ready():
    print('finished...')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

#                                             --kick--
@client.command()
@commands.has_role(898264710833639454)
async def kick(ctx, member: discord.Member, *, reason = None):
    try: 
        await member.kick(reason = reason)
        await ctx.send(f"User {member} kicked")
    except:
        return

#                                              --ban--
@client.command()
@commands.has_role(898265798454411284)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} got banned!') 

#                                              --unban--
@client.command()
@commands.has_role(898265798454411284)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

    await ctx.guild.unban(user)
    await ctx.send(f'User {member} was unbanned!') 

#you need to type gkick [member] [reason] but i already have that command idk the code looks sus mgh kinda cursed we should rewrite it idk how will help an explain

@client.command()
@commands.bot_has_permissions(ban_members = True)
#first we need to create the command and assign the parameters we need
# - ctx: context, you now know who wrote the message, in what channel etc.
# - member: discord.Member=None: the member at the first position after the command. the ping? yes
# - *: so we can get not default stuff like a simple "String" from the message
# - reason: everything typed after mentoning the user
async def warn(ctx, member: discord.Member=None, *, reason):
    #we need to check if the user is the bot or the author
    if member == client or member == ctx.author.name:
        #if the mentioned memeber is the bot or the message author, the bot will send this phrase: as i said you need to learn basic python to understand the code, i looked a bit i can do a crash course if you want instead of helping your here what? a python "crash course". quick overview how python code works and some basic stuff you need to know.
        # no just here with a new file i can comment the code and stuff like that do you mean vc? ok
        #go to the main.py
        return await ctx.send("You can't warn them!")
    



#                                               --test--
@client.command()
async def hello (ctx):
    await ctx.send('hi')

@client.command()
async def yes(ctx):
    await ctx.send('no')

@client.command()
async def no(ctx):
    await ctx.send('yes')


#@client.command()
#async def anya(ctx):
#    await ctx.send("steal account click here-https://images.app.goo.gl/h2MAbUGeZVPH1H3H7")    
        
#                                             --ASSignrole--
@client.command()
@commands.has_permissions(manage_roles=True)
async def assignrole(ctx, roleId : discord.Role):
    server = client.get_guild(983806648655167528)
    role2 = discord.utils.get(server.roles, id = 985874646794637402)#Role, which gets assigned to all people with the pinged role
    print("Role assigned to: ")
    for guild in client.guilds:
        for member in guild.members:
            if roleId in member.roles:
                print(member.name)
                await member.add_roles(role2)  
                  
#                                                --invlink--
@client.command()
async def invlink(ctx):
    embed=discord.Embed(title="https://discord.gg/sdkGVYp7UB", color=0xe67e22)
    embed.set_footer(text = f"Thanks for choosing our server!" ) 
    await ctx.send(embed = embed)

#                                                --commands--
@client.command()
async def commands(ctx):
    embed=discord.Embed(title="Commands list", color=0xe67e22)
    embed.add_field(name= "Prefix", value= "g", inline=False)
    embed.add_field(name= "Moderator", value= "kick, ban, unban", inline=False)
    embed.add_field(name= "Minigame", value= "yes, gg, percentage", inline=False)
    embed.add_field(name= "Server link", value= 'invlink', inline=False)
    embed.add_field(name= "Number Generator", value= 'ng100, ng1000, ng10000')
    embed.add_field(name= "Pictures", value= "obama, trump", inline=False)
    embed.set_footer(text= "Also find out ;)")
    await ctx.send(embed=embed)

#                                                   --IDK--
#import random
#@client.command()
#async def percentage(ctx):
#    percentage = (random.randint(0, 100))
#    await ctx.send(f'{percentage}%')

#                                                 --minigame--
from discord.ext import commands
@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def g(ctx):
    gg_list = ["gg", "gg", "gg", "gg", "gg", "gg", "gg", "gg", "gg", "gg", "Gg"]
    embed = discord.Embed(name="gg?", description=f"{random.choice(gg_list)}", color=0xe67e22)
    await ctx.send(embed = embed)

@g.error
async def command_name_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", color=0xe67e22)
            await ctx.send(embed=em)

@client.command()
async def percentage(ctx):
    await ctx.send('10%') 

#                                              --num generator-n-- 
@client.command()
async def ng100(ctx):
    embed = discord.Embed(title="Number", description=f"{random.randrange(101)}", color=0xe67e22)
    await ctx.send(embed = embed)

@client.command()
async def ng1000(ctx):
    embed = discord.Embed(title="Number", description=f"{random.randrange(1001)}", color=0xe67e22)
    await ctx.send(embed = embed)

@client.command()
async def ng10000(ctx):
    embed = discord.Embed(title="Number", description=f"{random.randrange(10001)}", color=0xe67e22)
    await ctx.send(embed = embed)

#                                                   --pic--
@client.command()
async def obama(ctx):
    await ctx.send(file=discord.File('obama-pyramid.gif'))

@client.command()
async def trump(ctx):
    await ctx.send(file=discord.File('trump-trumpium.gif'))

@client.command()
async def pr2(ctx):
    pr_list = ['obama-pyramid.gif', 'obama-pyramid.gif', 'obama-pyramid.gif', 'obama-pyramid.gif', 'trump-trumpium.gif']
    file = discord.File = f"{random.choice(pr_list)}"
    await ctx.send(file = file)

@client.command()
async def pr(message):
    await message.channel.send(file=discord.File(random.choice('obama-pyramid.gif', 'obama-pyramid.gif', 'obama-pyramid.gif', 'obama-pyramid.gif', 'trump-trumpium-gif')))


#from discord import Button

#@client.command()
#async def test(ctx):
#    button = discord.ui.Button(label="yes", style=discord.Buttonstyle )
#    await ctx.send("maybe")







client.run('OTgzODA3MTM0NTQwMTM2NDY4.G-3SKf.k-W22D1_megGlpWVvQJN3i_1gu4rPS5c8spvtE')    