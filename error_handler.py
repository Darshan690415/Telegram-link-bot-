def register_error_handler(app):
    @app.on_errors()
    async def handle_errors(client, update, error):
        # Log the error (you can use logging module)
        print(f"Error: {error}")
        if hasattr(update, "message"):
            await update.message.reply_text("❌ An error occurred while processing your request.")