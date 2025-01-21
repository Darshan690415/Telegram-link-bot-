from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import user, admin, error_handler

# Initialize Bot
app = Client("AdvancedLinkBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register Handlers
user.register_handlers(app)
admin.register_handlers(app)
error_handler.register_error_handler(app)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()