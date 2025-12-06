<div align="center">
  <img src="[photo_2025-11-20_16-59-31.jpg](https://ibb.co/VYVKF4GQ)">
  
  <h1>Infinite Bot</h1>
  
  <p>
    <b>Telegram URL Shortener</b>
  </p>
  
  <p>
    <a href="https://github.com/DejanJandric/Telegram-Bot-URL-shortener/issues">Report Bug</a>
    ·
    <a href="https://github.com/Telegram-Bot-URL-shortener/pulls">Request Feature</a>
  </p>
</div>

<br />


📖 **Overview** 

- Infinite Bot is a Python-based automation tool designed for Telegram. 
- It streamlines link management by converting long, cumbersome URLs into concise short links using the pyshorteners library (TinyURL integration).


🚀 **Features**

- Auto-Detection: The bot automatically detects valid URLs (HTTP/HTTPS) within any text message using RegEx. 

- Command Interface: Supports explicit commands like !shorten and !help. 

- Error Handling: Gracefully handles invalid URLs or API timeouts. 

- Security: Uses environment variables to protect API tokens.


## 🤖 Bot Commands

| Command | Usage | Description |
| :--- | :--- | :--- |
| **Shorten Link** | `!shorten <url>` | Explicitly shortens the provided URL (e.g., `!shorten https://github.com`). |
| **Auto-Detect** | `https://...` | Just paste any long link directly into the chat, and the bot will detect and shorten it automatically. |
| **Help** | `!help` | Displays a welcome message and basic instructions. |
| **Command List** | `!commandlist` | list of all available commands. |
| **Custom Alias** | `!custom <url> <alias>` | *(Beta)* Attempt to create a custom link alias. |


## Screenshots

<img width="390" height="237" alt="Infinitebot" src="https://github.com/user-attachments/assets/3edfb31f-d58e-440e-9775-cbdacdbcdc82" />



## Installation

- git clone https://github.com/Telegram-Bot-URL-shortener


## Install dependencies

- pip install -r requirements.txt

## Create a .env file in the root directory and add your token:

- TELEGRAM_TOKEN=your_token_here

## Run the bot :

- python telegram_bot.py



## Tech Stack

**Language**: Python 3.14.0

**Libraries**: python-telegram-bot, pyshorteners, python-dotenv

**Platform**: Telegram API


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## 🤝 **Contributing**


Feel free to fork this repository and submit pull requests.
