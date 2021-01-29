import discord
from discord.ext import commands

clint = commands.Bot(command_prefix=("."))

@clint.event
async def on_ready():
    print(" I'am ready")

@clint.event
async def on_member_join(member):
    print(f"Hi ya{member}")

@clint.event
async def on_member_remove(member):
    print(f"Bye Bye ya {member} ya 3ars")

@clint.command()
async def wala(ctx):
    await ctx.send("5o4 nam ya kosomk")

@clint.command()
async def y3ars(ctx):
    await ctx.send("omak  labsa stars")

@clint.command()
async def kosomk(ctx):
    await ctx.send("kosomen omk")

@clint.command()
async def sam3ny(ctx):
    await ctx.send("la a7na m4 sam3ynk")

@clint.command()
async def ya(ctx):
    await ctx.send("nakk batman ya 3ars")

@clint.command()
async def hapip(ctx):
    await ctx.send("24rb 7alebe ya 5awal")


@clint.command()
async def y5awal(ctx):
    await ctx.send("zby fe tezk at7awal")



@clint.command()
async def y3ars(ctx):
    await ctx.send("5od yakosomk")


@clint.command()
async def ping(ctx):
    await ctx.send("pong !")


@clint.command()
async def matkalm4_kda(ctx):
    await ctx.send("kosomk atkalm bra7ty ya 3ars")

@clint.command()
async def mariam(ctx):
    await ctx.send("Jo, Love her! so much ❤")

@clint.command()
async def waad(ctx):
    await ctx.send("EX al 3ars yaso")


@clint.command()
async def yara(ctx):
    await ctx.send("Boda, steel Love her ❤")

@clint.command()
async def roka(ctx):
    await ctx.send("lebya hahahahaha\n bahazar LOL \n Bedo hate her 😎")


@clint.command()
async def mera(ctx):
    await ctx.send("Center, profitinal😂😂😂")


@clint.command()
async def shahd(ctx):
    await ctx.send("mama 4aft al caht")


@clint.command()
async def a7na(ctx):
    await ctx.send("Rgala 💪💪")



@clint.command()
async def commands(ctx):
    await ctx.send(".wala \n .sam3ny \n .u5od \n .ya \n .hpip \n .y5awal \n . y3ars \n .ping")

@clint.command()
async def easteregg(ctx):
    await ctx.send(".waad \n .yara \n .roka \n .mariam")


@clint.command()
async def u5od(ctx):
    await ctx.send("7oto fe tezk")


@clint.command()

async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@clint.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

clint.run("ODA0MDI5OTY4NTAxODMzNzI4.YBGZQg.B2iET8uyEbGajWmRbOEzOO7PPj0")