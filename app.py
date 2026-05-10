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

# --- DANH SÁCH 29 TOKEN CỦA SẾP ---
RAW_TOKENS = [
    '8675065386:AAHVtY8NYQOykrCCEQ9tQDpe_mZK9XUmVV0', '8750639984:AAGAU7SsEe_V9CpZ9LAfxovI2iFWSCQ9riw',
    '8423233437:AAFPeFNFctZlgO8VU_KGkp_HT71FCTywUmI', '8705345450:AAHAxsFUHu7ux4USLvItL018KD4hBsTe4_Q',
    '8144155270:AAH-y47kIAFWgo7sge1VmCMrx2dc9CkYxOs', '8688293059:AAGoga_q3E7VbZQ3sL6xZ3-vzGgtC7RsTmc',
    '8652311818:AAGmFWSeRYW1-RQ-RH8jNguwkRtzFt0U-oQ', '8731497895:AAHHhCiAp7a62eflQBe0PztWw0jRjDPpyk4',
    '8684330434:AAEORwA4uvBXIm-orys4txSttOnkH2CRwZ4', '8796842934:AAENmEMod5CHQxfcl6Z5kl3nlwv8slQLJJc',
    '8668865669:AAGMgG3zBSN69eDYzTHENxl6Y9AAj6Kln4Q', '8429960682:AAHltNvwWjEn1QC_f5R8JPgz7uN1uFhny18', 
    '8481938728:AAGen1t8Tz3jeu02kJ8HoCIZLiPLdd687n8', '8739448460:AAGNLEW-WDvatvatMplzkziG5pd5hTRfqiE', 
    '8689807630:AAEoXvm45QaW1jlT-H_KzNlmCpu50Q3k2S4', '8575475228:AAHRtsOcCEQInRvR3isSBV-Igur-WykB_PE', 
    '8651553692:AAGNQwqUoWgV1QV0ozaZHLRL0RJm9M8q0e0', '8712129360:AAEgW2hBbtsgY8DyMd9mxYw1B6X8_VBpF-g', 
    '8626439785:AAEn2pArlYu0KW9tHLETtrJUXKo2BR0hjx0', '8793582382:AAHfbcee8kt-x6OeLHqwqXP79U4PBaII0MA', 
    '8397463503:AAGajcEI5H_SJ0i6mccvPT7GC-P8U5RTLOQ', '8718672219:AAH37zxnCBuWLMSEW_rCvEwnrf0ym8d7-H0', 
    '8650032681:AAE9TeiIIywG796f6hHLN7JiBWhNgH3gc', '8303481123:AAFN_bijtWzXlR1FlYHEvgN-5uhyqnZsbu0', 
    '8619086108:AAFYqRAdKNvg84eyj1ylXfa-TF8W8o8fxbo', '8661308767:AAFU__yZv8r1HlJ5jaW3URW88bWKWYKDCCY', 
    '8625550674:AAHIHuakDCvvxwCC0mgrDLU5g8vBNFdD7eI', '8724848112:AAHhLYnH1LO4tVUPMTjztbNZZtni7D0uDl4', 
    '8471422557:AAF30BcMF15veQPHCTDqcA1NU0iHb63Zm1o'
]

# ID Của Sếp (Chủ sở hữu cao nhất)
OWNER_ID = 7153197678
ADMIN_LIST = [7153197678]

VALID_BOTS = []
DELAY_TIME = 0.05 
stop_event = threading.Event()
SIGNATURE = "\n𖣘 Hai Quy NO1 𖣘"

# --- DATA VĂN BẢN (MỖI CÂU 1 DÒNG) ---
SPND_LIST = [
    "cn choa ei=))=))=))=))
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
lofi chill k=))=))=))=))"
]

SP_LIST = [
    "bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊 bố tung skill 1 sút là con mẹ mày chết liền lun 🤪👊con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏 con chó ảo war lên đây ngồi xàm loz cho t đụ vô loz bà già nó hay sao mà nó cứ nhảm nhảm đú gì 🤣🙏học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =)) học cách phản kháng bố để giải cứu con mẹ mày xem =))óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :)) óc cứt múa may quay cuồng để bị cha sỉ vả vào cái mặt cứt mày à :))mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :)) mặt lồn mày sao k 44 theo mẹ m đi :))"
]

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=8))

# --- LOGIC GỬI TIN ---
def bot_worker(bot, chat_id, mode, content="", target_id=None):
    count = 0
    while not stop_event.is_set():
        try:
            text = ""
            parse_m = None
            if mode == 'sp':
                text = f"{SP_LIST[count % len(SP_LIST)]} {get_noise()}{SIGNATURE}"
                count += 1
            elif mode == 'spnd':
                text = f"{SPND_LIST[count % len(SPND_LIST)]} {get_noise()}{SIGNATURE}"
                count += 1
            elif mode == 'sp2':
                text = f"{content} {get_noise()}{SIGNATURE}"
            elif mode == 'sptag':
                text = f"SỦA MAU CON CHÓ [\u200b](tg://user?id={target_id}) {get_noise()}{SIGNATURE}"
                parse_m = "Markdown"

            bot.send_message(chat_id, text, parse_mode=parse_m)
            time.sleep(DELAY_TIME)
        except: time.sleep(0.1)

# --- KHỞI CHẠY ---
def filter_system():
    global VALID_BOTS
    for t in RAW_TOKENS:
        try:
            bot = telebot.TeleBot(t, threaded=False)
            bot.get_me()
            VALID_BOTS.append(bot)
        except: continue

