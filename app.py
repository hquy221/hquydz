import telebot
import threading
from flask import Flask
import time
import requests

# --- DANH SÁCH 23 TOKEN (GIỮ NGUYÊN) ---
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
spam_delay = 1.0 
app = Flask('')

@app.route('/')
def home():
    return "SYSTEM 23 BOTS ACTIVE - FULL TEXT MODE"

def filter_tokens():
    global VALID_TOKENS
    VALID_TOKENS = []
    for t in RAW_TOKENS:
        try:
            res = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=5)
            if res.status_code == 200: VALID_TOKENS.append(t)
        except: pass

def setup_bot(token):
    bot = telebot.TeleBot(token)
    def check_adm(uid): return uid in ADMIN_LIST

    @bot.message_handler(commands=['help'])
    def h(m):
        if check_adm(m.from_user.id):
            msg = "📌 LỆNH CHIẾN:\n/spdai, /splag, /spam, /sptag\n/info, /list, /addadm, /xoaadm\n/setdelay, /dung"
            bot.reply_to(m, msg)

    @bot.message_handler(commands=['info', 'list'])
    def info(m):
        if check_adm(m.from_user.id):
            bot.reply_to(m, f"📊 Online: {len(VALID_TOKENS)} Bots\n⏳ Delay: {spam_delay}s")

    @bot.message_handler(commands=['addadm'])
    def add(m):
        if check_adm(m.from_user.id):
            try:
                nid = int(m.text.split()[1])
                if nid not in ADMIN_LIST: ADMIN_LIST.append(nid)
                bot.reply_to(m, f"✅ Đã thêm admin {nid}")
            except: pass

    @bot.message_handler(commands=['setdelay'])
    def sd(m):
        global spam_delay
        if check_adm(m.from_user.id):
            try:
                spam_delay = float(m.text.split()[1])
                bot.reply_to(m, f"⚡ Set delay: {spam_delay}s")
            except: pass

    @bot.message_handler(commands=['dung'])
    def stop(m):
        global is_spaming
        if check_adm(m.from_user.id):
            is_spaming = False
            bot.reply_to(m, "🛑 STOP")

    @bot.message_handler(commands=['sptag'])
    def tag_spam(m):
        global is_spaming
        if check_adm(m.from_user.id):
            is_spaming = True
            try:
                target = m.text.split(' ', 1)[1]
                for i in range(200):
                    if not is_spaming: break
                    bot.send_message(m.chat.id, f"{target} sủa đi e {i+1}")
                    time.sleep(spam_delay)
            except: pass

    @bot.message_handler(commands=['splag'])
    def lag(m):
        global is_spaming
        if check_adm(m.from_user.id):
            is_spaming = True
            # VĂN BẢN LAG FULL KHÔNG DÙNG PHÉP NHÂN
            txt_lag = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰\n"
            for _ in range(100):
                if not is_spaming: break
                try:
                    bot.send_message(m.chat.id, txt_lag)
                    time.sleep(spam_delay)
                except: time.sleep(1)

    @bot.message_handler(commands=['spdai'])
    def dai(m):
        global is_spaming
        if check_adm(m.from_user.id):
            is_spaming = True
            # VĂN BẢN ĐÀI FULL CỰC DÀI (GHI TRỰC TIẾP)
            txt_war = (
                "cn choa ei=))=))=))=))\n123=))=))=))=))\nm chay anh cmnr=))=))=))=))=))\n"
                "m yeu ot z tk nfu=))=))=))=))=))\nm cham vl e=))=))=))\nslow lun e=))=))=))=))\nyeu z cn dix=))=))=))=))\n"
                "tk 3de=))=))=))=))=))\ntk dix lgbt=))=))=))\ncn choa nfu=))=))=))=))=))\ndeo co canh lun e=))=))=))=))\n"
                "m cham vl e=))=))=))=))\nm yeu v=))=))=))=))=))=))\nyeu ro=))=))=))=))=))=))\nbia a=))=))=))=))\ntk dix=))=))=))=))\nmau k=))=))=))=))\nmau de=))=))=))=))=))\ncham a=))=))=))=))=))=))\ntk nfu =))=))=))=))=))\nmau ti de=))=))=))=))\nyeu ot vcl=))=))=))=))\ncmm dot tu kia=))=))=))\nlien tuc de=))=))=))=))=))\nalo may cn cho nu=)) =)) =)) \ncmm =))=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau de=))=))=))=))=))\nalo alo=))=))=))=))\ncn tó ei=))=))=))\nmau ti e=))=))=))=))\nmau de=))=))=))=))\nyeu ot v=))=))=))\ntk ccho ei=))=))=))\nm tru noi k ay=))=))=))=))\ntk 3de=))=))=))=))\ncn ga ei=))=))=))=))\nm ga vl lun e=))=))=))=))\nalo alo=))=))=))\nsao ay nhi=))=))=))=))\nanh lai win a=))=))=))=))\nuoc loser ma=))=))=))=))\ntk nfu ei=))=))=))=))\nslow k ay=))=))=))\ncn cho =))=))=))\nspeed lun e=))=))=))\ntoi die k e=))=))=))\ntru ma=))=))=))\ntru ne tk nfu=))=))=))=))=))\nm tru k noi a=))=))=))=))=))\nm yeu v a=))=))=))=))\ntk ga ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))=))\nyeu z=))=))=))=))=))\ncn choa nfu=))=))=))=))=))\nsao do=))=))=))=))=))=))\nchay bo a=))=))=))=))=))\nbo manh vl=))=))=))=))\nbo dzi ba ro=))=))=))=))\nm chay a ma=))=))=))\nanh hot war ma e=))=))=))=))=))\nanh hot trụ cmnr=))=))=))=))=))\nm lam lai a k =))=))=))=))\nlam lai anh deo dau ma=))=))=))=))\nchay anh ro r=))=))=))=))\ncon gi khac k=))=))=))=))=))\nm bia a=))=))=))=))\ntk nfu ei=))=))=))=))\ncam m bia ma=))=))=))=))\nbia cn gia m dot tu e=))=))=))=))=))\nlofi chill k=))=))=))=))\n"
                "cn choa ei=))=))=))=))\n123=))=))=))=))\nm chay anh cmnr=))=))=))=))=))\n"
                "m yeu ot z tk nfu=))=))=))=))=))\nm cham vl e=))=))=))\nslow lun e=))=))=))=))\nyeu z cn dix=))=))=))=))\n"
                "tk 3de=))=))=))=))=))\ntk dix lgbt=))=))=))\ncn choa nfu=))=))=))=))=))\ndeo co canh lun e=))=))=))=))\n"
                "m cham vl e=))=))=))=))\nm yeu v=))=))=))=))=))=))\nyeu ro=))=))=))=))=))=))\nbia a=))=))=))=))\ntk dix=))=))=))=))\nmau k=))=))=))=))\nmau de=))=))=))=))=))\ncham a=))=))=))=))=))=))\ntk nfu =))=))=))=))=))\nmau ti de=))=))=))=))\nyeu ot vcl=))=))=))=))\ncmm dot tu kia=))=))=))\nlien tuc de=))=))=))=))=))\nalo may cn cho nu=)) =)) =)) \ncmm =))=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau de=))=))=))=))=))\nalo alo=))=))=))=))\ncn tó ei=))=))=))\nmau ti e=))=))=))=))\nmau de=))=))=))=))\nyeu ot v=))=))=))\ntk ccho ei=))=))=))\nm tru noi k ay=))=))=))=))\ntk 3de=))=))=))=))\ncn ga ei=))=))=))=))\nm ga vl lun e=))=))=))=))\nalo alo=))=))=))\nsao ay nhi=))=))=))=))\nanh lai win a=))=))=))=))\nuoc loser ma=))=))=))=))\ntk nfu ei=))=))=))=))\nslow k ay=))=))=))\ncn cho =))=))=))\nspeed lun e=))=))=))\ntoi die k e=))=))=))\ntru ma=))=))=))\ntru ne tk nfu=))=))=))=))=))\nm tru k noi a=))=))=))=))=))\nm yeu v a=))=))=))=))\ntk ga ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))=))\nyeu z=))=))=))=))=))\ncn choa nfu=))=))=))=))=))\nsao do=))=))=))=))=))=))\nchay bo a=))=))=))=))=))\nbo manh vl=))=))=))=))\nbo dzi ba ro=))=))=))=))\nm chay a ma=))=))=))\nanh hot war ma e=))=))=))=))=))\nanh hot trụ cmnr=))=))=))=))=))\nm lam lai a k =))=))=))=))\nlam lai anh deo dau ma=))=))=))=))\nchay anh ro r=))=))=))=))\ncon gi khac k=))=))=))=))=))\nm bia a=))=))=))=))\ntk nfu ei=))=))=))=))\ncam m bia ma=))=))=))=))\nbia cn gia m dot tu e=))=))=))=))=))\nlofi chill k=))=))=))=))"
            )
            for _ in range(100):
                if not is_spaming: break
                bot.send_message(m.chat.id, txt_war)
                time.sleep(spam_delay)

    @bot.message_handler(commands=['spam'])
    def s(m):
        global is_spaming
        if check_adm(m.from_user.id):
            is_spaming = True
            try:
                txt = m.text.split(' ', 1)[1]
                for _ in range(100):
                    if not is_spaming: break
                    bot.send_message(m.chat.id, txt)
                    time.sleep(spam_delay)
            except: pass

    bot.infinity_polling(timeout=25, skip_pending=True)

def run():
    filter_tokens()
    if not VALID_TOKENS: return
    for token in VALID_TOKENS:
        t = threading.Thread(target=setup_bot, args=(token,))
        t.daemon = True
        t.start()
        time.sleep(1.2)

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    run()
    while True: 
        time.sleep(3) # Main loop duy trì 3s
