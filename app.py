import telebot
import threading
import time
import random
from flask import Flask

# --- WEB SERVER GIỮ BOT SỐNG ---
app = Flask('')

@app.route('/')
def home():
    return "Hệ thống đang chạy ổn định!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# --- HỆ THỐNG TOKEN ---
RAW_TOKENS = [
    '8675065386:AAHVtY8NYQOykrCCEQ9tQDpe_mZK9XUmVV0', '8750639984:AAGAU7SsEe_V9CpZ9LAfxovI2iFWSCQ9riw',
    '8423233437:AAFPeFNFctZlgO8VU_KGkp_HT71FCTywUmI', '8705345450:AAHAxsFUHu7ux4USLvItL018KD4hBsTe4_Q',
    '8144155270:AAH-y47kIAFWgo7sge1VmCMrx2dc9CkYxOs', '8688293059:AAGoga_q3E7VbZQ3sL6xZ3-vzGgtC7RsTmc',
    '8652311818:AAGmFWSeRYW1-RQ-RH8jNguwkRtzFt0U-oQ', '8731497895:AAHHhCiAp7a62eflQBe0PztWw0jRjDPpyk4',
    '8684330434:AAEORwA4uvBXIm-orys4txSttOnkH2CRwZ4', '8796842934:AAENmEMod5CHQxfcl6Z5kl3nlwv8slQLJJc',
    '8668865669:AAGMgG3zBSN69eDYzTHENxl6Y9AAj6Kln4Q', '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18'
]

ADMIN_LIST = [7153197678]
VALID_BOTS = []
DELAY_TIME = 0.000000001
stop_event = threading.Event()

# --- VĂN BẢN TUÔN THẲNG (DÀI GẤP 5 LẦN) ---
SPND_CONTENT = "𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜゚̀ 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻"

SP36_CONTENT = "cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=)"

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))

def filter_system():
    global VALID_BOTS
    VALID_BOTS.clear()
    for t in RAW_TOKENS:
        try:
            bot = telebot.TeleBot(t, threaded=False)
            bot_info = bot.get_me()
            bot.username = bot_info.username
            VALID_BOTS.append(bot)
        except: continue

def bot_worker(bot, chat_id, mode, content="", target_id=None):
    while not stop_event.is_set():
        try:
            p_mode = None
            if mode == 'sp36':
                text = f"[{SP36_CONTENT}](tg://user?id={target_id}) {get_noise()}"
                p_mode = "Markdown"
            elif mode == 'spnd':
                text = f"{SPND_CONTENT} {get_noise()}"
            elif mode == 'sptag':
                text = f"[Sủa đi](tg://user?id={target_id}) {get_noise()}"
                p_mode = "Markdown"
            elif mode == 'splag':
                text = "LẮC ĐI CON CHÓ LẮC ĐI CON CHÓ LẮC ĐI CON CHÓ LẮC ĐI CON CHÓ LẮC ĐI CON CHÓ LẮC ĐI CON CHÓ LẮC ĐI CON CHÓ " + get_noise()
            elif mode == 'spdai':
                text = "SỦA ĐI CON THÚ\nSỦA ĐI CON THÚ\nSỦA ĐI CON THÚ\nSỦA ĐI CON THÚ\nSỦA ĐI CON THÚ\n" + get_noise()
            elif mode == 'spchui':
                text = f"ĐỊT MẸ MÀY CON CHÓ ĐỊT MẸ MÀY CON CHÓ {get_noise()}"
            else:
                text = f"{content} {get_noise()}"
            
            bot.send_message(chat_id, text, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except:
            time.sleep(0.3)
            break

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

        # CÁC LỆNH CHIẾN ĐẤU
        if cmd in ['/spnd', '/sp36', '/sptag', '/splag', '/spdai', '/spchui', '/spam']:
            stop_event.clear()
            target_id = args[1] if len(args) > 1 else (m.reply_to_message.from_user.id if m.reply_to_message else None)
            master.send_message(m.chat.id, "🔴SPAM ONL")
            for b in VALID_BOTS:
                mode = cmd.replace('/', '')
                content = " ".join(args[1:]) if mode == 'spam' else ""
                threading.Thread(target=bot_worker, args=(b, m.chat.id, mode, content, target_id), daemon=True).start()

        # ĐỦ 15 LỆNH THEO YÊU CẦU
        elif cmd == '/help':
            master.reply_to(m, "📖 **DANH SÁCH 15 LỆNH:**\n"
                               "1. /help - Xem lệnh\n"
                               "2. /sp36 [id] - Tag + văn bản cực dài\n"
                               "3. /sptag [id] - Tag liên tục\n"
                               "4. /info - Xem ID\n"
                               "5. /listbot - Danh sách bot\n"
                               "6. /listadm - Danh sách Admin\n"
                               "7. /setdelay [s] - Chỉnh delay\n"
                               "8. /addadm [id] - Thêm Admin\n"
                               "9. /xoaadm [id] - Xóa Admin\n"
                               "10. /spnd - Spam tràn màn hình\n"
                               "11. /spam [text] - Spam tùy chỉnh\n"
                               "12. /splag - Spam lag máy\n"
                               "13. /spdai - Spam dài vcl\n"
                               "14. /spchui - Spam chửi\n"
                               "15. /dung - Dừng lại", parse_mode="Markdown")
        elif cmd == '/info':
            tid = m.reply_to_message.from_user.id if m.reply_to_message else m.from_user.id
            master.reply_to(m, f"🆔 ID: `{tid}`", parse_mode="Markdown")
        elif cmd == '/listbot':
            msg = "\n".join([f"@{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 BOTS LIVE: {len(VALID_BOTS)}\n{msg}")
        elif cmd == '/listadm':
            master.reply_to(m, f"👥 ADMINS: `{ADMIN_LIST}`")
        elif cmd == '/setdelay':
            try:
                val = float(args[1])
                DELAY_TIME = val
                master.reply_to(m, f"⏱ Delay: {val}s")
            except: pass
        elif cmd == '/addadm':
            try:
                new_id = int(args[1])
                if new_id not in ADMIN_LIST: ADMIN_LIST.append(new_id)
                master.reply_to(m, "✅ Đã thêm.")
            except: pass
        elif cmd == '/xoaadm':
            try:
                rem_id = int(args[1])
                if rem_id in ADMIN_LIST: ADMIN_LIST.remove(rem_id)
                master.reply_to(m, "❌ Đã xóa.")
            except: pass
        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🛑 ĐÃ DỪNG.")

    master.infinity_polling(timeout=60, long_polling_timeout=30)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    filter_system()
    while True:
        try:
            start_master()
        except:
            time.sleep(0.001)
