from pyrogram import filters
from helpers.generate_links import generate_direct_link, generate_streamable_link
from helpers.file_utils import validate_file, save_file_locally
from helpers.database import save_file

def register_handlers(app):
    @app.on_message(filters.private & filters.document)
    async def handle_file(client, message):
        file = message.document

        # Validate File Size
        is_valid, msg = validate_file(file.file_size)
        if not is_valid:
            await message.reply_text(f"❌ {msg}")
            return

        await message.reply_text("✅ Processing your file...")

        # Save File Locally
        file_path = await save_file_locally(file, "./uploads")

        # Generate Links
        direct_link = generate_direct_link(file_path)
        streamable_link = generate_streamable_link(file.file_id)

        # Save to Database
        save_file(
            file_id=file.file_id,
            file_name=file.file_name,
            user_id=message.from_user.id,
            direct_link=direct_link,
        )

        # Send Links to User
        await message.reply_text(
            f"🎉 Here are your links:\n\n"
            f"📥 **Direct Link:** [Click Here]({direct_link})\n"
            f"▶️ **Streamable Link:** [Watch Here]({streamable_link})",
            disable_web_page_preview=True,
        )

    @app.on_message(filters.private & filters.command("myfiles"))
    async def list_user_files(client, message):
        from helpers.database import get_files_by_user

        user_id = message.from_user.id
        files = get_files_by_user(user_id)

        if not files.count():
            await message.reply_text("You have not uploaded any files yet!")
            return

        text = "📂 **Your Uploaded Files:**\n\n"
        for file in files:
            text += f"📄 **{file['file_name']}**\n"
            text += f"📥 [Direct Link]({file['direct_link']})\n\n"

        await message.reply_text(text, disable_web_page_preview=True)