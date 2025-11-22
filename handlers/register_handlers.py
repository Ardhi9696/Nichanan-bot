# register_handlers.py
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers.command_wrapper import with_cooldown

# Heavy commands
from handlers_heavy.cek_ujian import cek_ujian  # /cek (nomor ujian)
from handlers_heavy.get_eps import eps_command  # /eps atau /e (progress EPS)
from handlers_heavy.tanya_meta import tanya_meta


def register_handlers(app: Application):
    # Hanya command berat + utilitas dasar
    app.add_handler(CommandHandler("cek", with_cooldown(cek_ujian)))
    app.add_handler(CommandHandler(["eps", "e"], eps_command))
    app.add_handler(CommandHandler("tanya", with_cooldown(tanya_meta)))

    # Responder di-nonaktifkan (biar handled oleh bot lain)
