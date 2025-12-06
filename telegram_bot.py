import os
import re
import pyshorteners
from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = "Your_Telegram_Bot_Token_Here"
BOT_USERNAME: Final = '@Infinite_inf_bot'

# Check if keys are present
if not TOKEN:
    raise ValueError("Missing TELEGRAM_TOKEN in .env file")

# Initialize the shortener
shortener = pyshorteners.Shortener()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! I am Infinite Bot (URL Edition).\n"
        "Send me any link, and I will shorten it for you.\n"
        "Type !help if you need more information."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "🔗 **URL Shortener Bot Help**\n\n"
        "Here are the commands I understand:\n"
        "1. **!shorten <url>** - Shortens a long link.\n"
        "2. **!custom <url> <alias>** - (Beta) Try to create a custom link.\n"
        "3. **!commandlist** - Shows the command list.\n"
        "4. **Direct Link** - Just paste a link, and I will shorten it automatically."
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def command_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Available commands:\n!help\n!custom\n!shorten\n!commandlist"
    )


async def shorten_url_logic(url: str) -> str:

    try:

        return shortener.tinyurl.short(url)
    except Exception as e:
        return f"Error shortening link: {str(e)}"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text: str = update.message.text
    response: str = ""

    # Handle "!" Commands manually(since Telegram uses / by default)
    if text.startswith('!'):
        command_parts = text.split()
        command = command_parts[0].lower()

        if command == '!help':
            await help_command(update, context)
            return

        elif command == '!commandlist':
            await command_list(update, context)
            return

        elif command == '!shorten':
            if len(command_parts) > 1:
                url_to_shorten = command_parts[1]
                short_url = await shorten_url_logic(url_to_shorten)
                response = f"Here is your short URL link: {short_url}"
            else:
                response = "Please provide a URL. For example: !shorten https://google.com"

        elif command == '!custom':
            response = "Custom aliases coming soon. For now, try standard shortening!"

        else:
            response = "Unknown command. Type !help for more options."

    # Handle raw URLs
    # This regex is checking if the message is just an URL
    elif re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
        short_url = await shorten_url_logic(text)
        response = f"Detected a link! Here is the shortened version or your link:\n{short_url}"

    # Default fallback
    else:
        response = "I didn't understand that. Please send a valid URL or type !help."

    # Send the response
    if response:
        await update.message.reply_text(response)


async def error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Starting Infinite Bot (URL Shortener)...")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)
