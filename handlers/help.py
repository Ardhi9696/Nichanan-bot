from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
📖 *Bantuan Singkat Nichanan Bot*  
Perintah yang tersedia saat ini:

🔎 *Cek Hasil CBT EPS-TOPIK*  
/cek [nomor ujian] – Cek hasil CBT berdasarkan nomor ujian  
Contoh: `/cek 012202512345678`

📊 *Pantau Progress EPS (DM saja, whitelist)*  
/eps [opsional: USER PASS TGL] – Ambil progress EPS. Tanpa argumen akan memakai akun yang terdaftar.

💬 *Tanya AI (Meta)*  
/tanya [pertanyaan] – Ajukan pertanyaan ke Meta AI  
Contoh: `/tanya Siapa presiden Korea?`

ℹ️ *Info*  
/help – Tampilkan bantuan ini  
Reply/mention bot – Bot akan membalas dengan respon ringan sesuai konteks.
        """,
        parse_mode="Markdown",
    )
