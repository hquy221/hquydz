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

# --- DANH SÁCH TOKEN (GIỮ NGUYÊN 29 TOKEN) ---
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
DELAY_TIME = 0.05 
stop_event = threading.Event()
SIGNATURE = "\nADMIN:HQUY"

# --- DANH SÁCH CÂU SPTAG ---
SPTAG_TEXTS = [
    "123 con chó cùng sủa =))", "con gái mẹ mày làm đĩ từ lúc sống đến khi chết mà 🤣", "con đĩ phàn kháng cha được không ấy",
    "thằng cha mày gánh lúa cho mày đi đú à :))", "mẹ đĩ mày dắt mày vô sàn à :))", "con điếm bị bố sỉ nhục", "không phục à",
    "phản kháng lại những câu sỉ vả của cha xem :))", "con chó học cách làm người à 👉🤣", "con chó ăn cứt :))", "phế phẩm vậy em",
    "con chó mồ côi 🤙", "mày ngu vậy sao không off mxh luôn đi 🤣👋", "max speed được không ấy con chó ei 👉🤪", "lại phải win à 😁",
    "sồn mau không con đĩ mẹ m chết", "thằng cặc bất hiếu", "mẹ mày bị anh chơi suốt năm suốt tháng mà 😛", "sồn để cứu con mẹ mày mau🥺👋",
    "cha win cmnr :))", "bố cầm shotgun bắn thủng não con đĩ ngu :))", "mặt cứt mày phế phẩm vậy em", "con chó đú ửa à 🤪",
    "thằng ngu ei 👉😛", "phản kháng bố mau 😒", "còn sự sống không ấy thằng nqu ei :))", "mxh là cách duy nhất để mày sống ak :))",
    "thua bố không phục ak :))", "đĩ lồn ăn cứt trâu để sống qua ngày à 🤣", "thằng ngu cố nhai nốt mấy câu để cầu cứu con gái mẹ m nha :))"
    # ... (Ông có thể paste thêm nốt các câu còn lại vào list này)
]

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))

# --- LOGIC XỬ LÝ NỘI DUNG TỪNG LỆNH ---
def bot_worker(bot, chat_id, mode, content="", target_id=None):
    count = 0
    while not stop_event.is_set():
        try:
            if mode == 'sptag':
                msg_index = count % len(SPTAG_TEXTS)
                text = f"{SPTAG_TEXTS[msg_index]} {get_noise()}{SIGNATURE}"
                count += 1
            
            elif mode == 'sp36':
                base = f"[cn choa ei=))=))=))=) nhìn cái đéo gì=)) nhìn nổ mẹ hai con ngươi của mẹ m à=)) sủa lẹ lên con đĩ mẹ m ơi=)) m điếc à con chó đần=)) cha hquy no1=))](tg://user?id={target_id}) "
                text = (base * 30)[:3900] + get_noise() + SIGNATURE
                
            elif mode == 'spnd':
                base = "𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 𝗔̀ 𝗖𝗢𝗡 𝗖𝗛𝗢́ 𝗡𝗚𝗨 𝗖𝗛𝗔 𝗛𝗤𝗨𝗬 𝗡𝗢𝟭 𝗠𝗔̀ 𝗖𝗢𝗡 𝗖𝗛𝗢́ Đ𝗔̂̀𝗡 𝗦𝗨̉𝗔 𝗟𝗘̣ 𝗖𝗛𝗢 𝗖𝗛𝗔 Đ𝗜 𝗖𝗢𝗡 𝗖𝗛𝗢́ Đ𝗘̉ "
                text = (base * 40)[:3900] + get_noise() + SIGNATURE
                
            elif mode == 'splag':
                text = ("꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟ " * 450)[:3900] + get_noise() + SIGNATURE
                
            elif mode == 'spdai':
                text = (" ccho nqu cha hquy no1 ma\n" * 150)[:3900] + get_noise() + SIGNATURE
                
            elif mode == 'spchui':
                text = ("ĐỊT MẸ MÀY TH NQU CHA HQUY NO1 " * 120)[:3900] + get_noise() + SIGNATURE
                
            else: # Lệnh /spam
                text = ((content + " ") * 150)[:3900] + get_noise() + SIGNATURE
            
            bot.send_message(chat_id, text, parse_mode="Markdown" if mode in ['sp36', 'sptag'] else None)
            time.sleep(DELAY_TIME)
        except:
            time.sleep(0.01)

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

        if cmd == '/help':
            help_msg = (
                "📖 **LIST MENU✈️:**\n\n"
                "1. `/sp36` - Spam tag + nội dung sp36\n"
                "2. `/spnd` - Spam nội dung nhìnditme\n"
                "3. `/sptag` - Spam list 150 câu (Từng dòng)\n"
                "4. `/splag` - Spam ký tự gây lag chat\n"
                "5. `/spdai` - Spam văn bản xuống dòng dài\n"
                "6. `/spchui` - Spam nội dung chửi rủa\n"
                "7. `/spam` - Spam nội dung tự chọn\n"
                "8. `/info` - Xem ID (Reply người khác)\n"
                "9. `/listbot` - Xem danh sách bot online\n"
                "10. `/listadm` - Xem danh sách Admin\n"
                "11. `/setdelay` - Chỉnh tốc độ spam\n"
                "12. `/addadm` - Thêm ID Admin\n"
                "13. `/xoaadm` - Xóa ID Admin\n"
                "14. `/dung` - Dừng tất cả (SPAM OFF)\n"
                "15. `/status` - Check trạng thái bot"
            )
            master.reply_to(m, help_msg, parse_mode="Markdown")

        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🔴 SPAM OFF")

        elif cmd in ['/sp36', '/spnd', '/sptag', '/splag', '/spdai', '/spchui', '/spam']:
            stop_event.clear()
            target_id = m.reply_to_message.from_user.id if m.reply_to_message else (args[1] if len(args) > 1 else m.from_user.id)
            master.send_message(m.chat.id, f"🚀 Start {cmd}...")
            for b in VALID_BOTS:
                mode = cmd.replace('/', '')
                content = " ".join(args[1:]) if mode == 'spam' else ""
                threading.Thread(target=bot_worker, args=(b, m.chat.id, mode, content, target_id), daemon=True).start()

    while True:
        try: master.infinity_polling(timeout=60)
        except: time.sleep(0.01)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    filter_system()
    start_master()
