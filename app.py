import telebot
import threading
import time
import random
import os
from flask import Flask

# --- HỆ THỐNG DUY TRÌ SERVER ---
app = Flask(__name__)
@app.route('/')
def home(): return "SYSTEM ONLINE"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH TOKEN ---
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
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', 
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', 
    '8650032681:AAE9TeiIIywG796f6hHLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', 
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', 
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4', 
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

ADMIN_LIST = [7153197678]
VALID_BOTS = []
DELAY_TIME = 0.01 
stop_event = threading.Event()
SIGNATURE = "\nADMIN:HQUY"

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=10))

# --- LOGIC SPAM SIÊU DÀI ---
def bot_worker(bot, chat_id, mode, content="", target_id=None):
    while not stop_event.is_set():
        try:
            if mode == 'sp36':
                base = f"[cn choa ei=))=))=))=) nhìn cái đéo gì=)) nhìn nổ mẹ hai con ngươi của mẹ m à=)) sủa lẹ lên con đĩ mẹ m ơi=)) m điếc à con chó đần=)) cha hquy no1=))](tg://user?id={target_id}) "
                text = (base * 30)[:3900] + get_noise() + SIGNATURE
            elif mode == 'spnd':
                base = "𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 𝗔̀ 𝗖𝗢𝗡 𝗖𝗛𝗢́ 𝗡𝗚𝗨 𝗖𝗛𝗔 𝗛𝗤𝗨𝗬 𝗡𝗢𝟭 𝗠𝗔̀ 𝗖𝗢𝗡 𝗖𝗛𝗢́ Đ𝗔̂̀𝗡 𝗦𝗨̉𝗔 𝗟𝗘̣ 𝗖𝗛𝗢 𝗖𝗛𝗔 Đ𝗜 𝗖𝗢𝗡 𝗖𝗛𝗢́ Đ𝗘̉ "
                text = (base * 40)[:3900] + get_noise() + SIGNATURE
            elif mode == 'sptag':
                base = f"[ĐỊT CON CỤ MÀY THẰNG NGU CHA HQUY NO1 MÀ SỦA LÊN ĐI CON CHÓ ĐẦN](tg://user?id={target_id}) "
                text = (base * 30)[:3900] + get_noise() + SIGNATURE
            elif mode == 'splag':
                text = ("꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟ " * 450)[:3900] + get_noise() + SIGNATURE
            elif mode == 'spchui':
                text = ("ĐỊT MẸ MÀY TH NQU CHA HQUY NO1 " * 120)[:3900] + get_noise() + SIGNATURE
            elif mode == 'spdai':
                text = (" ccho nqu cha hquy no1 ma\n" * 150)[:3900] + get_noise() + SIGNATURE
            else:
                text = ((content + " ") * 200)[:3900] + get_noise() + SIGNATURE
            
            bot.send_message(chat_id, text, parse_mode="Markdown" if mode in ['sp36', 'sptag'] else None)
            time.sleep(DELAY_TIME)
        except:
            time.sleep(0.5)

def filter_system():
    global VALID_BOTS
    for t in RAW_TOKENS:
        try:
            bot = telebot.TeleBot(t, threaded=False)
            me = bot.get_me()
            bot.username = me.username
            VALID_BOTS.append(bot)
        except: continue

def start_master():
    if not VALID_BOTS: return
    master = VALID_BOTS[0]

    @master.message_handler(func=lambda m: True)
    def handle_all(m):
        global DELAY_TIME, ADMIN_LIST
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        # --- 15 LỆNH THEO HÀNG DỌC ---
        if cmd == '/help':
            help_msg = (
                "📖 **LIST 15 LỆNH:**\n\n"
                "1. `/sp36`\n"
                "2. `/spnd`\n"
                "3. `/sptag`\n"
                "4. `/splag`\n"
                "5. `/spdai`\n"
                "6. `/spchui`\n"
                "7. `/spam`\n"
                "8. `/info`\n"
                "9. `/listbot`\n"
                "10. `/listadm`\n"
                "11. `/setdelay`\n"
                "12. `/addadm`\n"
                "13. `/xoaadm`\n"
                "14. `/dung`\n"
                "15. `/status`"
            )
            master.reply_to(m, help_msg, parse_mode="Markdown")
        
        elif cmd == '/info':
            target_id = m.reply_to_message.from_user.id if m.reply_to_message else m.from_user.id
            master.reply_to(m, f"🆔 ID: `{target_id}`", parse_mode="Markdown")

        elif cmd == '/addadm':
            if len(args) > 1 and args[1].isdigit():
                new_id = int(args[1])
                if new_id not in ADMIN_LIST:
                    ADMIN_LIST.append(new_id)
                    master.reply_to(m, f"✅ Đã thêm {new_id}")
            elif m.reply_to_message:
                new_id = m.reply_to_message.from_user.id
                if new_id not in ADMIN_LIST:
                    ADMIN_LIST.append(new_id)
                    master.reply_to(m, f"✅ Đã thêm {new_id}")

        elif cmd == '/xoaadm':
            if len(args) > 1 and args[1].isdigit():
                rem_id = int(args[1])
                if rem_id in ADMIN_LIST:
                    ADMIN_LIST.remove(rem_id)
                    master.reply_to(m, f"❌ Đã xóa {rem_id}")

        elif cmd == '/listadm':
            master.reply_to(m, f"📋 Admin: `{ADMIN_LIST}`", parse_mode="Markdown")

        elif cmd == '/listbot':
            bot_list = "\n".join([f"@{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 Online:\n{bot_list}")

        elif cmd == '/setdelay':
            if len(args) > 1:
                try:
                    DELAY_TIME = float(args[1])
                    master.reply_to(m, f"⚡ Delay: {DELAY_TIME}s")
                except: pass

        elif cmd in ['/sp36', '/spnd', '/sptag', '/splag', '/spdai', '/spchui', '/spam']:
            stop_event.clear()
            target_id = m.reply_to_message.from_user.id if m.reply_to_message else (args[1] if len(args) > 1 else m.from_user.id)
            master.send_message(m.chat.id, f"🚀 Start {cmd}...")
            for b in VALID_BOTS:
                mode = cmd.replace('/', '')
                content = " ".join(args[1:]) if mode == 'spam' else ""
                threading.Thread(target=bot_worker, args=(b, m.chat.id, mode, content, target_id), daemon=True).start()

        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🔴 SPAM OFF")

        elif cmd == '/status':
            master.reply_to(m, f"📊 {len(VALID_BOTS)} bots | Delay: {DELAY_TIME}s")

    while True:
        try:
            master.infinity_polling(timeout=60)
        except:
            time.sleep(0.01)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    filter_system()
    start_master()
