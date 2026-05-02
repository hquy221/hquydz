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

# --- KHO VĂN BẢN (X3) ---
CHUI_LIST = [
    "cn choa ei=))=))=))=))", "m chay anh cmnr=))=))=))=))=))", "m yeu ot z tk nfu=))=))=))=))=))", 
    "m cham vl e=))=))=))", "slow lun e=))=))=))=))", "yeu z cn dix=))=))=))=))", 
    "tk 3de=))=))=))=))=))", "tk dix lgbt=))=))=))=))", "cn choa nfu=))=))=))=))=))", 
    "deo co canh lun e=))=))=))=))", "m yeu v=))=))=))=))=))=))", "yeu ro=))=))=))=))=))=))",
    "alo may cn cho nu=)) =)) =))", "sua e=))=))=))=))", "tk ga=))=))=))", "m cham a=))=))=))",
    "cn tó ei=))=))=))", "anh lai win a=))=))=))=))", "a đấng hot war mà=))=))=))=))", 
    "cay k cn ccho ei=))=))=))=))", "sao cam nín v e=))=))=))", "tk nfu bất lực=))=))=))=))",
    "speed lên de tk ngu=))=))=))", "cn choa die r=))=))=))=))", "m câm à e=))=))=))=))", 
    "m rách cmnr=))=))=))=))", "cn gia m die ro=))=))=))=))", "m mếu r=))=))=))=))", 
    "anh dập m nát gáy=))=))=))=))", "yeu ot vcl=))=))=))=))", "m k có trình=))=))=))=))",
    "trình m tuổi j=))=))=))=))", "anh vả m vỡ mồm=))=))=))=))", "m sập r à=))=))=))=))",
    "đái ra máu r à con thú=))=))=))=))", "sủa mạnh lên xem nào=))=))=))=))", "cay lòi mắt r chứ j=))=))=))",
    "anh là bậc thầy spam=))=))=))=))", "m tuổi tôm đòi đú=))=))=))=))", "nhìn m thảm hại vl=))=))=))=))",
    "anh chấp cả lò nhà m=))=))=))=))", "m gãy cánh r e ơi=))=))=))=))", "m mới thế đã khóc r=))=))=))=))",
    "trình còi đừng ra gió=))=))=))=))", "m tịt ngòi r à=))=))=))=))", "anh dẫm m nát bấy=))=))=))=))",
    "m rách nát vl=))=))=))=))", "anh vả m lệch hàm=))=))=))=))", "sủa tiếp đi con thú=))=))=))=))",
    "m bất lực r e=))=))=))=))", "anh là huyền thoại war=))=))=))=))", "m chỉ là rác rưởi=))=))=))=))",
    "m cay anh lắm đúng k=))=))=))=))", "nhìn m như con cún=))=))=))=))", "anh dập m tới tấp=))=))=))=))",
    "m hụt hơi r kìa=))=))=))=))", "anh là ác mộng của m=))=))=))=))", "m run cầm cập r=))=))=))=))",
    "anh tiễn m về trời=))=))=))=))", "m rên rỉ đi e=))=))=))=))", "anh bẻ gãy gáy m=))=))=))=))",
    "m hết thời r e=))=))=))=))", "anh là chúa tể war=))=))=))=))", "m câm nín đi con=))=))=))=))",
    "anh quật m tơi tả=))=))=))=))", "m nhục nhã vl=))=))=))=))", "anh đứng trên đầu m=))=))=))=))",
    "m là thằng bại trận=))=))=))=))", "anh tiễn m ra đảo=))=))=))=))", "m tắt đài r e=))=))=))=))",
    "anh là vô địch spam=))=))=))=))", "m sợ anh r chứ j=))=))=))=))", "anh dìm m xuống bùn=))=))=))=))",
    "m khóc tiếng mán r=))=))=))=))", "nhìn m đuối vl e=))=))=))=))", "anh xả m nát xác=))=))=))=))",
    "trình m chỉ để anh dẫm=))=))=))=))", "sủa hăng lên nào con chó=))=))=))=))", "m gục ngã r à e=))=))=))=))",
    "anh hành m ra bã=))=))=))=))", "m là phế thải thôi=))=))=))=))", "anh bóp nghẹt gáy m=))=))=))=))",
    "m quỳ xuống lạy anh đi=))=))=))=))", "anh dập cho m hết sủa=))=))=))=))", "m chỉ là dế thôi=))=))=))=))"
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
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=1).json()
            if r.get("ok"):
                bot = telebot.TeleBot(t, threaded=True, num_threads=15)
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
            elif mode == 'splag':
                text = f"LẮC ĐI CON CHÓ {get_noise()} " * 20
            elif mode == 'spdai':
                text = f"SỦA ĐI CON THÚ {get_noise()}\n" * 15
            else:
                text = f"{content} {get_noise()}"
            
            bot.send_message(chat_id, text, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except:
            time.sleep(0.01)
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

        # --- LỆNH TẤN CÔNG (SPEED 0.1s) ---
        if cmd == '/spam':
            content = " ".join(args[1:]) if len(args) > 1 else "cha hquy spam"
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spam', content), daemon=True).start()

        elif cmd == '/spnd':
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spnd'), daemon=True).start()

        elif cmd == '/sptag':
            if len(args) < 2: return
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'sptag', "", args[1]), daemon=True).start()

        elif cmd == '/splag':
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'splag'), daemon=True).start()

        elif cmd == '/spdai':
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spdai'), daemon=True).start()

        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🔴stop")

        # --- LỆNH QUẢN TRỊ & HỆ THỐNG ---
        elif cmd == '/info':
            target = m.reply_to_message.from_user.id if m.reply_to_message else m.from_user.id
            master.reply_to(m, f"🆔 ID: `{target}`", parse_mode="Markdown")

        elif cmd == '/listadm':
            adms = "\n".join([f"👤 `{a}`" for a in ADMIN_LIST])
            master.reply_to(m, f"👥 **ADMIN:**\n{adms}", parse_mode="Markdown")

        elif cmd == '/listbot':
            bot_names = "\n".join([f"🤖 @{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🔥 **BOT ({len(VALID_BOTS)}):**\n{bot_names}")

        elif cmd == '/setdelay':
            try:
                DELAY_TIME = float(args[1])
                master.reply_to(m, f"⚡ Delay: `{DELAY_TIME}s`")
            except: pass

        elif cmd == '/addadm':
            try:
                nid = int(args[1])
                if nid not in ADMIN_LIST: ADMIN_LIST.append(nid); master.reply_to(m, f"✅ Added: `{nid}`")
            except: pass

        elif cmd == '/xoaadm':
            try:
                rid = int(args[1])
                if rid != 7153197678 and rid in ADMIN_LIST: ADMIN_LIST.remove(rid); master.reply_to(m, f"✅ Removed: `{rid}`")
            except: pass

        elif cmd == '/help':
            help_text = (
                "🆘 **ĐỦ 12 LỆNH CỦA ÔNG:**\n"
                "1. `/spam`: Spam nội dung\n"
                "2. `/spnd`: Spam chửi X3\n"
                "3. `/sptag`: Tag đối thủ\n"
                "4. `/splag`: Spam lag máy\n"
                "5. `/spdai`: Spam dòng dài\n"
                "6. `/dung`: Dừng toàn bộ\n"
                "7. `/info`: Lấy ID\n"
                "8. `/listbot`: Kiểm tra dàn bot\n"
                "9. `/listadm`: Danh sách admin\n"
                "10. `/addadm`: Thêm admin\n"
                "11. `/xoaadm`: Xóa admin\n"
                "12. `/setdelay`: Chỉnh tốc độ"
            )
            master.reply_to(m, help_text, parse_mode="Markdown")

    master.infinity_polling(timeout=10, long_polling_timeout=2)

@app.route('/')
def home(): return "POWERFUL"

if __name__ == "__main__":
    filter_system()
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master()
        except: time.sleep(0.1)
