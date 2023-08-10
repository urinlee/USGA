from tkinter import *
import tkinter as tk
import threading
import os
import pip
from PIL import Image, ImageTk


class starting():
    def __init__(self, size=90): #생성자

        #GUI 구성
        self.root = Tk()
        self.root.title("MOLA Game Cient") #앱 이름

        #화면 정보
        self.monitor_width = self.root.winfo_screenwidth()      #모니터 가로
        self.monitor_height = self.root.winfo_screenheight()    #모니터 세로
        self.window_width = int(self.monitor_width * (size / 100))      #윈도우 가로
        self.window_height = int(self.monitor_height * (size / 100))    #윈도우 세로
        self.start_winx = int((self.monitor_width - self.window_width) / 2)     #윈도우 시작 위치_X
        self.start_winy = int((self.monitor_height - self.window_height) / 2)   #윈도우 시작 위치_Y
        
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.start_winx}+{self.start_winy}")

        
    def start(self):
        #Background
        bg_image_file = Image.open("sources/background.jpeg")
        bg_image_tk = ImageTk.PhotoImage(bg_image_file)
        label = tk.Label(self.root, image=bg_image_tk)
        label.place(x=-2, y=-2, relwidth=1, relheight=1)

        #start button
        start_button = Button(text="시작하기", borderwidth=0, background="white", width=20, height=3, command=self.start_game)
        start_button.place(x=self.window_width/2-130, y=self.window_height/2-100)
        self.root.mainloop()
    
    def start_load(self):   #로딩화면
        #self.root.quit()
        pass
        
    
    def load(self): #로딩(계산)
        pip.main(["install", "-r", "requirements.txt"])
        
    def start_game(self):
        threading.Thread(target=self.load).start()
        self.start_load()

if __name__ == "__main__":
    starting(80).start()
        
        
        
        
