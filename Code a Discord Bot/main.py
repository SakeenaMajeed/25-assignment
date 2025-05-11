import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Allow reading message content

bot = commands.Bot(command_prefix='!', intents=intents)

# Bot ready
@bot.event
async def on_ready():
    print(f'✅ Bot is ready: {bot.user.name}')

# !ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Hello {ctx.author.mention}!")

# This is a separate listener for questions
@bot.event
async def on_message(message):
    # Process commands first (important!)
    await bot.process_commands(message)
    
    # Skip bot's own messages
    if message.author == bot.user:
        return
    
    # Add debug output
    print(f"Received message: '{message.content}'")
    
    # Check if message looks like a question (with more conditions)
    content = message.content.lower()
    if (
        "?" in content or
        content.startswith(("what", "how", "why", "when", "who", "where", "is", "can", "do", "does", "will", "would"))
    ):
        print(f"Question detected: '{message.content}'")
        responses = [
            "🤔 Hmm, acha sawal hai!",
            "💡 Let me think about that...",
            "😅 Main AI nahi hoon... lekin koshish karti hoon!",
            "📚 Python ek programming language hai — powerful aur easy to learn!",
            "🥹 Mujhe is ka exact answer nahi pata, but I believe in you!",
        ]
        chosen_response = random.choice(responses)
        print(f"Sending response: '{chosen_response}'")
        await message.channel.send(chosen_response)

# Run the bot
bot.run(token)