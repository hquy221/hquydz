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
ADMIN_LIST = [7153197678] # ID Admin mặc định
DELAY_TIME = 0.05
stop_event = threading.Event()
app = Flask(__name__)

# --- CÔNG CỤ TỰ ĐỘNG ---
def anti_ban_noise(text):
    """Chèn ký tự tàng hình để vượt mặt hệ thống quét của Telegram"""
    noise = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))
    return f"{text} {noise}"

def filter_dead_bots():
    """Tự động kiểm tra token sai/chết khi khởi động"""
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

# --- ENGINE ĐIỀU PHỐI QUÂN ĐOÀN ---
def spam_worker(chat_id, mode, content="", target_id=None):
    if not VALID_BOTS: return
    bot_cycle = itertools.cycle(VALID_BOTS)
    
    while not stop_event.is_set():
        current_bot = next(bot_cycle)
        try:
            msg = anti_ban_noise(content)
            p_mode = None
            if mode == 'sptag':
                msg = anti_ban_noise(f"[{content}](tg://user?id={target_id})")
                p_mode = "Markdown"
            elif mode == 'spnd':
                msg = anti_ban_noise("\n".join([f"[{i}] {content}" for i in range(50)]))
            
            current_bot.send_message(chat_id, msg, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except Exception as e:
            if "retry after" in str(e).lower(): time.sleep(5)
            continue

# --- MASTER CONTROL (ADMIN COMMANDS) ---
def start_master_bot():
    if not VALID_BOTS: return
    # Con bot đầu tiên trong danh sách hợp lệ sẽ làm "Chỉ huy trưởng"
    master = VALID_BOTS[0]

    @master.message_handler(func=lambda m: True)
    def handle_all_commands(m):
        global DELAY_TIME
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        # --- LỆNH QUẢN TRỊ ---
        if cmd == '/listbot':
            list_msg = "\n".join([f"🤖 @{b.username} (`{b.id}`)" for b in VALID_BOTS])
            master.reply_to(m, f"✅ **Danh sách bot đang sống ({len(VALID_BOTS)}):**\n{list_msg}", parse_mode="Markdown")

        elif cmd == '/setdelay':
            try:
                val = float(args[1])
                if 0.001 <= val <= 2.5:
                    DELAY_TIME = val
                    master.reply_to(m, f"⚡ Đã chỉnh delay spam thành: `{DELAY_TIME}s`", parse_mode="Markdown")
                else:
                    master.reply_to(m, "❌ Delay chỉ được trong khoảng `0.001` đến `2.5` giây.")
            except: master.reply_to(m, "❌ Sai cú pháp. Ví dụ: `/setdelay 0.1`")

        elif cmd == '/addadm':
            try:
                new_id = int(args[1])
                if new_id not in ADMIN_LIST:
                    ADMIN_LIST.append(new_id)
                    master.reply_to(m, f"✅ Đã cấp quyền Admin cho: `{new_id}`", parse_mode="Markdown")
            except: master.reply_to(m, "❌ Sai cú pháp. Ví dụ: `/addadm 123456789`")

        elif cmd == '/xoaadm':
            try:
                rem_id = int(args[1])
                if rem_id in ADMIN_LIST and rem_id != 7153197678: # Không cho xóa admin gốc
                    ADMIN_LIST.remove(rem_id)
                    master.reply_to(m, f"❌ Đã gỡ quyền Admin của: `{rem_id}`", parse_mode="Markdown")
            except: master.reply_to(m, "❌ Sai cú pháp. Ví dụ: `/xoaadm 123456789`")

        # --- LỆNH TẤN CÔNG & THÔNG TIN ---
        elif cmd == '/spnd':
            stop_event.clear()
            threading.Thread(target=spam_worker, args=(m.chat.id, 'spnd', m.text[6:]), daemon=True).start()

        elif cmd == '/sptag':
            if len(args) < 3: return
            stop_event.clear()
            threading.Thread(target=spam_worker, args=(m.chat.id, 'sptag', " ".join(args[2:]), args[1]), daemon=True).start()

        elif cmd == '/spam':
            stop_event.clear()
            threading.Thread(target=spam_worker, args=(m.chat.id, 'spam', m.text[6:]), daemon=True).start()

        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🛑 ĐÃ DỪNG TOÀN QUÂN.")

        elif cmd == '/info':
            target_id = m.reply_to_message.from_user.id if m.reply_to_message else (args[1] if len(args)>1 else m.from_user.id)
            master.reply_to(m, f"🆔 ID Người này: `{target_id}`", parse_mode="Markdown")

        elif cmd == '/help':
            msg = (
                "🚀 **LỆNH TẤN CÔNG:**\n"
                "`/spnd [nội dung]` / `/sptag [ID] [nội dung]` / `/spam [nội dung]` / `/dung`\n\n"
                "⚙️ **LỆNH QUẢN TRỊ:**\n"
                "`/listbot` - Xem bầy bot sống\n"
                "`/setdelay [0.001-2.5]` - Chỉnh tốc độ\n"
                "`/addadm [ID]` - Thêm Admin quản lý\n"
                "`/xoaadm [ID]` - Xoá Admin\n"
                "`/info` - Xem ID người dùng"
            )
            master.reply_to(m, msg, parse_mode="Markdown")

    master.infinity_polling(timeout=20, skip_pending=True)

@app.route('/')
def home(): return "BOT CLUSTER ONLINE"

if __name__ == "__main__":
    filter_dead_bots() # Lọc bot trước khi chạy
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master_bot()
        except: time.sleep(5)
