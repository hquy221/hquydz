import telebot
import time
from flask import Flask
from threading import Thread
import threading

# --- CẤU HÌNH MASTER ID CỦA ÔNG ---
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

# Văn bản /spdai ông vừa gửi
SPDAI_CONTENT = """cn choa ei=))=))=))=))
123=))=))=))=))
m chay anh cmnr=))=))=))=))=))
m yeu ot z tk nfu=))=))=))=))=))
m cham vl e=))=))=))
slow lun e=))=))=))=))
yeu z cn dix=))=))=))=))
tk 3de=))=))=))=))=))
tk dix lgbt=))=))=))=))
cn choa nfu=))=))=))=))=))
deo co canh lun e=))=))=))=))
m cham vl e=))=))=))=))
m yeu v=))=))=))=))=))=))
yeu ro=))=))=))=))=))=))
bia a=))=))=))=))
tk dix=))=))=))=))
mau k=))=))=))=))
mau de=))=))=))=))=))
cham a=))=))=))=))=))=))
tk nfu =))=))=))=))=))
mau ti de=))=))=))=))
yeu ot vcl=))=))=))=))
cmm dot tu kia=))=))=))
lien tuc de=))=))=))=))=))
alo may cn cho nu=)) =)) =)) 
cmm =))=))=))=))
sua e=))=))=))=))
mau e=))=))=))
mau de=))=))=))
tk ga=))=))=))
m cham a=))=))=))
m cham ro=))=))=))=))
m bia a=))=))=))
tk nfu ei=))=))=))=))
mau k e=))=))=))=))
mau de=))=))=))
alo alo=))=))=))=))=))
cn choa ei=))=))=))=))
mau ti k=))=))=))=))
mau de=))=))=))=))=))
alo alo=))=))=))=))
cn tó ei=))=))=))
mau ti e=))=))=))=))
mau de=))=))=))=))
yeu ot v=))=))=))
tk ccho ei=))=))=))
m tru noi k ay=))=))=))=))
tk 3de=))=))=))=))
cn ga ei=))=))=))=))
m ga vl lun e=))=))=))=))
alo alo=))=))=))
sao ay nhi=))=))=))=))
anh lai win a=))=))=))=))
uoc loser ma=))=))=))=))
tk nfu ei=))=))=))=))
slow k ay=))=))=))
cn cho =))=))=))
speed lun e=))=))=))
toi die k e=))=))=))
mau me m di=))=))=))=))
tk cho nfu=))=))=))=))=))
m ot bo ro=))=))=))=))
m bia a=))=))=))=))=))
con gi khac k=))=))=))=))
tk ga ei=))=))=))
mau k e=))=))=))=))=))
anh win cmnr=))=))=))
sua e=))=))=))=))
mau e=))=))=))
mau de=))=))=))
tk ga=))=))=))
m cham a=))=))=))
m cham ro=))=))=))=))
m bia a=))=))=))
tk nfu ei=))=))=))=))
mau k e=))=))=))=))
mau de=))=))=))
alo alo=))=))=))=))=))
cn choa ei=))=))=))=))
mau ti k=))=))=))=))
mau me m di=))=))=))=))
tk cho nfu=))=))=))=))=))
a đấng hot war mà=))=))=))=))
cmm chối à=))=))=))=))
a hw mẹ r=))=))=))=))
con gi dau ma noi =))=))=))=))
a treo co me m ma=))=))=))=))
a win ma=))=))=))=))
m bia a=))=))=))=))
tk nfu ri=))=))=))=))=))
m ngu v =))=))=))=))
ngu ro lun e=))=))=))=))=))
bia a e=))=))=))=))
le de alo =))=))=))=))
s do =))=))=))=))=))
m sao =))=))=))=))
 m chạy a mà=))=))=))=))
m bịa à=))=))=))=))
 tk nu=))=))=))=))=))
cmm =))=))=))=))
sua e=))=))=))=))
mau e=))=))=))
mau de=))=))=))
tk ga=))=))=))
m cham a=))=))=))
m cham ro=))=))=))=))
m bia a=))=))=))
tk nfu ei=))=))=))=))
mau k e=))=))=))=))
mau de=))=))=))
alo alo=))=))=))=))=))
cn choa ei=))=))=))=))
mau ti k=))=))=))=))
mau de=))=))=))=))=))
alo alo=))=))=))=))
cn tó ei=))=))=))
mau ti e=))=))=))=))
mau de=))=))=))=))
yeu ot v=))=))=))
tk ccho ei=))=))=))
m tru noi k ay=))=))=))=))
tk 3de=))=))=))=))
cn ga ei=))=))=))=))
m ga vl lun e=))=))=))=))
alo alo=))=))=))
sao ay nhi=))=))=))=))
anh lai win a=))=))=))=))
uoc loser ma=))=))=))=))
tk nfu ei=))=))=))=))
slow k ay=))=))=))
cn cho =))=))=))
speed lun e=))=))=))
toi die k e=))=))=))
tru ma=))=))=))
tru ne tk nfu=))=))=))=))=))
m tru k noi a=))=))=))=))=))
m yeu v a=))=))=))=))
tk ga ei=))=))=))=))
mau k e=))=))=))=))
mau de=))=))=))=))
yeu z=))=))=))=))=))
cn choa nfu=))=))=))=))=))
sao do=))=))=))=))=))=))
chay bo a=))=))=))=))=))
bo manh vl=))=))=))=))
bo dzi ba ro=))=))=))=))
m chay a ma=))=))=))
anh hot war ma e=))=))=))=))=))
anh hot trụ cmnr=))=))=))=))=))
m lam lai a k =))=))=))=))
lam lai anh deo dau ma=))=))=))=))
chay anh ro r=))=))=))=))
con gi khac k=))=))=))=))=))
m bia a=))=))=))=))
tk nfu ei=))=))=))=))
cam m bia ma=))=))=))=))
bia cn gia m dot tu e=))=))=))=))=))
lofi chill k=))=))=))=))"""

