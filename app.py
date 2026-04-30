import telebot
import threading
from flask import Flask
import time
import requests

# --- DANH SÁCH 20 TOKEN (TỰ LỌC LỖI) ---
RAW_TOKENS = [
    '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0',
    '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0',
    '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c',
    '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM',
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA',
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0',
    '8650032681:AAE9TeiIlywG796f6y6hKLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0',
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY',
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4',
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o', '8745047343:AAF3XKrSHnGHujBv94a2GeYXweXgIFMEFVs'
]

VALID_TOKENS = []
ADMIN_LIST = [7153197678] 
spam_delay = 0.1
app = Flask('')

@app.route('/')
def home():
    return f"Bot is running with {len(VALID_TOKENS)} tokens."

def filter_tokens():
    for t in RAW_TOKENS:
        try:
            response = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=5)
            if response.status_code == 200:
                VALID_TOKENS.append(t)
        except: pass

def setup_bot(token):
    bot = telebot.TeleBot(token)

    def is_admin(user_id):
        return user_id in ADMIN_LIST

    @bot.message_handler(commands=['help'])
    def send_help(message):
        help_text = (
            "📌 DANH SÁCH LỆNH:\n"
            "/spdai - Spam văn bản War\n"
            "/splag - Spam mã Lag\n"
            "/spam [nội dung] - Spam tùy chỉnh\n"
            "/info - Xem ID (Reply người khác)\n"
            "/list - Xem danh sách Admin\n"
            "/addadm [ID] - Thêm Admin\n"
            "/xoaadm [ID] - Xóa Admin\n"
            "/setdelay [số giây] - Chỉnh tốc độ"
        )
        bot.send_message(message.chat.id, help_text)

    @bot.message_handler(commands=['list'])
    def list_admin(message):
        bot.send_message(message.chat.id, f"👥 Admin List: {ADMIN_LIST}")

    @bot.message_handler(commands=['info'])
    def get_info(message):
        target = message.reply_to_message.from_user.id if message.reply_to_message else message.from_user.id
        bot.reply_to(message, f"🆔 ID: `{target}`", parse_mode="Markdown")

    @bot.message_handler(commands=['addadm'])
    def add_admin(message):
        if is_admin(message.from_user.id):
            try:
                new_id = int(message.text.split()[1])
                if new_id not in ADMIN_LIST:
                    ADMIN_LIST.append(new_id)
                    bot.reply_to(message, f"Đã thêm Admin: {new_id}")
            except: pass

    @bot.message_handler(commands=['xoaadm'])
    def xoa_admin(message):
        if is_admin(message.from_user.id):
            try:
                del_id = int(message.text.split()[1])
                if del_id in ADMIN_LIST and del_id != 7153197678:
                    ADMIN_LIST.remove(del_id)
                    bot.reply_to(message, f"Đã xóa Admin: {del_id}")
            except: pass

    @bot.message_handler(commands=['setdelay'])
    def set_delay(message):
        global spam_delay
        if is_admin(message.from_user.id):
            try:
                val = float(message.text.split()[1])
                spam_delay = val
                bot.reply_to(message, f"Đã chỉnh delay: {val}s")
            except: pass

    @bot.message_handler(commands=['spam'])
    def spam_custom(message):
        if is_admin(message.from_user.id):
            parts = message.text.split(' ', 1)
            if len(parts) > 1:
                content = parts[1]
                for _ in range(15):
                    bot.send_message(message.chat.id, content)
                    time.sleep(spam_delay)

    @bot.message_handler(commands=['spdai'])
    def spdai(message):
        if is_admin(message.from_user.id):
            text_war = (
                "cn choa ei=))=))=))=))\n123=))=))=))=))\nm chay anh cmnr=))=))=))=))=))\n"
                "m yeu ot z tk nfu=))=))=))=))=))\nm cham vl e=))=))=))\nslow lun e=))=))=))=))\nyeu z cn dix=))=))=))=))\n"
                "tk 3de=))=))=))=))=))\ntk dix lgbt=))=))=))\ncn choa nfu=))=))=))=))=))\ndeo co canh lun e=))=))=))=))\n"
                "m cham vl e=))=))=))=))\nm yeu v=))=))=))=))=))=))\nyeu ro=))=))=))=))=))=))\nbia a=))=))=))=))\ntk dix=))=))=))=))\nmau k=))=))=))=))\nmau de=))=))=))=))=))\ncham a=))=))=))=))=))=))\ntk nfu =))=))=))=))=))\nmau ti de=))=))=))=))\nyeu ot vcl=))=))=))=))\ncmm dot tu kia=))=))=))\nlien tuc de=))=))=))=))=))\nalo may cn cho nu=)) =)) =)) \ncmm =))=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau de=))=))=))=))=))\nalo alo=))=))=))=))\ncn tó ei=))=))=))\nmau ti e=))=))=))=))\nmau de=))=))=))=))\nyeu ot v=))=))=))\ntk ccho ei=))=))=))\nm tru noi k ay=))=))=))=))\ntk 3de=))=))=))=))\ncn ga ei=))=))=))=))\nm ga vl lun e=))=))=))=))\nalo alo=))=))=))\nsao ay nhi=))=))=))=))\nanh lai win a=))=))=))=))\nuoc loser ma=))=))=))=))\ntk nfu ei=))=))=))=))\nslow k ay=))=))=))\ncn cho =))=))=))\nspeed lun e=))=))=))\ntoi die k e=))=))=))\nmau me m di=))=))=))=))\ntk cho nfu=))=))=))=))=))\nm ot bo ro=))=))=))=))\nm bia a=))=))=))=))=))\ncon gi khac k=))=))=))=))\ntk ga ei=))=))=))\nmau k e=))=))=))=))=))\nanh win cmnr=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau me m di=))=))=))=))\ntk cho nfu=))=))=))=))=))\na đấng hot war mà=))=))=))=))\ncmm chối à=))=))=))=))\na hw mẹ r=))=))=))=))\ncon gi dau ma noi =))=))=))=))\na treo co me m ma=))=))=))=))\na win ma=))=))=))=))\nm bia a=))=))=))=))\ntk nfu ri=))=))=))=))=))\nm ngu v =))=))=))=))\nngu ro lun e=))=))=))=))=))\nbia a e=))=))=))=))\nle de alo =))=))=))=))\ns do =))=))=))=))=))\nm sao =))=))=))=))\n m chạy a mà=))=))=))=))\nm bịa à=))=))=))=))\n tk nu=))=))=))=))=))\ncmm =))=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau de=))=))=))=))=))\nalo alo=))=))=))=))\ncn tó ei=))=))=))\nmau ti e=))=))=))=))\nmau de=))=))=))=))\nyeu ot v=))=))=))\ntk ccho ei=))=))=))\nm tru noi k ay=))=))=))=))\ntk 3de=))=))=))=))\ncn ga ei=))=))=))=))\nm ga vl lun e=))=))=))=))\nalo alo=))=))=))\nsao ay nhi=))=))=))=))\nanh lai win a=))=))=))=))\nuoc loser ma=))=))=))=))\ntk nfu ei=))=))=))=))\nslow k ay=))=))=))\ncn cho =))=))=))\nspeed lun e=))=))=))\ntoi die k e=))=))=))\ntru ma=))=))=))\ntru ne tk nfu=))=))=))=))=))\nm tru k noi a=))=))=))=))=))\nm yeu v a=))=))=))=))\ntk ga ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))=))\nyeu z=))=))=))=))=))\ncn choa nfu=))=))=))=))=))\nsao do=))=))=))=))=))=))\nchay bo a=))=))=))=))=))\nbo manh vl=))=))=))=))\nbo dzi ba ro=))=))=))=))\nm chay a ma=))=))=))\nanh hot war ma e=))=))=))=))=))\nanh hot trụ cmnr=))=))=))=))=))\nm lam lai a k =))=))=))=))\nlam lai anh deo dau ma=))=))=))=))\nchay anh ro r=))=))=))=))\ncon gi khac k=))=))=))=))=))\nm bia a=))=))=))=))\ntk nfu ei=))=))=))=))\ncam m bia ma=))=))=))=))\nbia cn gia m dot tu e=))=))=))=))=))\nlofi chill k=))=))=))=))"
            )
            bot.send_message(message.chat.id, text_war)

    @bot.message_handler(commands=['splag'])
    def splag(message):
        if is_admin(message.from_user.id):
            # VĂN BẢN LAG ĐƯỢC XẢ THẲNG (CỰC DÀI)
            text_lag = "꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰"
            for _ in range(15):
                bot.send_message(message.chat.id, text_lag)
                time.sleep(spam_delay)

    @bot.message_handler(commands=['spdai'])
    def spdai_cmd(message):
        if is_admin(message.from_user.id):
            text_war = (
                "cn choa ei=))=))=))=))\n123=))=))=))=))\nm chay anh cmnr=))=))=))=))=))\n"
                "m yeu ot z tk nfu=))=))=))=))=))\nm cham vl e=))=))=))\nslow lun e=))=))=))=))\nyeu z cn dix=))=))=))=))\n"
                "tk 3de=))=))=))=))=))\ntk dix lgbt=))=))=))\ncn choa nfu=))=))=))=))=))\ndeo co canh lun e=))=))=))=))\n"
                "m cham vl e=))=))=))=))\nm yeu v=))=))=))=))=))=))\nyeu ro=))=))=))=))=))=))\nbia a=))=))=))=))\ntk dix=))=))=))=))\nmau k=))=))=))=))\nmau de=))=))=))=))=))\ncham a=))=))=))=))=))=))\ntk nfu =))=))=))=))=))\nmau ti de=))=))=))=))\nyeu ot vcl=))=))=))=))\ncmm dot tu kia=))=))=))\nlien tuc de=))=))=))=))=))\nalo may cn cho nu=)) =)) =)) \ncmm =))=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau de=))=))=))=))=))\nalo alo=))=))=))=))\ncn tó ei=))=))=))\nmau ti e=))=))=))=))\nmau de=))=))=))=))\nyeu ot v=))=))=))\ntk ccho ei=))=))=))\nm tru noi k ay=))=))=))=))\ntk 3de=))=))=))=))\ncn ga ei=))=))=))=))\nm ga vl lun e=))=))=))=))\nalo alo=))=))=))\nsao ay nhi=))=))=))=))\nanh lai win a=))=))=))=))\nuoc loser ma=))=))=))=))\ntk nfu ei=))=))=))=))\nslow k ay=))=))=))\ncn cho =))=))=))\nspeed lun e=))=))=))\ntoi die k e=))=))=))\nmau me m di=))=))=))=))\ntk cho nfu=))=))=))=))=))\nm ot bo ro=))=))=))=))\nm bia a=))=))=))=))=))\ncon gi khac k=))=))=))=))\ntk ga ei=))=))=))\nmau k e=))=))=))=))=))\nanh win cmnr=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau me m di=))=))=))=))\ntk cho nfu=))=))=))=))=))\na đấng hot war mà=))=))=))=))\ncmm chối à=))=))=))=))\na hw mẹ r=))=))=))=))\ncon gi dau ma noi =))=))=))=))\na treo co me m ma=))=))=))=))\na win ma=))=))=))=))\nm bia a=))=))=))=))\ntk nfu ri=))=))=))=))=))\nm ngu v =))=))=))=))\nngu ro lun e=))=))=))=))=))\nbia a e=))=))=))=))\nle de alo =))=))=))=))\ns do =))=))=))=))=))\nm sao =))=))=))=))\n m chạy a mà=))=))=))=))\nm bịa à=))=))=))=))\n tk nu=))=))=))=))=))\ncmm =))=))=))=))\nsua e=))=))=))=))\nmau e=))=))=))\nmau de=))=))=))\ntk ga=))=))=))\nm cham a=))=))=))\nm cham ro=))=))=))=))\nm bia a=))=))=))\ntk nfu ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))\nalo alo=))=))=))=))=))\ncn choa ei=))=))=))=))\nmau ti k=))=))=))=))\nmau de=))=))=))=))=))\nalo alo=))=))=))=))\ncn tó ei=))=))=))\nmau ti e=))=))=))=))\nmau de=))=))=))=))\nyeu ot v=))=))=))\ntk ccho ei=))=))=))\nm tru noi k ay=))=))=))=))\ntk 3de=))=))=))=))\ncn ga ei=))=))=))=))\nm ga vl lun e=))=))=))=))\nalo alo=))=))=))\nsao ay nhi=))=))=))=))\nanh lai win a=))=))=))=))\nuoc loser ma=))=))=))=))\ntk nfu ei=))=))=))=))\nslow k ay=))=))=))\ncn cho =))=))=))\nspeed lun e=))=))=))\ntoi die k e=))=))=))\ntru ma=))=))=))\ntru ne tk nfu=))=))=))=))=))\nm tru k noi a=))=))=))=))=))\nm yeu v a=))=))=))=))\ntk ga ei=))=))=))=))\nmau k e=))=))=))=))\nmau de=))=))=))=))\nyeu z=))=))=))=))=))\ncn choa nfu=))=))=))=))=))\nsao do=))=))=))=))=))=))\nchay bo a=))=))=))=))=))\nbo manh vl=))=))=))=))\nbo dzi ba ro=))=))=))=))\nm chay a ma=))=))=))\nanh hot war ma e=))=))=))=))=))\nanh hot trụ cmnr=))=))=))=))=))\nm lam lai a k =))=))=))=))\nlam lai anh deo dau ma=))=))=))=))\nchay anh ro r=))=))=))=))\ncon gi khac k=))=))=))=))=))\nm bia a=))=))=))=))\ntk nfu ei=))=))=))=))\ncam m bia ma=))=))=))=))\nbia cn gia m dot tu e=))=))=))=))=))\nlofi chill k=))=))=))=))"
            )
            bot.send_message(message.chat.id, text_war)

    try:
        bot.infinity_polling(timeout=20, skip_pending=True)
    except: pass

def run_bots():
    filter_tokens()
    for token in VALID_TOKENS:
        threading.Thread(target=setup_bot, args=(token,)).start()
        time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    run_bots()
