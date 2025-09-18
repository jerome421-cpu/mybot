import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get bot token from environment variable (more secure)
BOT_TOKEN = os.getenv('BOT_TOKEN', '7991521182:AAGqp-hIjEfASGzUDNcRq41-RiWtokNmKP4')
CHANNEL_LINK = "https://t.me/+mZ-efTXP6LgzMWNk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler for the /start command"""
    try:
        # Send the channel promotion message
        message = await update.message.reply_text(
            "Join to the most trusted channel\n" + CHANNEL_LINK
        )
        
        # Schedule message deletion after 5 minutes (300 seconds)
        asyncio.create_task(delete_after_delay(message, 300))
    except Exception as e:
        print(f"Error in start command: {e}")

async def delete_after_delay(message, delay: int) -> None:
    """Delete message after specified delay in seconds"""
    await asyncio.sleep(delay)
    try:
        await message.delete()
        print("Message deleted successfully")
    except Exception as e:
        print(f"Error deleting message: {e}")

def main() -> None:
    """Start the bot"""
    try:
        # Create application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add handler for start command
        application.add_handler(CommandHandler("start", start))
        
        print("Bot starting...")
        # Start polling
        application.run_polling()
    except Exception as e:
        print(f"Error starting bot: {e}")

if name == "main":
    main()