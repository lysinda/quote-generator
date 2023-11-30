import random
import math
import textwrap
import telepot
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
from dotenv import load_dotenv


load_dotenv("") # Path to .env file, to be entered by user

WIDTH = 400
HEIGHT = 400

# Send the image with a telegram bot
def telegram_bot_sendimg(image):
    bot_token = os.getenv("") # Bot token name, to be entered by user
    chat_id = os.getenv("CHAT_ID")

    bio = BytesIO()
    bio.name = 'image.png'
    image.save(bio, 'PNG')
    bio.seek(0)

    bot = telepot.Bot(bot_token)
    bot.sendPhoto(chat_id, photo=bio)

# Get the quotes from the custom quotes.txt file and choose a random one
with open("quotes.txt", "r") as f:
    quotes = f.readlines()
    quote = random.choice(quotes)

# Adjust the font size and line width depending on the length of the chosen quote
font_size = 70 - math.trunc(len(quote) / 20) * 5 + max([math.trunc((len(quote) - 160) / 20), 0]) * 5
line_width = 12 + math.trunc(len(quote) / 20) * 2

# Select a random image as a background
img_num = random.randint(1, 10)
img = Image.open(f"images/{img_num}.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("font.ttf", font_size)

# Write the quote unto the image, line by line
lines = textwrap.wrap(quote, line_width)
y = (HEIGHT - len(lines) * font.getsize(lines[0])[1]) / 2
for line in lines:
    w, h = font.getsize(line)
    draw.text(((WIDTH - w) / 2, y), line, font=font)
    y += h

telegram_bot_sendimg(img)