# Nội dung Lag trắng màn hình
K_LAG = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ "
LAG_TXT = K_LAG * 500

app = Flask(__name__)
@app.route('/')
def home(): return "SYSTEM READY"

def spam_task(bot, chat_id, content):
    global dang_spam
    while dang_spam:
        try:
            bot.send_message(chat_id, content)
            time.sleep(delay_spam)
        except: break

def setup_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(func=lambda m: True)
    def handle_all(m):
        global dang_spam, delay_spam
        # Check quyền Master ID của ông
        if m.from_user.id != 7153197678 and m.from_user.id not in ADMINS:
            return

        txt = m.text.lower() if m.text else ""

        if txt == '/help':
            bot.send_message(m.chat.id, "✨ **DANH SÁCH LỆNH**\n- `/info` | `/list` | `/splag` | `/spdai` | `/spam` | `/dung` | `/setdelay` | `/addadm` | `/xoaadm`", parse_mode="Markdown")

        elif txt == '/info':
            bot.send_message(m.chat.id, f"👤 **MASTER:** `7153197678`", parse_mode="Markdown")

        elif txt == '/list':
            bot.send_message(m.chat.id, f"👥 **ADMINS:**\n" + "\n".join([f"• `{a}`" for a in ADMINS]), parse_mode="Markdown")

        elif txt.startswith('/addadm'):
            if m.from_user.id == 7153197678:
                try:
                    new_id = int(m.text.split()[1])
                    if new_id not in ADMINS: ADMINS.append(new_id)
                    bot.reply_to(m, f"✅ Thêm Admin: `{new_id}`")
                except: pass

        elif txt == '/splag':
            if not dang_spam:
                dang_spam = True
                threading.Thread(target=spam_task, args=(bot, m.chat.id, LAG_TXT)).start()

        elif txt == '/spdai':
            if not dang_spam:
                dang_spam = True
                threading.Thread(target=spam_task, args=(bot, m.chat.id, SPDAI_CONTENT)).start()

        elif txt.startswith('/spam'):
            if not dang_spam:
                content = m.text.replace('/spam', '').strip() or "..."
                dang_spam = True
                threading.Thread(target=spam_task, args=(bot, m.chat.id, content)).start()

        elif txt == '/dung':
            dang_spam = False
            bot.send_message(m.chat.id, "🛑 **ĐÃ DỪNG**")

        elif txt.startswith('/setdelay'):
            try:
                delay_spam = float(m.text.split()[1])
                bot.reply_to(m, f"⏱️ Delay: `{delay_spam}s`")
            except: pass

    bot.polling(none_stop=True)

if __name__ == '__main__':
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    for token in TOKENS:
        Thread(target=setup_bot, args=(token,)).start()
