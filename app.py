import asyncio
import random
import html
import logging
import sys
import re
import time
from threading import Event
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode
from telegram import ReplyKeyboardMarkup

# --- ĐOẠN CODE THÊM VÀO ĐỂ CHẠY FREE TRÊN RENDER ---
from threading import Thread
import os
from http.server import SimpleHTTPRequestHandler
import socketserver

def chay_server_gia_lap():
    # Render sẽ tự động cấp một cổng ngẫu nhiên qua biến môi trường PORT
    port = int(os.environ.get("PORT", 8080))
    handler = SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"[Render] Đang duy trì cổng server giả lập tại: {port}")
            httpd.serve_forever()
    except Exception as e:
        print(f"[Render] Lỗi server giả lập: {e}")

# Chạy server giả lập ở một luồng riêng để không ảnh hưởng đến bot Telegram
Thread(target=chay_server_gia_lap, daemon=True).start()
# --------------------------------------------------

logging.basicConfig(level=logging.ERROR)

BOT_TOKENS = [
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
    '84714225
