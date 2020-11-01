import re
import discord
from discord.ext import commands
import asyncio
import logging
import random

bot = commands.Bot(command_prefix="!")
voted = [572448507344977942, 615936514219835393, 269750332337291264]
votingenabled = False
amac = 3
lukas = 0
sep = 0

"""
 candidates:
 amac, lukas, sep
"""
bot.remove_command('help')

@bot.event
async def on_ready():
    print('hi {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!vote in DM's to vote"))

@bot.command()
async def openvotes(ctx):
    owner = await bot.fetch_user(user_id=459773410285846558)
    rock = await bot.fetch_user(user_id=168731800963645440)
    if ctx.author == owner or ctx.author == rock:
        embedVoteOpenedReturnMsg = discord.Embed(title="OK", description="The vote has been open. Now people can use the !vote command.",
                                        color=0x00ff00)
        await ctx.channel.send(embed=embedVoteOpenedReturnMsg)
        global votingenabled
        votingenabled = True
    else:
        embedNotOwner = discord.Embed(title="Not Bot Developer", description="Only Konmedy can open the votes since he's, you know, the bot developer.", color=0xff0000)
        await ctx.channel.send(embed=embedNotOwner)
        return

@bot.command()
async def vote(ctx, candidate: int = 0):
    owner = await bot.fetch_user(user_id=459773410285846558)
    rock = await bot.fetch_user(user_id=168731800963645440)
    if votingenabled == False:
        embedVotingDisabled = discord.Embed(title="Voting Disabled", description="The !vote command is currently disabled.",
                                   color=0xff0000)
        await ctx.channel.send(embed=embedVotingDisabled)
        return
    else:
        if ctx.author.id in voted:
            embedVotedAlready = discord.Embed(title="Voted already", description="You can only vote once.",
                                       color=0xff0000)
            await ctx.channel.send(embed=embedVotedAlready)
            return
        else:
            if isinstance(ctx.channel, discord.channel.DMChannel):
                if candidate == 1:
                    voted.append(ctx.author.id)
                    global amac
                    amac += 1
                    embedVoted = discord.Embed(title="Voted", description="You have voted for Amac.",
                                               color=0x00ff00)
                    await ctx.channel.send(embed=embedVoted)
                    return
                elif candidate == 2:
                    voted.append(ctx.author.id)
                    global lukas
                    lukas += 1
                    embedVoted = discord.Embed(title="Voted", description="You have voted for Lukas.",
                                               color=0x00ff00)
                    await ctx.channel.send(embed=embedVoted)
                    return
                elif candidate == 3:
                    voted.append(ctx.author.id)
                    global sep
                    sep += 1
                    embedVoted = discord.Embed(title="Voted", description="You have voted for Sepkat.",
                                               color=0x00ff00)
                    await ctx.channel.send(embed=embedVoted)
                    return
                else:
                    embedCandidates = discord.Embed(title="Candidates", description="**These are the Pillow's Moderator Election final candidates:**\n\n**1:** Amac *(!vote 1)*\n**2:** Lukas *(!vote 2)*\n**3:** Sepkat *(!vote 3)*\n\nTo vote, DM the bot \"!vote\" and the number of the candidate.", color=0x00ff00)
                    await ctx.channel.send(embed=embedCandidates)
                    return

            else:
                embedNotDM = discord.Embed(title="Not in DM's", description="You can only vote on your candidate in DM's.", color=0x00ff00)
                await ctx.channel.send(embed=embedNotDM)
                return

@bot.command()
async def countvotes(ctx, areyousure: str = "not sure"):
    owner = await bot.fetch_user(user_id=459773410285846558)
    rock = await bot.fetch_user(user_id=168731800963645440)
    if ctx.author == owner or ctx.author == rock:
        if areyousure == "not sure":
            embedAreYouSure = discord.Embed(title="Are you sure?",
                                          description="Are you sure you want to close the votes and send the results?",
                                          color=0x00ff00)
            await ctx.channel.send(embed=embedAreYouSure)
        elif areyousure.lower() == "yes":
            embedVotesClosed = discord.Embed(title="OK",
                                          description="OK. The votes have been closed. The results have been sent to the organisators of the election. Thank you everyone for voting!",
                                          color=0x00ff00)
            await ctx.channel.send(embed=embedVotesClosed)
            global amac
            global lukas
            global sep
            embedResults = discord.Embed(title="Election Results",
                                         description=f"**The Pillow Moderator Election voting has been closed. Here are the voting results:**\n\nAmac: **{amac}**\nLukas: **{lukas}**\nSepkat: **{sep}**",
                                         color=0x00ff00)
            await rock.send(embed=embedResults)
            await owner.send(embed=embedResults)
            votingenabled = False
        else:
            embedAreYouSure = discord.Embed(title="Are you sure?",
                                          description="Are you sure you want to close the votes and send the results?",
                                          color=0x00ff00)
            await ctx.channel.send(embed=embedAreYouSure)
    else:
        embedNotOwner = discord.Embed(title="Not Bot Developer", description="Only Konmedy can cloes the votes since he's, you know, the bot developer.", color=0xff0000)
        await ctx.channel.send(embed=embedNotOwner)
        return

@bot.command()
async def instructions(ctx):
    rock = await bot.fetch_user(user_id=168731800963645440)
    if ctx.author == rock:
        embedInstructions = discord.Embed(title="Voting Instructions", description="**How to vote:**\n\n1. DM the bot \"!vote\"\n2.You'll get a DM with candidates who you can vote on\n3. Vote on your candidate\n\nHere's how the voting process looks like: https://i.imgur.com/9onxkaE.png", color=0x00ff00)
        await ctx.channel.send("", embed=embedInstructions)
        return
    else:
        pass

bot.run("ADD YOUR TOKEN HERE")
