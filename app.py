import telebot
import time
from flask import Flask
from threading import Thread

# --- CẤU HÌNH MASTER ID ---
MASTER_ID = 7153197678
ADMINS = [7153197678]
delay_spam = 0.3
dang_spam = False

TOKENS = [
    '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', 
    '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0', 
    '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c', 
    '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM', 
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwXP79U4PBaII0MA', 
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', 
    '8650032681:AAE9TeiIlywG796f6hKLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', 
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', 
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbIztbNZZtni7D0uDl4', 
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o', '8745047343:AAF3XKrSHnGHujBv94a2GeYXweXgIFMEFVs'
]

# Nội dung Lag cực đại như ảnh mẫu
K_LAG = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ "
LAG_TXT = K_LAG * 600

app = Flask(__name__)
@app.route('/')
def home(): return "SYSTEM ONLINE"

def setup_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(func=lambda m: True)
    def handle_all_messages(m):
        global dang_spam, delay_spam
        # Check quyền ID 7153197678
        if m.from_user.id != 7153197678 and m.from_user.id not in ADMINS:
            return

        cmd = m.text.split()[0].lower() if m.text else ""

        # LỆNH HỆ THỐNG
        if cmd == '/help':
            help_text = (
                "✨ **DANH SÁCH LỆNH ĐIỀU KHIỂN**\n"
                "━━━━━━━━━━━━━━\n"
                "🔹 `/info`: Thông tin chủ bot\n"
                "🔹 `/list`: Danh sách Admin\n"
                "🔹 `/splag`: Spam lag siêu dài\n"
                "🔹 `/spdai`: Spam chửi mẫu\n"
                "🔹 `/spam [text]`: Spam nội dung tùy chọn\n"
                "🔹 `/dung`: Dừng spam\n"
                "🔹 `/setdelay [s]`: Chỉnh tốc độ\n"
                "🔹 `/addadm [id]`: Thêm Admin\n"
                "🔹 `/xoaadm [id]`: Xóa Admin"
            )
            bot.send_message(m.chat.id, help_text, parse_mode="Markdown")

        elif cmd == '/list':
            ad_list = "👥 **ADMINS:**\n" + "\n".join([f"• `{a}`" for a in ADMINS])
            bot.send_message(m.chat.id, ad_list, parse_mode="Markdown")

        elif cmd == '/info':
            bot.send_message(m.chat.id, "👤 **MASTER:** `7153197678` | **STATUS:** `ONLINE`", parse_mode="Markdown")

        # QUẢN LÝ ADMIN (Chỉ Master được dùng)
        elif cmd == '/addadm':
            if m.from_user.id == 7153197678:
                try:
                    new_id = int(m.text.split()[1])
                    if new_id not in ADMINS: ADMINS.append(new_id)
                    bot.reply_to(m, f"✅ Đã thêm Admin: `{new_id}`")
                except: pass
        
        elif cmd == '/xoaadm':
            if m.from_user.id == 7153197678:
                try:
                    old_id = int(m.text.split()[1])
                    if old_id != 7153197678 and old_id in ADMINS:
                        ADMINS.remove(old_id)
                        bot.reply_to(m, f"🗑️ Đã xóa Admin: `{old_id}`")
                except: pass

        # LỆNH SPAM
        elif cmd == '/splag':
            dang_spam = True
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, LAG_TXT)
                    time.sleep(delay_spam)
                except: break

        elif cmd == '/spdai':
            dang_spam = True
            content = "alo alo cn choa ei mau ti k mau de mau de mau de tk nfu ei m cham vl m bia ro m yeu ot vcl " * 80
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, content)
                    time.sleep(delay_spam)
                except: break

        elif cmd == '/spam':
            content = m.text.replace('/spam', '').strip() or "..."
            dang_spam = True
            while dang_spam:
                try:
                    bot.send_message(m.chat.id, content)
                    time.sleep(delay_spam)
                except: break

        elif cmd == '/dung':
            dang_spam = False
            bot.send_message(m.chat.id, "🛑 **ĐÃ DỪNG TOÀN BỘ**")

        elif cmd == '/setdelay':
            try:
                delay_spam = float(m.text.split()[1])
                bot.reply_to(m, f"⏱️ Delay: `{delay_spam}s`")
            except: pass

    bot.polling(none_stop=True)

if __name__ == '__main__':
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    for token in TOKENS:
        Thread(target=setup_bot, args=(token,)).start()
