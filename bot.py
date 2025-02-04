import discord
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN_HERE"


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is now online! Resetting server structure...')
    
    for guild in bot.guilds:
        await delete_all_roles(guild)
        await delete_all_channels_and_categories(guild)
        await create_channels_and_roles(guild)

@bot.event
async def on_guild_join(guild):
    """Deletes all channels, roles, and sets up the server structure when the bot joins a new server."""
    print(f"Bot has joined {guild.name}. Resetting channels and roles...")
    await delete_all_roles(guild)
    await delete_all_channels_and_categories(guild)
    await create_channels_and_roles(guild)

async def delete_all_roles(guild):
    """Deletes all existing roles except @everyone."""
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"Deleted role: {role.name}")
            except Exception as e:
                print(f"Error deleting role {role.name}: {e}")

async def delete_all_channels_and_categories(guild):
    """Deletes all existing text channels, voice channels, and categories."""
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except Exception as e:
            print(f"Error deleting {channel.name}: {e}")

async def create_channels_and_roles(guild):
    """Sets up the server structure for Infected Soul Project."""

    roles = ["Game Developer", "Programmer", "Artist", "Composer", "Playtester", "Marketing & Social", "Writer", "Animator", "Technical Artist", "Video Editor", "Admin", "Moderator"]
    for role in roles:
        existing_role = discord.utils.get(guild.roles, name=role)
        if not existing_role:
            await guild.create_role(name=role, mentionable=True)
            print(f"Created role: {role}")

    categories = {
        "📢 | General": ["📢announcements", "👋welcome", "📜rules", "💬general-chat", "🎮game-recommendations", "🔗resources", "📅events", "💼job-listings"],
        "🛠 | Infected Soul Project": ["💡ideas", "📜story-lore", "🎭character-design", "🎮gameplay-mechanics", "🛠programming", "🤖artificial-intelligence", "🗺️level-design", "🎥cinematics-animation"],
        "🎨 | Art & Visual Design": ["🎨concept-art", "🖌3D-modeling", "🎭character-world-design", "🎨UI-UX-design"],
        "🔊 | Sound & Music": ["🎼game-music", "🎤sound-effects"],
        "🎮 | Playtesting & Debugging": ["🎮playtesting", "🐛bug-reports"],
        "📢 | Social Media & Marketing": ["📢social-media", "🎬trailers-videos", "✍️blogs-articles"],
        "🔊 | Voice Channels": ["💻 | programming-room", "🎨 | artist-room", "🎼 | music-studio", "🕹 | playtesting-room", "📢 | team-meetings", "🌎 | open-collaboration"]
    }

    for category_name, channels in categories.items():
        category = await guild.create_category(category_name)
        print(f"Created category: {category_name}")

        for channel_name in channels:
            if "🔊" in category_name:
                await guild.create_voice_channel(channel_name, category=category)
            else:
                await guild.create_text_channel(channel_name, category=category)
            print(f"Created channel: {channel_name}")

bot.run(TOKEN)
