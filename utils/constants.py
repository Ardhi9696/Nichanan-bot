import os

DATA_DIR = "data"

# Hanya tiga file data yang masih dipakai:
# - cache_eps.json : cache hasil cek ujian EPS (/cek)
# - respon.json    : kumpulan respon ringan untuk simple_responder
# - topik_ids.json : mapping thread ID untuk guard command
EPS_DATA = os.path.join(DATA_DIR, "cache_eps.json")
RESPON_FILE = os.path.join(DATA_DIR, "respon.json")
TOPIK_ID = os.path.join(DATA_DIR, "topik_ids.json")
