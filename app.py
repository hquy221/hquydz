import telebot
import threading
from flask import Flask
import time
import requests
import os
import random

# --- DANH SÁCH 34 TOKEN ---
RAW_TOKENS = [
    '8675065386:AAHVtY8NYQOykrCCEQ9tQDpe_mZK9XUmVV0', '8750639984:AAGAU7SsEe_V9CpZ9LAfxovI2iFWSCQ9riw',
    '8423233437:AAFPeFNFctZlgO8VU_KGkp_HT71FCTywUmI', '8705345450:AAHAxsFUHu7ux4USLvItL018KD4hBsTe4_Q',
    '8144155270:AAH-y47kIAFWgo7sge1VmCMrx2dc9CkYxOs', '8688293059:AAGoga_q3E7VbZQ3sL6xZ3-vzGgtC7RsTmc',
    '8652311818:AAGmFWSeRYW1-RQ-RH8jNguwkRtzFt0U-oQ', '8731497895:AAHHhCiAp7a62eflQBe0PztWw0jRjDPpyk4',
    '8684330434:AAEORwA4uvBXIm-orys4txSttOnkH2CRwZ4', '8796842934:AAENmEMod5CHQxfcl6Z5kl3nlwv8slQLJJc',
    '8668865669:AAGMgG3zBSN69eDYzTHENxl6Y9AAj6Kln4Q', '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18', 
    '8481938728:AAGen1t8Tz3jeu02kJ8HoCIZLiPLdd687n8', '8739448460:AAGNLEW-WDvatbxmPLzkziG5jpd5hTRfqiE', 
    '8689807630:AAEoXvm45QaW1jlT-H_KzNlmCpu50Q3k2S4', '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', 
    '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', 
    '8716604939:AAH2isXOrU_J8gyRlrsqnfem6Y4F3eUwg_0', '8734778356:AAF1ZZbigLFn4TDKnFPJ7KIhSRNT2b8UFnc', 
    '8750340566:AAG_fJhmqgs1X67kJybsG3i1uBYCNELqV9c', '8612349553:AAFGMoIgICvQH5DK3BuFQnT9AkR8i__4kIo', 
    '8697555066:AAEmP-XxiwDynhMgNWPsANr1hksg5mhHLhM', '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', 
    '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', 
    '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', '8650032681:AAE9TeiIIywG796f6hHLN7JiBWhNgH3gc', 
    '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', 
    '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', 
    '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4', '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

# --- KHO VĂN BẢN CHIẾN (Gấp 3 lần) ---
CHUI_LIST = [
    "cn choa ei=))=))=))=))", "123=))=))=))=))", "m chay anh cmnr=))=))=))=))=))", 
    "m yeu ot z tk nfu=))=))=))=))=))", "m cham vl e=))=))=))", "slow lun e=))=))=))=))",
    "yeu z cn dix=))=))=))=))", "tk 3de=))=))=))=))=))", "tk dix lgbt=))=))=))=))",
    "cn choa nfu=))=))=))=))=))", "deo co canh lun e=))=))=))=))", "m cham vl e=))=))=))=))",
    "m yeu v=))=))=))=))=))=))", "yeu ro=))=))=))=))=))=))", "bia a=))=))=))=))",
    "alo may cn cho nu=)) =)) =))", "sua e=))=))=))=))", "tk ga=))=))=))", "m cham a=))=))=))",
    "m bia a=))=))=))", "cn tó ei=))=))=))", "yeu ot v=))=))=))", "anh lai win a=))=))=))=))",
    "a đấng hot war mà=))=))=))=))", "con gi dau ma noi =))=))=))=))", "lofi chill k=))=))=))=))",
    "cay k cn ccho ei=))=))=))=))", "m tru de=))=))=))=))", "sao cam nín v e=))=))=))",
    "tk nfu bất lực=))=))=))=))", "anh ba đạo quá mà=))=))=))", "speed lên de tk ngu=))=))=))",
    "cn choa die r=))=))=))=))", "m câm à e=))=))=))=))", "sủa lên t nghe=))=))=))=))",
    "m rách cmnr=))=))=))=))", "m bia nx di=))=))=))=))", "cn gia m die ro=))=))=))=))",
    "m mếu r=))=))=))=))", "tk lofi chill lòi=))=))=))=))", "m gãy r=))=))=))=))",
    "anh dập m nát gáy=))=))=))=))", "yeu ot vcl=))=))=))=))", "m k có trình=))=))=))=))",
    "trình m tuổi j=))=))=))=))", "anh vả m vỡ mồm=))=))=))=))", "m sập r à=))=))=))=))",
    "lofi chill de e=))=))=))=))", "m duoi r ak=))=))=))=))", "cay k em ei=))=))=))=))",
    "tk ngu hoc=))=))=))=))", "m mat dang r ak=))=))=))=))", "anh ba dao lam=))=))=))=))",
    "m tuoi lon=))=))=))=))", "cn cho nfu=))=))=))=))", "slow roi e=))=))=))=))",
    "m tit roi ak=))=))=))=))", "lofi chill di cưng=))=))=))=))", "m bi anh vả vỡ gáy=))=))=))=))",
    "m yeu qua di=))=))=))=))", "m gãy r cưng=))=))=))=))", "anh la dang ma=))=))=))=))",
    "m tuoi j san san vs anh=))=))=))=))", "m rách roi=))=))=))=))", "sủa tiep di e=))=))=))=))",
    "anh ba đạo quá mà=))=))=))", "m khóc r ak=))=))=))=))", "lofi chill lòi tĩ=))=))=))=))",
    "m yeu ot vl=))=))=))=))", "m duoi r ak cn cho=))=))=))=))", "anh ba dao thiet=))=))=))=))",
    "m tuoi j doi win anh=))=))=))=))", "m rot cmnr=))=))=))=))", "m cham kinh=))=))=))=))",
    "anh ba dao nhat=))=))=))=))", "m yeu ot z e=))=))=))=))", "m rot mang ak=))=))=))=))",
    "lofi chill de=))=))=))=))", "m tuoi j=))=))=))=))", "anh ba dao=))=))=))=))",
    "m gãy r=))=))=))=))", "m rot roi=))=))=))=))", "anh ba dao qua=))=))=))=))",
    "m tuoi lon de win anh=))=))=))=))", "m cham vl e=))=))=))=))", "m rot de=))=))=))=))",
    "anh ba dao lam e=))=))=))=))", "m tuoi lon doi win=))=))=))=))", "m yeu ot=))=))=))=))"
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
                text = f"[Sủa đi con chó ngu này](tg://user?id={target_id}) {get_noise()}"
                p_mode = "Markdown"
            else:
                text = f"{content} {get_noise()}"
            
            bot.send_message(chat_id, text, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except Exception as e:
            if "retry after" in str(e).lower():
                time.sleep(0) # Theo ý ông: Bỏ nghỉ khi bị chặn
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
            master.reply_to(m, f"🚀 {len(VALID_BOTS)} Bot khai hỏa!")

        elif cmd == '/spnd':
            stop_event.clear()
            for b in VALID_BOTS:
                threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spnd'), daemon=True).start()
            master.reply_to(m, f"🔥 Xả kho chửi X3!")

        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🛑 DỪNG.")

        elif cmd == '/listbot':
            list_b = "\n".join([f"✅ @{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 Online ({len(VALID_BOTS)}):\n{list_b}")

    master.infinity_polling(timeout=15, skip_pending=True)

@app.route('/')
def home(): return "SYSTEM ONLINE"

if __name__ == "__main__":
    filter_system()
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master()
        except: 
            time.sleep(0) # Theo ý ông: Bỏ nghỉ nếu lỗi Master
