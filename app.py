import telebot
import threading
from flask import Flask
import time
import requests
import itertools
import sys

# --- HỆ THỐNG CẤU HÌNH TRUNG TÂM ---
RAW_TOKENS = [
    '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18', '8481938728:AAGen1t8Tz3jeu02kJ8HoCIZLiPLdd687n8',
    '8739448460:AAGNLEW-WDvatbxmPLzkziG5jpd5hTRfqiE', '8689807630:AAEoXvm45QaW1jlT-H_KzNlmCpu50Q3k2S4',
    '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0',
    '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0',
    '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c',
    '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM',
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA',
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0',
    '8650032681:AAE9TeiIlywG796f6hHLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0',
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY',
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4',
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

VALID_BOTS = []
DEAD_TOKENS = []
ADMIN_LIST = [7153197678] # ID Admin gốc
DELAY_TIME = 0.05
stop_event = threading.Event()
app = Flask(__name__)

# --- CƠ CHẾ LỌC TOKEN SỐNG/CHẾT ---
def filter_tokens():
    global VALID_BOTS, DEAD_TOKENS
    print("--- [SYSTEM] ĐANG KIỂM TRA QUÂN SỐ BOT ---")
    VALID_BOTS.clear()
    DEAD_TOKENS.clear()
    for t in RAW_TOKENS:
        try:
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=5).json()
            if r.get("ok"):
                bot = telebot.TeleBot(t)
                bot.username = r['result']['username']
                VALID_BOTS.append(bot)
            else:
                DEAD_TOKENS.append(t)
        except:
            DEAD_TOKENS.append(t)
    print(f"--- [SYSTEM] HOÀN TẤT: {len(VALID_BOTS)} SỐNG, {len(DEAD_TOKENS)} CHẾT ---")

# --- BỘ MÁY TẠO VĂN BẢN (KHÔNG DẤU NHÂN) ---
def build_long_text(base_text, lines=1000):
    result = []
    cycle = itertools.cycle(base_text.split())
    for i in range(lines):
        line = " ".join([next(cycle) for _ in range(10)])
        result.append(f"[{i}] {line}")
    return "\n".join(result)

# --- ENGINE SPAM ĐA LUỒNG ---
def spam_worker(chat_id, mode, content="", target_id=None):
    if not VALID_BOTS: return
    bot_cycle = itertools.cycle(VALID_BOTS)
    
    # Chuẩn bị nội dung
    if mode == 'spnd':
        final_msg = build_long_text(content)
        parse = None
    elif mode == 'sptag':
        final_msg = f"[{content}](tg://user?id={target_id})"
        parse = "Markdown"
    elif mode == 'spam':
        final_msg = content
        parse = None

    while not stop_event.is_set():
        current_bot = next(bot_cycle)
        try:
            current_bot.send_message(chat_id, final_msg, parse_mode=parse)
            time.sleep(DELAY_TIME)
        except: continue

