# 🎯 Discord OpenSea NFT Floor Bot

**Discord-Opensea-NFT-Floor-Bot** is a lightweight Discord bot that retrieves and displays the **floor price** of any NFT collection on **OpenSea**.  
It shows the price in **ETH** and its current equivalent in **USD**, so users can track trends without leaving Discord.

---

## 🚀 What It Does

- 🔍 Scrapes OpenSea for the lowest listed NFT price in a given collection
- 💸 Converts ETH floor price to live USD value using CoinGecko
- 💬 Sends a clean, formatted embed message in your server
- ⚡ Quick and easy `/floor <collection-name>` command

---

## 🔍 Features

- 💎 Get real-time NFT floor prices in both ETH & USD
- 🌐 Supports any OpenSea collection via its URL slug
- ⚙️ Simple command: `!floor <collection-name>`
- 🧠 Powered by BeautifulSoup web scraping and CoinGecko API

---

## 🔐 API Key Setup (.env Required)

This project uses an `.env` file to store your **Discord API key** securely.  
You must create your own `.env` file in the root of the project:
TOKEN=your-discord-bot-token-here
