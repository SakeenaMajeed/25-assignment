import random

print("🔥 Welcome to the Mad Libs Adventure! 🔥\n")
print("😆 Fill in the blanks and create your own hilarious story!\n")

name = input("😜 Enter your name: ")
superpower = input("⚡ Enter a superpower: ")
animal = input("🐾 Enter a random animal: ")
place = input("📍 Enter a weird place: ")
food = input("🍕 Enter a delicious food: ")
object = input("🎾 Enter a random object: ")
emotion = input("😊 Enter an emotion: ")
sound = input("🔊 Enter a funny sound (like 'Boing' or 'Kaboom'): ")

actions = [
    "started dancing like a chicken 🐔💃",
    "flew up in the sky ☁️🚀",
    "turned into a frog 🐸😂",
    "sang a song about potatoes 🎶🥔",
    "did 100 push-ups in 2 seconds 💪😆"
]

random_action = random.choice(actions)

story = f"""
🌟✨ YOUR CRAZY MAD LIBS STORY ✨🌟

📌 ONE DAY, {name} 😴✨ woke up and discovered they had an amazing superpower: {superpower}! 🦸‍♂️⚡
   Excited, {name} decided to test it out by going to {place} 🏞️🏃‍♂️.
🐾 As soon as they arrived, they saw a giant {animal} 😱 blocking the way! 🚧
   Without thinking twice, {name} used their {superpower} 💥 and {random_action.upper()} 🌀💨.
🎉 The {animal} was so {emotion} 🤩 that it made a loud '{sound}!' 🔊 and ran away! 🏃‍♂️💨
🍛 After this crazy adventure, {name} sat down 🪑, picked up a {object} 🎾, and started eating {food} 🤤.
🏆🔥 And that, my friend, is how {name} became the legend of {place}! 🎭🎉
"""

print("\n" + "="*50)
print(story)
print("="*50 + "\n")
