import telebot
import time
from flask import Flask
from threading import Thread

# --- CẤU HÌNH ĐỊNH DANH (ĐÃ THAY ID CỦA ÔNG) ---
ID_CHU_BOT = 7153197678  
ADMINS = [7153197678] # ID của ông nằm trong danh sách Admin mặc định

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

# --- VĂN BẢN LAG (Khối ký tự đặc biệt) ---
LAG_TXT = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ " * 50

# --- VĂN BẢN /SPDAI (Nội dung dài dồn dập, không dùng *) ---
DAI_TXT = (
    "alo alo cn choa ei mau ti k mau de mau de mau de tk nfu ei m cham vl m bia ro m yeu ot vcl "
    "tk nfu ei m ga vl lun e alo alo sao ay nhi anh lai win a uoc loser ma tk nfu ei slow k ay "
    "cn cho speed lun e toi die k e mau me m di tk cho nfu m ot bo ro m bia a con gi khac k "
    "tk ga ei mau k e anh win cmnr sua e mau e mau de tk ga m cham a m cham ro m bia a "
    "tk nfu ei mau k e mau de alo alo cn choa ei mau ti k mau me m di tk cho nfu a đấng hot war mà "
    "cmm chối à a hw mẹ r con gi dau ma noi a treo co me m ma a win ma m bia a tk nfu ri m ngu v "
    "ngu ro lun e bia a e le de alo s do m sao m chạy a mà m bịa à tk nu cmm sua e mau e mau de "
    "tk ga m cham a m cham ro m bia a tk nfu ei mau k e mau de alo alo cn choa ei mau ti k mau de "
    "alo alo cn tó ei mau ti e mau de yeu ot v tk ccho ei m tru noi k ay tk 3de cn ga ei m ga vl lun e "
    "alo alo sao ay nhi anh lai win a uoc loser ma tk nfu ei slow k ay cn cho speed lun e toi die k e "
    "tru ma tru ne tk nfu m tru k noi a m yeu v a tk ga ei mau k e mau de yeu z cn choa nfu sao do "
    "chay bo a bo manh vl bo dzi ba ro m chay a ma anh hot war ma e anh hot trụ cmnr m lam lai a k "
    "lam lai anh deo dau ma chay anh ro r con gi khac k m bia a tk nfu ei cam m bia ma bia cn gia m dot tu e "
) * 5 # Nhân bản 5 lần để đảm bảo tin nhắn siêu dài

app = Flask(__name__)
@app.route('/')
def home(): return "System Online for ID: 7153197678"
def run_flask(): app.run(host='0.0.0.0', port=8080)

def setup_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['help'])
    def help_cmd(m):
        if m.from_user.id in ADMINS:
            msg = ("📜 HỆ THỐNG CỦA ÔNG:\n"
                   "/spam [nội dung] - Spam văn bản tùy chọn\n"
                   "/splag - Thả bom LAG ký tự\n"
                   "/spdai - Thả bom VĂN BẢN CHỬI DÀI\n"
                   "/dung - Dừng spam ngay lập tức\n"
                   "/setdelay [giây] - Chỉnh tốc độ (mặc định 0.5)\n"
                   "/info - Check tình trạng Bot")
            bot.reply_to(m, msg)

    @bot.message_handler(commands=['spdai'])
    def spdai_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            dang_spam = True
            bot.send_message(m.chat.id, "📏 ĐANG XẢ VĂN BẢN DÀI...")
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, DAI_TXT)
                    time.sleep(delay_spam)
                except: time.sleep(1); break

    @bot.message_handler(commands=['splag'])
    def splag_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            dang_spam = True
            bot.send_message(m.chat.id, "🚀 ĐANG THẢ BOM LAG...")
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, LAG_TXT)
                    time.sleep(delay_spam)
                except: time.sleep(1); break

    @bot.message_handler(commands=['spam'])
    def spam_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            content = m.text.replace('/spam', '').strip() or "System Lagging..."
            dang_spam = True
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, content)
                    time.sleep(delay_spam)
                except: time.sleep(1); break

    @bot.message_handler(commands=['dung'])
    def dung_cmd(m):
        global dang_spam
        if m.from_user.id in ADMINS:
            dang_spam = False
            bot.reply_to(m, "🛑 ĐÃ DỪNG LẠI THEO LỆNH ÔNG!")

    @bot.message_handler(commands=['setdelay'])
    def setdelay_cmd(m):
        global delay_spam
        if m.from_user.id in ADMINS:
            try:
                delay_spam = float(m.text.split()[1])
                bot.reply_to(m, f"⏱️ Delay mới: {delay_spam}s")
            except: pass

    @bot.message_handler(commands=['info'])
    def info_cmd(m):
        if m.from_user.id in ADMINS:
            bot.reply_to(m, f"ℹ️ Số lượng Bot: {len(TOKENS)}\n👤 Chủ: 7153197678\n⏱️ Delay: {delay_spam}s")

    # Xử lý các lệnh quản lý admin (Chỉ ID_CHU_BOT mới dùng được)
    @bot.message_handler(commands=['addadm'])
    def addadm_cmd(m):
        if m.from_user.id == ID_CHU_BOT:
            try:
                new_id = int(m.text.split()[1])
                if new_id not in ADMINS:
                    ADMINS.append(new_id)
                    bot.reply_to(m, f"✅ Đã thêm Admin: {new_id}")
            except: pass

    bot.polling(none_stop=True)

if __name__ == '__main__':
    # Chạy Flask giữ bot sống
    Thread(target=run_flask).start()
    # Chạy toàn bộ bot trong list TOKENS
    for token in TOKENS:
        Thread(target=setup_bot, args=(token,)).start()

   
