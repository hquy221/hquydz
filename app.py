import telebot
import time
from flask import Flask
from threading import Thread

# --- CẤU HÌNH ĐỊNH DANH TUYỆT ĐỐI ---
ID_CHU_BOT = 7153197678  
ADMINS = [7153197678]

TOKENS = [
    '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', 
    '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0', 
    '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c', 
    '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM', 
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', 
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', 
    '8650032681:AAE9TeiIlywG796f6hKLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', 
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', 
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbIztbNZZtni7D0uDl4', 
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o', '8745047343:AAF3XKrSHnGHujBv94a2GeYXweXgIFMEFVs'
]

delay_spam = 0.5
dang_spam = False

# VĂN BẢN LAG (ĐÃ KÉO DÀI GẤP 3 LẦN BẢN CŨ)
LAG_TXT = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ " * 200
DAI_TXT = "Văn bản dài test hệ thống... " * 300

app = Flask(__name__)
@app.route('/')
def home(): return "Bot System Online - Master: 7153197678"
def run_flask(): app.run(host='0.0.0.0', port=8080)

def setup_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['help'])
    def help_cmd(m):
        msg = ("📜 HỆ THỐNG SPAM LAG:\n"
               "/spam [nội dung] - Spam văn bản tùy chỉnh\n"
               "/splag - Thả bom LAG SIÊU CẤP (Văn bản dài)\n"
               "/spdai - Spam văn bản cực dài\n"
               "/dung - Dừng ngay lập tức\n"
               "/setdelay [giây] - Chỉnh tốc độ\n"
               "/list - Danh sách Admin\n"
               "/addadm [ID] - Thêm Admin (Chủ bot)\n"
               "/xoaadm [ID] - Xóa Admin (Chủ bot)\n"
               "/info - Kiểm tra trạng thái")
        bot.reply_to(m, msg)

    @bot.message_handler(commands=['list'])
    def list_cmd(m):
        if m.from_user.id in ADMINS:
            bot.reply_to(m, f"👥 Admins: {ADMINS}")

    @bot.message_handler(commands=['addadm'])
    def addadm_cmd(m):
        if m.from_user.id == 7153197678:
            try:
                new_id = int(m.text.split()[1])
                if new_id not in ADMINS:
                    ADMINS.append(new_id)
                    bot.reply_to(m, f"✅ Đã thêm {new_id} làm Admin.")
            except: bot.reply_to(m, "❌ HD: /addadm [ID]")

    @bot.message_handler(commands=['xoaadm'])
    def xoaadm_cmd(m):
        if m.from_user.id == 7153197678:
            try:
                old_id = int(m.text.split()[1])
                if old_id in ADMINS and old_id != 7153197678:
                    ADMINS.remove(old_id)
                    bot.reply_to(m, f"🗑️ Đã xóa Admin {old_id}.")
                else: bot.reply_to(m, "❌ Không thể xóa ID này!")
            except: bot.reply_to(m, "❌ HD: /xoaadm [ID]")

    @bot.message_handler(commands=['setdelay'])
    def setdelay_cmd(m):
        global delay_spam
        if m.from_user.id in ADMINS:
            try:
                delay_spam = float(m.text.split()[1])
                bot.reply_to(m, f"⏱️ Delay hiện tại: {delay_spam}s")
            except: bot.reply_to(m, "❌ HD: /setdelay [giây]")

    @bot.message_handler(commands=['splag'])
    def splag_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            dang_spam = True
            bot.reply_to(m, "⚠️ ĐANG KÍCH HOẠT BOM LAG SIÊU CẤP...")
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, LAG_TXT)
                    time.sleep(delay_spam)
                except: time.sleep(1)

    @bot.message_handler(commands=['spdai'])
    def spdai_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            dang_spam = True
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, DAI_TXT)
                    time.sleep(delay_spam)
                except: time.sleep(1)

    @bot.message_handler(commands=['spam'])
    def spam_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            content = m.text.replace('/spam', '').strip() or "System Overload..."
            dang_spam = True
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, content)
                    time.sleep(delay_spam)
                except: time.sleep(1)

    @bot.message_handler(commands=['dung'])
    def dung_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            dang_spam = False
            bot.reply_to(m, "🛑 STOPPED!")

    @bot.message_handler(commands=['info'])
    def info_cmd(m):
        if m.from_user.id in ADMINS:
            bot.reply_to(m, f"ℹ️ Hệ thống: {len(TOKENS)} Bots Online\n👤 Chủ: `7153197678`\n⚡ Tốc độ: {delay_spam}s")

    bot.polling(none_stop=True)

if __name__ == '__main__':
    Thread(target=run_flask).start()
    for token in TOKENS:
        Thread(target=setup_bot, args=(token,)).start()
