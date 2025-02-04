# 🚀 How to Connect a Python Bot to Discord

This guide explains how to connect your Python bot to Discord, including setting up a bot, installing dependencies, and running the bot.

## 1️⃣ Creating a Discord Bot
Before writing Python code, we need to create and register a bot in Discord.

### Step 1: Go to the Discord Developer Portal
1. Open [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"** and give your bot a unique name.
3. Navigate to **"Bot"** on the left panel.
4. Click **"Add Bot"**, confirm, and enable **"Public Bot"** if you want others to use it.

---

## 2️⃣ Getting the Bot Token
1. Under the **"Bot"** tab, find **"Token"**.
2. Click **"Reset Token"** and copy the new token.
> ⚠️ **DO NOT SHARE THIS TOKEN!** (It gives full access to your bot.)

---

## 3️⃣ Installing Required Dependencies
Before running the bot, install the required Python libraries.

```bash
pip install discord
```

or for more stability:

```bash
pip install discord.py
```

---

## 4️⃣ Writing the Python Code
Create a new Python file called **bot.py** and paste the following code:

```python
import discord
from discord.ext import commands

# ✅ Your bot token (Replace with your actual token)
TOKEN = "YOUR_BOT_TOKEN_HERE"

# ✅ Set up bot intents (Allows bot to see messages, members, and servers)
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

# ✅ Create bot instance with prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Bot event: When bot is ready
@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user.name} is now online and connected to Discord!')

# ✅ Example Command: Responds to "!hello"
@bot.command()
async def hello(ctx):
    await ctx.send(f'👋 Hello, {ctx.author.name}!')

# ✅ Run the bot
bot.run(TOKEN)
```

---

## 5️⃣ Running the Bot
1. Save the file as **bot.py**.
2. Open a terminal in the same directory and run:

```bash
python bot.py
```

3. If the setup is correct, you should see:

```bash
✅ Bot MyBot is now online and connected to Discord!
```

---

## 6️⃣ Inviting the Bot to Your Server
To invite the bot:
1. Go to **OAuth2 → URL Generator** in the Discord Developer Portal.
2. Select the **"bot"** and **"applications.commands"** scopes.
3. Under Permissions, select:
   - **Administrator** (For full access) 
   - OR manually select what your bot needs.
4. Copy the generated link and paste it into your browser.
5. Select your Discord server and invite the bot!

---

## 7️⃣ Common Issues & Fixes

### ❌ ModuleNotFoundError: No module named 'discord'
✅ Run:
```bash
pip install discord
```

### ❌ discord.errors.LoginFailure: Improper token has been passed.
✅ Check if you copied the correct bot token!
✅ Make sure you did not share your token publicly.

### ❌ Bot is online but not responding to commands
✅ Ensure your bot has the correct permissions.
✅ Check if you enabled **"MESSAGE CONTENT INTENT"** under "Bot" settings.

---

## ✅ Next Steps
🎮 **Set up automatic channels & roles** → *(Customize bot.py for structured servers)*
⚙️ **Add more commands** → *(Use `@bot.command()` to create functions)*
🔧 **Deploy the bot on a server** → *(Use AWS, Heroku, or Replit to keep it running 24/7)*

🚀 Now your bot is ready to connect and work on Discord! 🎮🔥
