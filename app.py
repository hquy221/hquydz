import telebot
import threading
from flask import Flask
import time
import requests
import os
import random

# --- HỆ THỐNG TOKEN ---
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

ADMIN_LIST = [7153197678]
VALID_BOTS = []
DELAY_TIME = 0.000000001
stop_event = threading.Event()
app = Flask(__name__)

# --- VĂN BẢN TUÔN THẲNG (GẤP 50 LẦN - ĐÃ TỐI ƯU RAM) ---
SPND_TEXT = "𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻"

SP36_TEXT = "cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=)) cn choa ei=))=))=))=))"

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))

def filter_system():
    global VALID_BOTS
    VALID_BOTS.clear()
    for t in RAW_TOKENS:
        try:
            r = requests.get(f"https://api.telegram.org/bot{t}/getMe", timeout=1).json()
            if r.get("ok"):
                # Hạ số thread xuống để tiết kiệm RAM cho Render
                bot = telebot.TeleBot(t, threaded=True, num_threads=100)
                bot.username = r['result']['username']
                VALID_BOTS.append(bot)
        except: continue

def bot_worker(bot, chat_id, mode, content="", target_id=None):
    while not stop_event.is_set():
        try:
            p_mode = None
            if mode == 'sp36':
                text = f"[{SP36_TEXT}](tg://user?id={target_id}) {get_noise()}"
                p_mode = "Markdown"
            elif mode == 'spnd':
                text = f"{SPND_TEXT} {get_noise()}"
            elif mode == 'sptag':
                text = f"[Sủa đi](tg://user?id={target_id}) {get_noise()}"
                p_mode = "Markdown"
            elif mode == 'splag':
                text = "LẮC ĐI CON CHÓ " * 40 + get_noise()
            elif mode == 'spdai':
                text = "SỦA ĐI CON THÚ\n" * 25 + get_noise()
            elif mode == 'spchui':
                text = f"ĐỊT MẸ MÀY CON CHÓ {get_noise()}"
            else:
                text = f"{content} {get_noise()}"
            
            bot.send_message(chat_id, text, parse_mode=p_mode)
            time.sleep(DELAY_TIME)
        except:
            time.sleep(0.01)

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

        # PHẢN HỒI LỆNH TỨC THÌ (0.000001S)
        if cmd in ['/spnd', '/sp36', '/sptag', '/splag', '/spdai', '/spchui', '/spam']:
            stop_event.clear()
            target_id = args[1] if len(args) > 1 else (m.reply_to_message.from_user.id if m.reply_to_message else None)
            master.send_message(m.chat.id, "🚀 ĐANG KHAI HỎA!")
            for b in VALID_BOTS:
                mode = cmd.replace('/', '')
                content = " ".join(args[1:]) if mode == 'spam' else ""
                threading.Thread(target=bot_worker, args=(b, m.chat.id, mode, content, target_id), daemon=True).start()

        # --- 14 LỆNH CHUẨN ---
        elif cmd == '/help':
            master.reply_to(m, "📖 **DANH SÁCH 14 LỆNH:**\n"
                               "1. `/help` - Xem lệnh\n"
                               "2. `/sp36 [id]` - Tag + văn bản 50x\n"
                               "3. `/sptag [id]` - Tag liên tục\n"
                               "4. `/info` - Xem ID\n"
                               "5. `/listbot` - Danh sách bot\n"
                               "6. `/listadm` - Danh sách Admin\n"
                               "7. `/setdelay [s]` - Chỉnh delay\n"
                               "8. `/addadm [id]` - Thêm Admin\n"
                               "9. `/xoaadm [id]` - Xóa Admin\n"
                               "10. `/spnd` - Spam nội dung 50x\n"
                               "11. `/spam [text]` - Spam tùy chỉnh\n"
                               "12. `/splag` - Spam lag\n"
                               "13. `/spdai` - Spam dài\n"
                               "14. `/spchui` - Spam chửi\n"
                               "15. `/dung` - Dừng lại", parse_mode="Markdown")
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
                if 0.0001 <= val <= 3.0:
                    DELAY_TIME = val
                    master.reply_to(m, f"⏱ Delay: {val}s")
                else: master.reply_to(m, "⚠️ Chỉ từ 0.0001 - 3.0")
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

    master.infinity_polling(timeout=1)

@app.route('/')
def home(): return "SYSTEM LIVE"

if __name__ == "__main__":
    filter_system() # Lọc token die ngay từ đầu
    port = int(os.environ.get("PORT", 10000))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master()
        except: time.sleep(0.1)
