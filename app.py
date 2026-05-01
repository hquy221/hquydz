import telebot
import threading
from flask import Flask
import time
import requests

# --- CẤU HÌNH HỆ THỐNG ---
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

VALID_TOKENS = []
ADMIN_LIST = [7153197678] 
is_spaming = False
spam_delay = 0.1 
app = Flask('')

@app.route('/')
def home(): return "ULTIMATE SWARM V27 - ONLINE"

# --- VĂN BẢN TẢNG ĐÁ (FULL 3X - KHÔNG RÚT GỌN) ---
LAG_TEXT = """
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
జ్ఞాజ్ఞాజ్ఞాజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
జ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞaజ్ఞa
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
m chay dau cho thoat khoi tay cha hquy=))=)) sua len di con dix mồ côi=))=))
slow vcl e ơi mồ côi gáy gắt lên=))=)) m yeu ot z tk nfu học đòi war bot=))=))
cay lam dung k nhìn màn hình nhảy chữ đi=))=)) cay di e cay di e cmm tk nfu=))=))
cmm nfu nfu nfu mồ côi sủa gắt=))=)) choa sua tiep di bố m đang đợi m đây=))=))
bố m vả nát gáo m nè con dog mồ côi gáy lên=))=))
m chay dau cho thoat khoi tay cha hquy=))=)) sua len di con dix mồ côi=))=))
slow vcl e ơi mồ côi gáy gắt lên=))=)) m yeu ot z tk nfu học đòi war bot=))=))
cay lam dung k nhìn màn hình nhảy chữ đi=))=)) cay di e cay di e cmm tk nfu=))=))
cmm nfu nfu nfu mồ côi sủa gắt=))=)) choa sua tiep di bố m đang đợi m đây=))=))
bố m vả nát gáo m nè con dog mồ côi gáy lên=))=))
m chay dau cho thoat khoi tay cha hquy=))=)) sua len di con dix mồ côi=))=))
slow vcl e ơi mồ côi gáy gắt lên=))=)) m yeu ot z tk nfu học đòi war bot=))=))
cay lam dung k nhìn màn hình nhảy chữ đi=))=)) cay di e cay di e cmm tk nfu=))=))
cmm nfu nfu nfu mồ côi sủa gắt=))=)) choa sua tiep di bố m đang đợi m đây=))=))
bố m vả nát gáo m nè con dog mồ côi gáy lên=))=))
"""

# --- CÔNG NHÂN SPAM (XẢ TỨC THÌ) ---
def start_worker(tk, chat_id, mode, custom_text, target_tag):
    bot = telebot.TeleBot(tk)
    while is_spaming:
        try:
            if mode == 'lag': bot.send_message(chat_id, LAG_TEXT)
            elif mode == 'dai': bot.send_message(chat_id, WAR_TEXT)
            elif mode == 'tag': 
                tag_content = (f"{target_tag} sua de con choa mo coi=))=))\n" * 50)
                bot.send_message(chat_id, tag_content)
            elif mode == 'custom': bot.send_message(chat_id, custom_text)
            time.sleep(spam_delay)
        except:
            time.sleep(0.5)

def trigger_all(chat_id, mode, custom_text="", target_tag=""):
    global is_spaming
    is_spaming = True
    for t in VALID_TOKENS:
        threading.Thread(target=start_worker, args=(t, chat_id, mode, custom_text, target_tag), daemon=True).start()

# --- CHỈ HUY MASTER (ĐẦY ĐỦ LỆNH) ---
def master_listener(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(func=lambda m: m.from_user.id in ADMIN_LIST)
    def handle(m):
        global is_spaming, spam_delay
        cmd = m.text.lower()

        # NHÓM LỆNH CHIẾN ĐẤU (0.1S TRIGGER)
        if cmd == '/splag':
            trigger_all(m.chat.id, 'lag')
            bot.send_message(m.chat.id, "🌪️ SWARM LAG ON!")

        elif cmd == '/spdai':
            trigger_all(m.chat.id, 'dai')
            bot.send_message(m.chat.id, "🔥 SWARM WAR ON!")

        elif cmd.startswith('/sptag '):
            target = m.text.split(' ')[1]
            trigger_all(m.chat.id, 'tag', target_tag=target)
            bot.send_message(m.chat.id, f"🎯 TARGETING: {target}")

        elif cmd.startswith('/spam '):
            trigger_all(m.chat.id, 'custom', custom_text=m.text[6:])
            bot.send_message(m.chat.id, "🚀 CUSTOM ON")

        elif cmd == '/dung':
            is_spaming = False
            bot.send_message(m.chat.id, "🛑 ALL STOPPED.")

        # NHÓM LỆNH HỆ THỐNG
        elif cmd == '/info':
            bot.reply_to(m, f"👤 ID: `{m.from_user.id}`\n🤖 Bots Live: {len(VALID_TOKENS)}\n⚡ Delay: {spam_delay}s", parse_mode="Markdown")

        elif cmd == '/list':
            bot.reply_to(m, f"✅ Sẵn sàng {len(VALID_TOKENS)} bốt.")

        elif cmd.startswith('/setdelay '):
            try:
                spam_delay = float(m.text.split(' ')[1])
                bot.reply_to(m, f"⚡ Delay set: {spam_delay}s")
            except: pass

        elif cmd.startswith('/addadm '):
            try:
                new_id = int(m.text.split(' ')[1])
                if new_id not in ADMIN_LIST: ADMIN_LIST.append(new_id)
                bot.reply_to(m, f"✅ Thêm Admin: {new_id}")
            except: pass

        elif cmd.startswith('/xoaadm '):
            try:
                rem_id = int(m.text.split(' ')[1])
                if rem_id in ADMIN_LIST and rem_id != 7153197678: 
                    ADMIN_LIST.remove(rem_id)
                    bot.reply_to(m, f"❌ Xóa Admin: {rem_id}")
            except: pass

        elif cmd == '/help':
            h = "LỆNH:\n/splag, /spdai, /sptag, /spam, /info, /list, /setdelay, /addadm, /xoaadm, /dung"
            bot.reply_to(m, h)

    bot.infinity_polling(timeout=10, skip_pending=True)

# --- KHỞI TẠO VÀ LỌC TOKEN CHẾT ---
def init():
    global VALID_TOKENS
    print("--- ĐANG LỌC TOKEN ---")
    for t in RAW_TOKENS:
        try:
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=2).json()
            if r.get("ok"): VALID_TOKENS.append(t)
        except: pass
    
    if VALID_TOKENS:
        # Chọn con Bot sống đầu tiên làm Chỉ huy
        threading.Thread(target=master_listener, args=(VALID_TOKENS[0],), daemon=True).start()
        print(f"--- ĐÃ KÍCH HOẠT {len(VALID_TOKENS)} BOT ---")

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    init()
    while True: time.sleep(2)
