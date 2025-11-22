# 🇰🇷 Minsu Bot (EPS-TOPIK Helper)

Bot Telegram ringan untuk komunitas EPS-TOPIK Indonesia. Fitur yang dipertahankan:

- 🔎 `/cek <nomor ujian>` — cek hasil CBT EPS-TOPIK dengan guard topik.
- 📊 `/eps` — pantau progress EPS di DM (perlu whitelist di `.env` atau `config/eps_accounts.json`).
- 🤖 `/tanya <pertanyaan>` — tanya Meta AI.
- 🆔 `/cek_id` — lihat ID chat & thread untuk konfigurasi.
- 💬 Balas/mention bot — bot memberi respon ringan dari `data/respon.json`.

## Persiapan Cepat
1) **Buat `.env`** (minimal):
```env
BOT_TOKEN=isi_token_bot_anda
MY_TELEGRAM_ID=123456789        # pemilik, bisa jalankan command di DM
EPS_USER=123456789,987654321    # ID yang boleh pakai /eps (opsional)
```

2) **Install dependencies**
```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python -m playwright install chromium  # diperlukan untuk modul EPS core
```
Pastikan Chrome/Chromium dan ChromeDriver tersedia di PATH untuk `/cek`.

3) **Siapkan data pendukung**
- `config/eps_accounts.json` → kredensial EPS bawaan untuk `/eps` (opsional; format contoh berada di file itu).
- `data/topik_ids.json` → mapping command ke thread ID. Minimal isi `{ "cek": <thread_id> }`.

4) **Jalankan bot**
```bash
python bot.py
```

### Catatan
- Log otomatis tersimpan di folder `logs/`.
- Command berat (cek ujian & EPS) memakai Playwright/Selenium, jadi pastikan dependensi tersebut siap sebelum deploy.
# Nichanan-bot
