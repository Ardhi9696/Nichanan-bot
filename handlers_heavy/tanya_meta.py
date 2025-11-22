import os
import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from meta_ai_api import MetaAI

logger = logging.getLogger(__name__)
_admin_ids_env = os.getenv("ADMIN_LIST", "") or ""
_owner_id = os.getenv("MY_TELEGRAM_ID", "")
_admin_ids = {
    int(part.strip())
    for part in (_admin_ids_env.split(",") if _admin_ids_env else [])
    if part.strip().isdigit()
}
if _owner_id.strip().isdigit():
    _admin_ids.add(int(_owner_id.strip()))


async def tanya_meta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_type = update.effective_chat.type
    user = update.effective_user
    user_mention = user.mention_html()
    is_admin = user.id in _admin_ids

    # Hanya boleh di grup; DM hanya untuk admin
    if chat_type == "private" and not is_admin:
        await update.message.reply_text(
            "❌ /tanya hanya bisa dipakai di grup. DM hanya untuk admin."
        )
        return
    if chat_type not in ["group", "supergroup"] and not is_admin:
        await update.message.reply_text(
            "❌ /tanya hanya bisa dipakai di grup.", disable_web_page_preview=True
        )
        return

    if len(context.args) == 0:
        await update.message.reply_html(
            f"💬 Halo {user_mention}, silakan gunakan perintah seperti ini:\n"
            f"<code>/tanya Siapa presiden Indonesia sekarang?</code>"
        )
        return

    message = " ".join(context.args)
    logger.info(
        f"[📥 /tanya] {user.full_name} ({user.id}) di {chat_type} bertanya: {message}"
    )

    # Kirim pesan tunggu
    waiting_msg = await update.message.reply_text(
        "⏳ Mohon tunggu, sedang memproses pertanyaanmu..."
    )

    try:
        ai = MetaAI()
        result = ai.prompt(message=message)
        logger.info(f"[✅ /tanya] Meta AI response len={len(str(result))}")

        msg = (
            result.get("message", "❌ Tidak ada jawaban yang tersedia.")
            .replace("\\n", "\n")
            .strip()
        )
        logger.debug(f"[✅ /tanya] Meta AI response message: {msg[:500]}")

        # Respons dengan mention (terlihat di grup)
        response = (
            f"🤖 <b>Jawaban dari Meta AI</b>\n\n"
            f"👤 Ditanyakan oleh: {user_mention}\n\n"
            f"{msg}"
        )
        await update.message.reply_html(response, disable_web_page_preview=True)

    except Exception as e:
        logger.error("[❌ /tanya] Error memproses pertanyaan", exc_info=True)
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat memproses pertanyaan."
        )
    finally:
        await waiting_msg.delete()


def register_handler(app):
    app.add_handler(CommandHandler("tanya", tanya_meta))
