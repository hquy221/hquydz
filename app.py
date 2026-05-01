import telebot
import threading
from flask import Flask
import time
import requests
import os
import random

# --- HỆ THỐNG TOKEN (Tự động lọc khi khởi động) ---
RAW_TOKENS = [
    '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18', '8481938728:AAGen1t8Tz3jeu02kJ8HoCIZLiPLdd687n8',
    '8739448460:AAGNLEW-WDvatbxmPLzkziG5jpd5hTRfqiE', '8689807630:AAEoXvm45QaW1jlT-H_KzNlmCpu50Q3k2S4',
    '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0',
    '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0',
    '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c',
    '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM',
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA',
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0',
    '8650032681:AAE9TeiIIywG796f6hHLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0',
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY',
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4',
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

# --- KHO VĂN BẢN CHIẾN (GẤP 3 LẦN) ---
CHUI_LIST = [
    "cn choa ei=))=))=))=))", "123=))=))=))=))", "m chay anh cmnr=))=))=))=))=))", 
    "m yeu ot z tk nfu=))=))=))=))=))", "m cham vl e=))=))=))", "slow lun e=))=))=))=))",
    "yeu z cn dix=))=))=))=))", "tk 3de=))=))=))=))=))", "tk dix lgbt=))=))=))=))",
    "cn choa nfu=))=))=))=))=))", "deo co canh lun e=))=))=))=))", "m cham vl e=))=))=))=))",
    "m yeu v=))=))=))=))=))=))", "yeu ro=))=))=))=))=))=))", "bia a=))=))=))=))",
    "alo may cn cho nu=)) =)) =))", "sua e=))=))=))=))", "tk ga=))=))=))", "m cham a=))=))=))",
    "m cham ro=))=))=))=))", "m bia a=))=))=))", "tk nfu ei=))=))=))=))",
    "alo alo=))=))=))=))=))", "cn choa ei=))=))=))=))", "mau ti k=))=))=))=))",
    "a đấng hot war mà=))=))=))=))", "cmm chối à=))=))=))=))", "a hw mẹ r=))=))=))=))",
    "con gi dau ma noi =))=))=))=))", "a treo co me m ma=))=))=))=))", "a win ma=))=))=))=))",
    "le de alo =))=))=))=))", "m chạy a mà=))=))=))=))", "tk nu=))=))=))=))=))",
    "tru ma=))=))=))", "tru ne tk nfu=))=))=))=))=))", "m tru k noi a=))=))=))=))=))",
    "anh hot war ma e=))=))=))=))=))", "anh hot trụ cmnr=))=))=))=))=))", 
    "lofi chill k=))=))=))=))", "cay k cn ccho ei=))=))=))=))", "m tru de=))=))=))=))",
    "sao cam nín v e=))=))=))", "m nín ro r=))=))=))=))", "tk nfu bất lực=))=))=))=))",
    "anh ba đạo quá mà=))=))=))", "uớc đc đối thủ=))=))=))=))", "m yếu vcl e=))=))=))",
    "speed lên de tk ngu=))=))=))", "m lỳ k e=))=))=))=))", "tk rách nát=))=))=))=))",
    "cn choa die r=))=))=))=))", "m óc vcl e=))=))=))=))", "chạy đi cn tó=))=))=))",
    "m câm à e=))=))=))=))", "sủa lên t nghe=))=))=))=))", "m hụt hơi r=))=))=))=))",
    "m rách cmnr=))=))=))=))", "anh win chặt=))=))=))=))", "cn gia m die ro=))=))=))=))",
    "m khóc de e=))=))=))=))", "m mếu r=))=))=))=))", "tk lofi chill lòi=))=))=))",
    "m gãy r=))=))=))=))", "anh dập m nát gáy=))=))=))=))", "m tru deo noi=))=))=))=))",
    "tk ocs cho ei=))=))=))=))", "m k có trình=))=))=))=))", "trình m tuổi j=))=))=))=))",
    "anh vả m vỡ mồm=))=))=))=))", "m ngáo r e=))=))=))=))", "m sập r à=))=))=))=))",
    "đái ra quần chưa e=))=))=))", "m tuổi tôm à=))=))=))=))", "tk rách nát hôi hám=))=))=))",
    "m quỳ xuống de=))=))=))=))", "khóc lóc j nx=))=))=))=))", "m bất lực ro=))=))=))=))",
    "m hết hơi r à=))=))=))=))", "sủa mạnh lên xem=))=))=))=))", "anh là ông nội m=))=))=))",
    "m chỉ là rác rưởi=))=))=))=))", "đớp cứt đi cn=))=))=))=))", "m lặn mất tăm v=))=))=))",
    "sao im de v e=))=))=))=))", "m sợ anh ro k=))=))=))=))", "tk phế vật nfu=))=))=))=))",
    "m nát bét ro e=))=))=))=))", "anh vả lệch hàm m=))=))=))", "m có trình j k=))=))=))",
    "m sủa j v e=))=))=))=))", "m cay lắm đúng k=))=))=))", "anh cho m ăn hành=))=))=))",
    "m hụt hơi cmnr=))=))=))=))", "m lag lòi mắt r=))=))=))=))", "tk đần độn ei=))=))=))=))",
    "m câm như hến v=))=))=))=))", "m đuối r à cn=))=))=))=))", "anh là trùm m mà=))=))=))"
]

VALID_BOTS = []
ADMIN_LIST = [7153197678] 
DELAY_TIME = 0.1
stop_event = threading.Event()
app = Flask(__name__)

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=3))

