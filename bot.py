import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents) # command_prefix可以換成別的符號或文字 intents記得在discord開發頁面打開


@bot.event
async def on_ready():
    print(f"機器人 --> {bot.user}")

@bot.command()
async def load(ctx, extension):
    if extension in cogs:
          await ctx.send(f"{extension} 已載入，將進行重載")
          await bot.reload_extension(f"cogs.{extension}")
          return
      else:
          try:
              await bot.load_extension(f"cogs.{extension}")
              await ctx.send(f"{extension} 已載入")
              cogs.append(extension)
          except:
              await ctx.send(f"{extension} 載入失敗，請檢查檔案是否存在或是否存在錯誤")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension}已卸載")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start("TOKEN") # TOKEN換成自己的


if __name__ == "__main__":
    asyncio.run(main())
