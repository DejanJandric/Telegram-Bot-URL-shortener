Infinite Bot - Telegram URL Shortener

📖 Overview
Infinite Bot is a Python-based automation tool designed for Telegram. It streamlines link management by converting long, cumbersome URLs into concise short links using the pyshorteners library (TinyURL integration).

🚀 Features
Auto-Detection: The bot automatically detects valid URLs (HTTP/HTTPS) within any text message using RegEx.
Command Interface: Supports explicit commands like !shorten and !help.
Error Handling: Gracefully handles invalid URLs or API timeouts.
Security: Uses environment variables to protect API tokens.

🛠️ Tech Stack
Language: Python 3.x
Libraries: python-telegram-bot, pyshorteners, python-dotenv
Platform: Telegram API

📸 Bot Profile

![photo_2025-11-20_16-59-31](https://github.com/user-attachments/assets/80ce9486-409a-4310-a44d-0910e7439430)
<img width="390" height="237" alt="Infinitebot" src="https://github.com/user-attachments/assets/ec07f820-5019-4ad8-9c15-b4cc42b9063f" />


⚙️ Installation & Usage
Clone the repository:
Bash

- git clone https://github.com/yourusername/infinite-bot.git


Install dependencies:
Bash

 - pip install -r requirements.txt
Configure Environment: Create a .env file in the root directory and add your token:

Ini, TOML
TELEGRAM_TOKEN=your_token_here
Run the Bot:

Bash

- python telegram_bot.py
