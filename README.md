**Infinite Bot - Telegram URL Shortener**


📖 **Overview** 

Infinite Bot is a Python-based automation tool designed for Telegram. 
It streamlines link management by converting long, cumbersome URLs into concise short links using the pyshorteners library (TinyURL integration).


🚀 **Features**

Auto-Detection: The bot automatically detects valid URLs (HTTP/HTTPS) within any text message using RegEx. 

Command Interface: Supports explicit commands like !shorten and !help. 

Error Handling: Gracefully handles invalid URLs or API timeouts. 

Security: Uses environment variables to protect API tokens.



## Screenshots

![Infinite Bot](https://freeimage.host/i/fudnL0J)


## Installation

git clone https://github.com/Telegram-Bot-URL-shortener


## Install dependencies

pip install -r requirements.txt

## Create a .env file in the root directory and add your token:

TELEGRAM_TOKEN=your_token_here

## Run the bot :

python telegram_bot.py



## Tech Stack

**Language**: Python 3.x

**Libraries**: python-telegram-bot, pyshorteners, python-dotenv

**Platform**: Telegram API


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## 🤝 **Contributing**


Feel free to fork this repository and submit pull requests.