def start_master():
    if not VALID_BOTS: return
    master = VALID_BOTS[0]

    @master.message_handler(func=lambda m: True)
    def handle_all(m):
        global DELAY_TIME, ADMIN_LIST
        
        # Kiểm tra quyền Admin
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        # --- MENU QUẢN TRỊ ---
        if cmd == '/addadm':
            if m.from_user.id != OWNER_ID:
                master.reply_to(m, "❌ Chỉ Boss Hai Quy mới có quyền thêm Admin!")
                return
            try:
                new_id = int(args[1]) if len(args) > 1 else (m.reply_to_message.from_user.id if m.reply_to_message else None)
                if new_id and new_id not in ADMIN_LIST:
                    ADMIN_LIST.append(new_id)
                    master.reply_to(m, f"✅ Đã thêm `{new_id}` vào danh sách Admin.", parse_mode="Markdown")
                else:
                    master.reply_to(m, "❌ ID không hợp lệ hoặc đã là Admin.")
            except: master.reply_to(m, "❌ Lệnh: `/addadm <id>` hoặc reply tin nhắn.")

        elif cmd == '/xoaadm':
            if m.from_user.id != OWNER_ID:
                master.reply_to(m, "❌ Chỉ Boss Hai Quy mới có quyền xóa Admin!")
                return
            try:
                del_id = int(args[1]) if len(args) > 1 else (m.reply_to_message.from_user.id if m.reply_to_message else None)
                if del_id == OWNER_ID:
                    master.reply_to(m, "❌ Không thể xóa Boss khỏi hệ thống!")
                elif del_id in ADMIN_LIST:
                    ADMIN_LIST.remove(del_id)
                    master.reply_to(m, f"🗑️ Đã xóa `{del_id}` khỏi danh sách Admin.", parse_mode="Markdown")
                else:
                    master.reply_to(m, "❌ ID này không có trong danh sách Admin.")
            except: master.reply_to(m, "❌ Lệnh: `/xoaadm <id>` hoặc reply tin nhắn.")

        elif cmd == '/listadm':
            msg = "👥 **DANH SÁCH ADMIN HỆ THỐNG:**\n"
            for idx, adm in enumerate(ADMIN_LIST):
                msg += f"{idx+1}. `{adm}` {'(BOSS)' if adm == OWNER_ID else ''}\n"
            master.reply_to(m, msg, parse_mode="Markdown")

        # --- MENU CHÍNH ---
        elif cmd == '/help':
            menu_text = (
                ". 　˚　. . ✦˚ .     　　˚　　　　✦　.\n"
                "𖣘 Hai Quy.   2026 𖣘\n"
                ".  ˚　.　 . ✦　˚　 .   .　.  　˚　  　.\n\n"
                "🔥 𝑺𝒑𝒂𝒎 & 𝑻𝒂𝒈\n"
                "┣ /sp - Spam chửi\n"
                "┣ /sp2 <nd> - Spam nội dung\n"
                "┣ /spnd - Spam treo\n"
                "┣ /sptag - Spam tag\n"
                "┗ /stop - Dừng tất cả\n\n"
                "☠ 𝑸𝒖𝒂‌𝒏 𝑻𝒓𝒊‌ 𝑨𝒅𝒎𝒊𝒏\n"
                "┣ /addadm <id/rep> - Thêm Admin\n"
                "┣ /xoaadm <id/rep> - Xóa Admin\n"
                "┗ /listadm - Xem danh sách Admin\n\n"
                "📦 𝑳𝒂‌𝒕 𝑽𝒂‌𝒕\n"
                "┣ /info <@/id/rep> - Soi ID\n"
                "┣ /clear - Dọn box (100 tin)\n"
                "┣ /setdelay <giây> - Tốc độ\n"
                "┗ /listbot - Check số lượng bot\n\n"
                "👤 ADMIN: Hquy"
            )
            master.reply_to(m, menu_text)

        # --- CÁC LỆNH CHIẾN ĐẤU ---
        elif cmd in ['/sp', '/spnd', '/sp2', '/sptag']:
            stop_event.clear()
            tid = m.reply_to_message.from_user.id if m.reply_to_message else m.from_user.id
            content = " ".join(args[1:]) if cmd == '/sp2' else ""
            master.send_message(m.chat.id, f"🚀 **KHAI HỎA CHIẾN DỊCH:** `{cmd.upper()}`")
            for b in VALID_BOTS:
                threading.Thread(target=bot_worker, args=(b, m.chat.id, cmd.replace('/',''), content, tid), daemon=True).start()

        elif cmd == '/stop':
            stop_event.set()
            master.reply_to(m, "🛑 BOT ĐÃ NGỪNG XẢ ĐẠN.")

        elif cmd == '/info':
            target_id = None
            if len(args) > 1:
                if args[1].startswith('@'):
                    try: target_id = master.get_chat(args[1]).id
                    except: pass
                else: target_id = args[1]
            elif m.reply_to_message: target_id = m.reply_to_message.from_user.id
            else: target_id = m.from_user.id
            master.reply_to(m, f"🔍 ID ĐỐI TƯỢNG: `{target_id}`", parse_mode="Markdown")

        elif cmd == '/setdelay':
            try:
                DELAY_TIME = float(args[1])
                master.reply_to(m, f"⏳ Tốc độ: {DELAY_TIME}s")
            except: pass

        elif cmd == '/listbot':
            master.reply_to(m, f"🤖 Bot đang Online: {len(VALID_BOTS)}/29")

        elif cmd == '/clear':
            try:
                for i in range(1, 101):
                    master.delete_message(m.chat.id, m.message_id - i)
            except: pass

    master.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    filter_system()
    start_master()

