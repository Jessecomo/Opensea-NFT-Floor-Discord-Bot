import os
import requests
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import re
import datetime

#Scrape the NFT collection page sorted low-high
class NFTfloor:
    def __init__(self):
        self.bot = {"collection": None,"url": None,"img": None, "floor": None, "USD": None}

    def get_floor(self, collection):
        collection_url = 'https://opensea.io/collection/' + collection
        sorted_url = collection_url + '?search[sortBy]=PRICE&search[sortAscending]=true&search[toggles][0]=BUY_NOW'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(sorted_url, headers=hdr)
        html_page = urlopen(req)
        html_text = html_page.read().decode("utf-8")
        soup = BeautifulSoup(html_text, "html.parser")
        self.bot["collection"] = soup.h2.text
        self.bot["url"] = sorted_url
        self.bot["floor"] = soup.find("div",{"class":"Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount"}).text

        ethreq = Request("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
        html_page_eth = urlopen(ethreq)
        html_text_eth = html_page_eth.read().decode("utf-8")
        soup_eth = BeautifulSoup(html_text_eth, "html.parser")
        eth_price = re.findall('\d*\.?\d+',soup_eth.text)
        eth_to_usd = float(eth_price[0]) * float(self.bot["floor"])
        self.bot["USD"] = str("{0:.2f}".format(eth_to_usd))

def get_floor_message(collection):
    embed = discord.Embed()
    NFT = NFTfloor()
    NFT.get_floor(collection)
    if NFT.bot["collection"] is None:
        embed.title = "Error occurred when retrieving NFT collection name"
        return embed
    if NFT.bot["url"] is None:
        embed.title = "Error occurred when retrieving NFT url."
        return embed
    if NFT.bot["floor"] is None:
        embed.title = "Error occurred when retrieving NFT floor Price."
        return embed

    embed.title = NFT.bot["collection"] + " Floor Price"
    embed.url = NFT.bot["url"]
    embed.description = "**" + NFT.bot["floor"] + " ETH" + "**" + " ($" + NFT.bot["USD"] + " USD)"
    embed.color = 0x0a6fdb
    return embed

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def floor(ctx, collection = None):
    if collection:
        #Send NFT Floor
        await ctx.send(embed = get_floor_message(collection))


load_dotenv()
bot.run(os.getenv('TOKEN'))
