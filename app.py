import telebot
import threading
import time
import random
import os
from flask import Flask

# --- HỆ THỐNG CẤU HÌNH ---
app = Flask(__name__)
@app.route('/')
def home(): return "SYSTEM ALIVE - SPAM MODE ACTIVE"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- DANH SÁCH TOKEN ĐÃ XOÁ 5 CON THEO YÊU CẦU ---
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
DELAY_TIME = 0.000000001
stop_event = threading.Event()

# --- VĂN BẢN TUÔN THẲNG DÀI GẤP 20 LẦN (THÔ) ---
SPND_CONTENT = "𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻 𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻"
SP36_CONTENT = "cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=) cn choa ei=))=))=))=)"

def get_noise():
    return "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=10))

# --- CORE SPAM ---
def bot_worker(bot, chat_id, mode, content="", target_id=None):
    while not stop_event.is_set():
        try:
            if mode == 'sp36': text = f"[{SP36_CONTENT}](tg://user?id={target_id}) {get_noise()}"
            elif mode == 'spnd': text = f"{SPND_CONTENT} {get_noise()}"
            elif mode == 'sptag': text = f"[ĐỊT CON CỤ MÀY](tg://user?id={target_id}) {get_noise()}"
            elif mode == 'splag': text = ("꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰kk ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰ ꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰" * 50) + get_noise()
            elif mode == 'spdai': text = (" ccho nqu cha hquy no1 ma\n" * 50) + get_noise()
            elif mode == 'spchui': text = ("ĐỊT MẸ MÀY TH NQU CHA HQUY NO1 " * 20) + get_noise()
            else: text = f"{content} {get_noise()}"
            
            bot.send_message(chat_id, text, parse_mode="Markdown" if 'sp' in mode else None)
            time.sleep(0.001)
        except Exception:
            time.sleep(0.1) # EXCEPT NGHỈ 0.1S NHƯ YÊU CẦU

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

        # CÁC LỆNH SPAM
        if cmd in ['/spnd', '/sp36', '/sptag', '/splag', '/spdai', '/spchui', '/spam']:
            stop_event.clear()
            target_id = args[1] if len(args) > 1 else (m.reply_to_message.from_user.id if m.reply_to_message else None)
            master.send_message(m.chat.id, "🚀 SPAM ONL!")
            for b in VALID_BOTS:
                mode = cmd.replace('/', '')
                content = " ".join(args[1:]) if mode == 'spam' else ""
                threading.Thread(target=bot_worker, args=(b, m.chat.id, mode, content, target_id), daemon=True).start()

        # ĐỦ 15 LỆNH ĐIỀU KHIỂN
        elif cmd == '/help':
            help_text = (
                "📖 **MENU✈️:**\n"
                "1. /help - Xem menu lệnh\n"
                "2. /sp36 - Văn bản xả thẳng dài vcl\n"
                "3. /spnd - Spam (x20)\n"
                "4. /sptag - Tag th lồn óc cặc"
                "5. /splag - Gửi tin nhắn qrtf\n"
                "6. /spdai - Spam dái chó\n"
                "7. /spchui - ĐUỔI CHÓ\n"
                "8. /spam - Spam nội dung tự chọn\n"
                "9. /info - Check ID người dùng\n"
                "10. /listbot - Xem danh sách bot live\n"
                "11. /listadm - Xem danh sách Admin\n"
                "12. /setdelay - Chỉnh tốc độ (giây)\n"
                "13. /addadm - Thêm Admin mới\n"
                "14. /xoaadm - Xoá Admin\n"
                "15. /dung - STOP🔴"
            )
            master.reply_to(m, help_text, parse_mode="Markdown")
        elif cmd == '/info':
            tid = m.reply_to_message.from_user.id if m.reply_to_message else m.from_user.id
            master.reply_to(m, f"🆔 ID: `{tid}`", parse_mode="Markdown")
        elif cmd == '/listbot':
            msg = "\n".join([f"@{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 BOTS LIVE: {len(VALID_BOTS)}\n{msg}")
        elif cmd == '/listadm':
            master.reply_to(m, f"👥 ADMINS: `{ADMIN_LIST}`")
        elif cmd == '/setdelay':
            try: DELAY_TIME = float(args[1]); master.reply_to(m, f"⏱ Delay: {args[1]}s")
            except: pass
        elif cmd == '/addadm':
            try:
                nid = int(args[1]); (ADMIN_LIST.append(nid) if nid not in ADMIN_LIST else None); master.reply_to(m, "✅ Đã thêm.")
            except: pass
        elif cmd == '/xoaadm':
            try:
                rid = int(args[1]); (ADMIN_LIST.remove(rid) if rid in ADMIN_LIST else None); master.reply_to(m, "❌ Đã xoá.")
            except: pass
        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "STOP🔴")

    master.infinity_polling(timeout=60)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    filter_system()
    while True:
        try: start_master()
        except: time.sleep(0.001)
