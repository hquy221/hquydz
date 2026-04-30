import telebot
import time
from flask import Flask
from threading import Thread

# --- CẤU HÌNH ID CHỦ BOT: 7153197678 ---
ID_CHU_BOT = 7153197678  
ADMINS = [7153197678]
# Danh sách Token (Hãy chắc chắn các Token này còn sống)
TOKENS = ['8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0', '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c', '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM', '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', '8650032681:AAE9TeiIlywG796f6hKLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbIztbNZZtni7D0uDl4', '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o', '8745047343:AAF3XKrSHnGHujBv94a2GeYXweXgIFMEFVs']

delay_spam = 0.5
dang_spam = False

LAG_TXT = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃰ ꙰꙰⃟꙰⃟꙰⃟꙰⃰ ꙰꙰⃟꙰⃟꙰⃟꙰kk ꙰꙰⃟꙰"

DAI_TXT = """[Văn bản dài của ông]""" # Chỗ này ông tự dán đoạn văn dài vào nhé

app = Flask('')
@app.route('/')
def home(): return "CHA HQUY ONLINE 🚀"

def setup_bot(token):
    try:
        bot = telebot.TeleBot(token)
        
        @bot.message_handler(commands=['help'])
        def help(m):
            bot.reply_to(m, "🚀 /spam | 💥 /splag | 📜 /spdai\n🛑 /dung | ⚡ /setdelay\nℹ️ /info | ➕ /addadm | ➖ /xoaadm")

        @bot.message_handler(commands=['addadm'])
        def add_ad(m):
            if m.from_user.id == 7153197678:
                try:
                    new_id = int(m.text.split()[1])
                    if new_id not in ADMINS:
                        ADMINS.append(new_id)
                        bot.reply_to(m, f"✅ Admin: {new_id}")
                except: pass

        @bot.message_handler(commands=['xoaadm'])
        def del_ad(m):
            if m.from_user.id == 7153197678:
                try:
                    old_id = int(m.text.split()[1])
                    if old_id in ADMINS and old_id != 7153197678:
                        ADMINS.remove(old_id)
                        bot.reply_to(m, f"🗑 Xóa Admin: {old_id}")
                except: pass

        @bot.message_handler(commands=['info'])
        def send_info(m):
            bot.reply_to(m, f"🤖 Live | Delay: {delay_spam}s | Admin: {len(ADMINS)}")

        @bot.message_handler(commands=['splag'])
        def start_lag(m):
            global dang_spam
            if m.from_user.id in ADMINS:
                dang_spam = True
                bot.reply_to(m, "🔥 BẮT ĐẦU SPAM LAG!")
                while dang_spam:
                    try: 
                        bot.send_message(m.chat.id, LAG_TXT)
                        time.sleep(delay_spam)
                    except Exception as e:
                        print(f"Lỗi gửi tin: {e}")
                        time.sleep(1)

        @bot.message_handler(commands=['spam'])
        def start_spam(m):
            global dang_spam
            if m.from_user.id in ADMINS:
                c = m.text.replace('/spam', '').strip()
                if not c: return
                dang_spam = True
                bot.reply_to(m, "🔥 CHA HQUY SPAM")
                while dang_spam:
                    try: bot.send_message(m.chat.id, c); time.sleep(delay_spam)
                    except: time.sleep(1)

        @bot.message_handler(commands=['spdai'])
        def start_dai(m):
            global dang_spam
            if m.from_user.id in ADMINS:
                dang_spam = True
                bot.reply_to(m, DAI_TXT)
                while dang_spam:
                    try: bot.send_message(m.chat.id, DAI_TXT); time.sleep(delay_spam)
                    except: time.sleep(1)

        @bot.message_handler(commands=['dung'])
        def stop(m):
            global dang_spam
            if m.from_user.id in ADMINS:
                dang_spam = False
                bot.reply_to(m, "🛑 DỪNG LẠI!")

        bot.polling(none_stop=True)
    except: pass

if __name__ == "__main__":
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    for t in TOKENS: Thread(target=setup_bot, args=(t,)).start(); time.sleep(0.4)
                