# --- HỆ THỐNG LỆNH CHỈ HUY ---
def start_master():
    if not VALID_BOTS: return
    master = VALID_BOTS[0] # Con bot đầu tiên làm chỉ huy

    @master.message_handler(commands=['help'])
    def cmd_help(m):
        if m.from_user.id not in ADMIN_LIST: return
        text = (
            "🆘 --- DANH SÁCH LỆNH CHỈ HUY ---\n\n"
            "🚀 **SPAM TRỌNG TÂM:**\n"
            "/spnd [nội dung] - Spam nội dung kéo dài (1000 dòng)\n"
            "/sptag [ID] [nội dung] - Tag tên mục tiêu liên tục\n"
            "/spam [nội dung] - Spam tin nhắn ngắn liên tục\n"
            "/stop - Dừng mọi hoạt động tấn công\n\n"
            "⚙️ **QUẢN TRỊ HỆ THỐNG:**\n"
            "/info - Kiểm tra tình trạng bầy bot\n"
            "/list - Danh sách các bot đang hoạt động\n"
            "/setdelay [số] - Chỉnh tốc độ spam (giây)\n\n"
            "👤 **QUẢN LÝ ADMIN:**\n"
            "/listadm - Xem danh sách admin\n"
            "/addadm [ID] - Thêm admin mới\n"
            "/xoaadm [ID] - Xoá quyền admin"
        )
        master.reply_to(m, text, parse_mode="Markdown")

    @master.message_handler(func=lambda m: True)
    def handle_all(m):
        global DELAY_TIME
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        # --- NHÓM LỆNH SPAM ---
        if cmd == '/spnd':
            if len(args) < 2: return master.reply_to(m, "Thiếu nội dung!")
            stop_event.clear()
            for _ in range(3): threading.Thread(target=spam_worker, args=(m.chat.id, 'spnd', m.text[6:]), daemon=True).start()
            master.reply_to(m, "🌪️ ĐANG XẢ 1000 DÒNG BIẾN THẾ!")

        elif cmd == '/sptag':
            if len(args) < 3: return master.reply_to(m, "Cú pháp: /sptag [ID] [Nội dung]")
            stop_event.clear()
            threading.Thread(target=spam_worker, args=(m.chat.id, 'sptag', " ".join(args[2:]), args[1]), daemon=True).start()
            master.reply_to(m, f"🎯 ĐANG TAG MỤC TIÊU {args[1]}")

        elif cmd == '/spam':
            if len(args) < 2: return master.reply_to(m, "Thiếu nội dung!")
            stop_event.clear()
            for _ in range(2): threading.Thread(target=spam_worker, args=(m.chat.id, 'spam', m.text[6:]), daemon=True).start()
            master.reply_to(m, "🔥 ĐANG SPAM LIÊN TỤC!")

        elif cmd == '/stop':
            stop_event.set()
            master.reply_to(m, "🛑 ĐÃ DỪNG QUÂN ĐOÀN.")

        # --- NHÓM LỆNH HỆ THỐNG ---
        elif cmd == '/info':
            msg = (
                f"📊 **TÌNH TRẠNG QUÂN ĐOÀN:**\n"
                f"✅ Bot đang sống: {len(VALID_BOTS)}\n"
                f"❌ Bot đã chết: {len(DEAD_TOKENS)}\n"
                f"⚡ Delay hiện tại: {DELAY_TIME}s"
            )
            master.reply_to(m, msg, parse_mode="Markdown")

        elif cmd == '/list':
            bot_names = "\n".join([f"@{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 **DANH SÁCH BOT:**\n{bot_names}", parse_mode="Markdown")

        elif cmd == '/setdelay':
            try:
                DELAY_TIME = float(args[1])
                master.reply_to(m, f"⚡ Đã chỉnh delay thành: {DELAY_TIME}s")
            except: master.reply_to(m, "Sai định số!")

        # --- NHÓM LỆNH ADMIN ---
        elif cmd == '/listadm':
            master.reply_to(m, f"👥 **DANH SÁCH ADMIN:**\n`{ADMIN_LIST}`", parse_mode="Markdown")

        elif cmd == '/addadm':
            try:
                new_id = int(args[1])
                if new_id not in ADMIN_LIST:
                    ADMIN_LIST.append(new_id)
                    master.reply_to(m, f"✅ Đã thêm {new_id} làm admin.")
            except: master.reply_to(m, "ID không hợp lệ!")

        elif cmd == '/xoaadm':
            try:
                rem_id = int(args[1])
                if rem_id in ADMIN_LIST:
                    ADMIN_LIST.remove(rem_id)
                    master.reply_to(m, f"❌ Đã xoá admin {rem_id}.")
            except: master.reply_to(m, "ID không hợp lệ!")

    print(f"--- [MASTER] @{master.username} ĐANG CHỈ HUY ---")
    master.infinity_polling(skip_pending=True)

# --- VẬN HÀNH ---
@app.route('/')
def home(): return f"BOT MASTER ACTIVE: {len(VALID_BOTS)} BOTS ONLINE"

if __name__ == "__main__":
    filter_tokens()
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080), daemon=True).start()
    start_master()
