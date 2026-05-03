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

# --- VĂN BẢN /SPND (TUÔN DÀI GẤP 3 - KHÔNG RÚT GỌN) ---
SPND_TEXT = """𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻
𝗡𝗛𝗜̀𝗡 𝗖𝗔́𝗜 Đ𝗜̣𝗧 𝗠𝗘̣ 𝗠𝗔̀𝗬 🤣🤣🤪👌🏻"""

# --- VĂN BẢN /SP36 (GIỮ NGUYÊN TUÔN THẲNG) ---
SP36_TEXT = """cn choa ei=))=))=))=))
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
lofi chill k=))=))=))=))"""

# --- CẤU HÌNH HỆ THỐNG ---
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
                bot = telebot.TeleBot(t, threaded=True, num_threads=40)
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

def start_master():
    if not VALID_BOTS: return
    master = VALID_BOTS[0]
    
    @master.message_handler(func=lambda m: True)
    def handle_cmds(m):
        global DELAY_TIME, ADMIN_LIST
        if m.from_user.id not in ADMIN_LIST: return
        
        args = m.text.split()
        if not args: return
        cmd = args[0].lower()

        if cmd == '/addadm':
            try:
                nid = int(args[1])
                if nid not in ADMIN_LIST: ADMIN_LIST.append(nid)
                master.reply_to(m, f"✅ Admin Added: `{nid}`")
            except: pass
        elif cmd == '/xoaadm':
            try:
                rid = int(args[1])
                if rid in ADMIN_LIST and rid != 7153197678: ADMIN_LIST.remove(rid)
                master.reply_to(m, f"❌ Admin Removed: `{rid}`")
            except: pass
        elif cmd == '/listadm':
            master.reply_to(m, f"👥 Admins: `{ADMIN_LIST}`")
        elif cmd == '/listbot':
            bots = "\n".join([f"@{b.username}" for b in VALID_BOTS])
            master.reply_to(m, f"🤖 **BOTS ONLINE ({len(VALID_BOTS)}):**\n{bots}", parse_mode="Markdown")
        elif cmd == '/check':
            filter_system()
            master.reply_to(m, f"🔄 Reloaded. Live: {len(VALID_BOTS)}")
        elif cmd == '/info':
            target = m.reply_to_message.from_user.id if m.reply_to_message else m.from_user.id
            master.reply_to(m, f"🆔 ID: `{target}`", parse_mode="Markdown")
        elif cmd == '/setdelay':
            try:
                val = float(args[1])
                if 0.001 <= val <= 3.0:
                    DELAY_TIME = val
                    master.reply_to(m, f"⚡ Speed: `{DELAY_TIME}s`")
            except: pass
        elif cmd == '/spnd':
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spnd'), daemon=True).start()
        elif cmd == '/sp36':
            if len(args) < 2: return
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'sp36', "", args[1]), daemon=True).start()
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
        elif cmd == '/spam':
            content = " ".join(args[1:]) if len(args) > 1 else "cha hquy spam"
            stop_event.clear()
            for b in VALID_BOTS: threading.Thread(target=bot_worker, args=(b, m.chat.id, 'spam', content), daemon=True).start()
        elif cmd == '/dung':
            stop_event.set()
            master.reply_to(m, "🔴 STOPPED.")
        elif cmd == '/help':
            msg = "📜 **SYSTEM COMMANDS**\n1. /spnd\n2. /sp36 [ID]\n3. /sptag [ID]\n4. /spam [Text]\n5. /splag\n6. /spdai\n7. /dung\n8. /setdelay [s]\n9. /addadm [ID]\n10. /xoaadm [ID]\n11. /listadm\n12. /listbot\n13. /info\n14. /check"
            master.reply_to(m, msg, parse_mode="Markdown")

    master.infinity_polling(timeout=20)

@app.route('/')
def home(): return "SYSTEM ONLINE"

if __name__ == "__main__":
    filter_system()
    port = int(os.environ.get("PORT", 8080))
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port), daemon=True).start()
    while True:
        try: start_master()
        except: time.sleep(0.1)
