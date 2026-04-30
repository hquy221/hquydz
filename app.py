import telebot
import time
from flask import Flask
from threading import Thread

# --- CẤU HÌNH ID: 7153197678 ---
ID_CHU_BOT = 7153197678  
ADMINS = [7153197678]
TOKENS = ['8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0', '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c', '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM', '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', '8650032681:AAE9TeiIlywG796f6hKLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbIztbNZZtni7D0uDl4', '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o', '8745047343:AAF3XKrSHnGHujBv94a2GeYXweXgIFMEFVs']

delay_spam = 0.5
dang_spam = False

LAG_TXT = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃰ ꙰꙰⃟꙰⃟꙰⃟꙰⃰ ꙰꙰⃟꙰⃟꙰⃟꙰kk ꙰꙰⃟꙰"

# Văn bản dài của ông
DAI_TXT = """cn choa ei=))=))=))=))
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

app = Flask('')
@app.route('/')
def home(): return "CHA HQUY ONLINE 🚀"

def setup_bot(token):
    try:
        bot = telebot.TeleBot(token)
        
        @bot.message_handler(commands=['help'])
        def help(m):
            bot.reply_to(m, "🚀 /spam | 💥 /splag | 📜 /spdai\n🛑 /dung | ⚡ /setdelay\nℹ️ /info")

        @bot.message_handler(commands=['info', 'list'])
        def send_info(m):
            bot.reply_to(m, f"🤖 Status: Live\n⚡ Delay: {delay_spam}s\n🆔 My ID: 7153197678")

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
                # Đã thay câu thông báo thành nội dung văn bản ông muốn
                bot.reply_to(m, DAI_TXT)
                while dang_spam:
                    try: bot.send_message(m.chat.id, DAI_TXT); time.sleep(delay_spam)
                    except: time.sleep(1)

        @bot.message_handler(commands=['dung'])
        def stop(m):
            global dang_spam
            if m.from_user.id in ADMINS:
                dang_spam = False
                bot.reply_to(m, "🛑 STOPPED!")

        bot.polling(none_stop=True)
    except: pass

if __name__ == "__main__":
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    for t in TOKENS: Thread(target=setup_bot, args=(t,)).start(); time.sleep(0.4)