def filter_system():
    global VALID_BOTS
    VALID_BOTS.clear()
    for t in RAW_TOKENS:
        try:
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=3).json()
            if r.get("ok"):
                bot = telebot.TeleBot(t)
                bot.username = r['result']['username']
                VALID_BOTS.append(bot)
        except: continue

def bot_worker(bot, chat_id, mode, content="", target_id=None):
    while not stop_event.is_set():
        try:
            p_mode = None
            if mode == 'spnd':
                text = f"{random.choice(CHUI_LIST)} {get_noise()}"
            elif mode == 'sptag':
                text = f"[Sủa đi con chó ngu](tg://user?id={target_id}) {get_noise()}"
                p_mode = "Markdown"
            else:
                text = f"{content} {get_noise()}"
            
            bot.send_message(chat_id, text, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except Exception as e:
            if "retry after" in str(e).lower():
                time.sleep(5)
            continue

def start_master():
    if not VALID_BOTS: return
    master = VALID_BOTS[0]

    @master.message_handler(func=lambda m: True)
    def handle_cmds(m):
        global DELAY_TIME
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        if cmd == '/spam':
            content = " ".join(args[1:]) if len(args) > 1 else "QUÂN ĐOÀN KHAI HỎA!!!"
            stop_event.clear()
            for b in VALID_BOTS:
                threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spam', content), daemon=True).start()
            master.reply_to(m, f"🚀 23 Bot xả: {content}")

        elif cmd == '/spnd':
            stop_event.clear()
            for b in VALID_BOTS:
                threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spnd'), daemon=True).start()
            master.reply_to(m, "🔥 KHAI HỎA KHO CHỬI SIÊU DÀI!")

        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🛑 DỪNG CHIẾN.")

        elif cmd == '/xoaadm':
            try:
                target_id = int(args[1])
                if target_id in ADMIN_LIST and target_id != 7153197678:
                    ADMIN_LIST.remove(target_id)
                    master.reply_to(m, f"✅ Đã xóa Admin: {target_id}")
            except: pass

        elif cmd == '/addadm':
            try:
                new_id = int(args[1])
                if new_id not in ADMIN_LIST: 
                    ADMIN_LIST.append(new_id)
                    master.reply_to(m, f"✅ Đã thêm Admin: {new_id}")
            except: pass

        elif cmd == '/setdelay':
            try:
                v = float(args[1])
                if 0.001 <= v <= 2.5:
                    DELAY_TIME = v
                    master.reply_to(m, f"⚡ Delay: {v}s")
            except: pass

        elif cmd == '/listbot':
            list_b = "\n".join([f"✅ @{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 Online ({len(VALID_BOTS)}):\n{list_b}")

        elif cmd == '/listadm':
            master.reply_to(m, f"👥 Admins: {ADMIN_LIST}")

        elif cmd == '/info':
            tid = m.reply_to_message.from_user.id if m.reply_to_message else (args[1] if len(args)>1 else m.from_user.id)
            master.reply_to(m, f"🆔 ID: {tid}")

        elif cmd == '/help':
            msg = ("🚀 **LỆNH:**\n"
                   "`/spam [nội dung]`\n"
                   "`/spnd` (Kho chửi x3)\n"
                   "`/sptag [ID]`\n"
                   "`/dung` | `/setdelay`\n"
                   "`/addadm` | `/xoaadm` | `/listadm` | `/listbot`")
            master.reply_to(m, msg, parse_mode="Markdown")

    master.infinity_polling(timeout=15, skip_pending=True)

@app.route('/')
def home(): return "ACTIVE"

if __name__ == "__main__":
    filter_system()
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master()
        except: time.sleep(5)
