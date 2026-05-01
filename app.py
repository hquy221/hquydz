import telebot
import threading
from flask import Flask
import time
import requests
import itertools
import os
import random

# --- HỆ THỐNG TOKEN ---
RAW_TOKENS = [
    '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18', '8481938728:AAGen1t8Tz3jeu02kJ8HoCIZLiPLdd687n8',
    '8739448460:AAGNLEW-WDvatbxmPLzkziG5jpd5hTRfqiE', '8689807630:AAEoXvm45QaW1jlT-H_KzNlmCpu50Q3k2S4',
    '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0',
    '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0',
    '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c',
    '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM',
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA',
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0',
    '8650032681:AAE9TeiIIywG796f6hHLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0',
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY',
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4',
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

VALID_BOTS = []
ADMIN_LIST = [7153197678] 
DELAY_TIME = 0.05
stop_event = threading.Event()
app = Flask(__name__)

# --- ANTI-BAN SHIELD ---
def anti_ban_content(text):
    """Lách luật Telegram bằng ký tự tàng hình"""
    noise = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))
    return f"{text} {noise}"

# --- TỰ ĐỘNG LỌC TOKEN CHẾT ---
def filter_system():
    global VALID_BOTS
    VALID_BOTS.clear()
    for t in RAW_TOKENS:
        try:
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=3).json()
            if r.get("ok"):
                bot = telebot.TeleBot(t)
                bot.username = r['result']['username']
                bot.id = r['result']['id']
                VALID_BOTS.append(bot)
        except: continue

# --- ENGINE SPAM ĐIỀU PHỐI ---
def run_spam(chat_id, mode, content="", target_id=None):
    if not VALID_BOTS: return
    cycle = itertools.cycle(VALID_BOTS)
    while not stop_event.is_set():
        bot = next(cycle)
        try:
            msg = anti_ban_content(content)
            p_mode = None
            if mode == 'sptag':
                msg = anti_ban_content(f"[{content}](tg://user?id={target_id})")
                p_mode = "Markdown"
            elif mode == 'spnd':
                msg = anti_ban_content("\n".join([f"[{i}] {content}" for i in range(50)]))
            
            bot.send_message(chat_id, msg, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except Exception as e:
            if "retry after" in str(e).lower(): time.sleep(10)
            continue

# --- MASTER CONTROL (ADMIN) ---
def start_master():
    if not VALID_BOTS: return
    # Con bot đầu tiên trong danh sách sống sẽ làm Chỉ huy
    master = VALID_BOTS[0]

    @master.message_handler(func=lambda m: True)
    def handle_commands(m):
        global DELAY_TIME
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        # --- LỆNH TẤN CÔNG ---
        if cmd in ['/spnd', '/spam']:
            stop_event.clear()
            threading.Thread(target=run_spam, args=(m.chat.id, cmd[1:], m.text[6:]), daemon=True).start()
            master.reply_to(m, "🚀 KHỞI ĐỘNG QUÂN ĐOÀN!")

        elif cmd == '/sptag':
            if len(args) < 3: return
            stop_event.clear()
            threading.Thread(target=run_spam, args=(m.chat.id, 'sptag', " ".join(args[2:]), args[1]), daemon=True).start()

        elif cmd == '/dung': # ĐÃ THAY ĐỔI TẠI ĐÂY
            stop_event.set()
            master.reply_to(m, "🛑 ĐÃ DỪNG SPAM.")

        # --- LỆNH THÔNG TIN ---
        elif cmd == '/help':
            master.reply_to(m, "🔥 `/spnd /sptag /spam /dung` \n📊 `/infobot /info /listbot /listadm` \n⚙️ `/setdelay /addadm /xoaadm`")

        elif cmd == '/infobot':
            master.reply_to(m, f"🤖 ID Bot Chỉ Huy: `{master.id}`", parse_mode="Markdown")

        elif cmd == '/info':
            tid = m.reply_to_message.from_user.id if m.reply_to_message else (args[1] if len(args)>1 else m.from_user.id)
            master.reply_to(m, f"🆔 User ID tra cứu: `{tid}`", parse_mode="Markdown")

        elif cmd == '/listbot':
            list_b = "\n".join([f"✅ @{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 **Bots sống ({len(VALID_BOTS)}):**\n{list_b}", parse_mode="Markdown")

        elif cmd == '/listadm':
            master.reply_to(m, f"👥 **Admins:** `{ADMIN_LIST}`", parse_mode="Markdown")

        elif cmd == '/setdelay': 
            try: DELAY_TIME = float(args[1])
            except: pass

        elif cmd == '/addadm':
            try:
                nid = int(args[1])
                if nid not in ADMIN_LIST: ADMIN_LIST.append(nid)
            except: pass

        elif cmd == '/xoaadm':
            try: ADMIN_LIST.remove(int(args[1]))
            except: pass

    master.infinity_polling(timeout=20, skip_pending=True)

@app.route('/')
def home(): return "SYSTEM ONLINE"

if __name__ == "__main__":
    filter_system() # Tự động lọc bot chết/sai khi khởi động
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master()
        except: time.sleep(5) # Tự hồi sinh sau 5s nếu sập
