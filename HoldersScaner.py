import os
import time
import json
import tkinter as jra
from threading import Thread
from tkinter import messagebox
from tkinter import font as tkfont
from MODEL.get_value import get_setting_value
from scaner_canvas import ScanerCanvas

logo = "./DATA/img/logo.ico"
img_render = './DATA/img/render.png'
title_tool = "Holders Scaner"
bg_color = "#C7CAC6"
stop_color = "#263942"
btn_color = "#ffffff"
text_btn_color = "#263942"

# LOGO_PATH="pic/logo.ico"
# LOGO_LINUX_PATH="@pic/logo_1.xbm"  #do not forget "@" symbol and .xbm format for Ubuntu 
#     if detect_screen_size().detect_os()=="Linux":
#         root.iconbitmap(LOGO_LINUX_PATH)
#     else:
#         root.iconbitmap(LOGO_PATH)

class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title(title_tool)
        # master.iconbitmap(logo)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        hi = 1300
        wi = 800
        x, y = ws / 2 - hi / 2 , hs / 2 - wi / 2 
        master.geometry('%dx%d+%d+%d' % (hi, wi, x, y))

        # <------------------------------ field ------------------------------>
        self.theonly = None
        self.keep_running = True
        self.win = None
        self.entries = None
        # <------------------------------ field  ------------------------------>

        self.canvas_batdau = jra.Frame(self, width=50)

        # <------------------------------ column=0 ------------------------------>

        self.font = tkfont.Font(family='Helvetica', size=12, weight="bold")

        row_idx = 0
        jra.Label(self.canvas_batdau, bg=bg_color).grid(row=row_idx, column=0)
        row_idx += 1

        self.buttonSoSanh = jra.Button(self.canvas_batdau, text="Setting", font=self.font,
                                       fg=btn_color, bg=text_btn_color, width=20, height=1)
        self.buttonSoSanh["command"] = self.open1
        self.buttonSoSanh.grid(row=row_idx, column=0)
        row_idx += 1
        jra.Label(self.canvas_batdau,bg=bg_color).grid(row=row_idx, column=0)
        row_idx += 1
    
        # <------------------------------ frame_container ------------------------------>

        self.frame_container = jra.Frame(self.canvas_batdau,
                                       bg="pink", width=20, height=20)
        self.frame_container.grid(row=row_idx, column=0)
        row_idx += 1
        # <------------------------------ scaner ------------------------------>
        for col in range(3):
            for row_idx_con in range(4):
                scan = ScanerCanvas(self.frame_container, bg_color)
                scan.grid(row=row_idx_con, column=col)
        # <------------------------------ scaner ------------------------------>

        # <------------------------------ frame_container ------------------------------>
    

        # <------------------------------ column=0 ------------------------------>
        self.canvas_batdau.grid(row=0, column=0)

        self.huongDan = jra.Label(self, text="\nBất kì vấn đề nào \n phudinhtruongk18@gmail.com", width=60, bg=bg_color)
        self.huongDan.grid(row=row_idx, column=0)
        row_idx += 1

        self.canvas_batdau.configure(bg=bg_color)
        self.configure(bg=bg_color)
        master.configure(bg=bg_color)

        self.grid()
        self.mainloop()

    def open1(self):
        self.win = jra.Toplevel()
        self.win.title("Setting")
        # self.win.iconbitmap(logo)

        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x, y = ws / 2 - 950, hs / 2 - 400
        self.win.geometry('%dx%d+%d+%d' % (300, 120, x, y))

        # Income, Age, Experience, CCAvg, Mortgage
        labels = [jra.Label(self.win, text="Timer:")]
        self.entries = [
            jra.Entry(self.win)
        ]

        data_temp = [get_setting_value()]

        for index, (label, entry) in enumerate(zip(labels, self.entries)):
            label.pack()
            entry.insert(0, data_temp[index])
            entry.pack()

        jra.Button(self.win, bg="#263942", fg="#ffffff", text="Save", command=self.save_command).pack()
        self.win.mainloop()

    def save_command(self):
        data_pre = [entry.get() for entry in self.entries]
        if data_pre.__len__() == 1:
            try:
                setting = {
                    'timer': int(data_pre[0]),
                }

                with open("./DATA/setting.json", "w") as jsonfile:
                    json.dump(setting, jsonfile)
            except Exception as e:
                messagebox.showwarning("Wrong", "Make sure your data is right: \n" + str(e))
                return
        print("------------------------------------------------------")
        messagebox.showinfo("Done", "Set Success!")
        self.win.destroy()

print("Hello")
giaoDien = jra.Tk()
app = Application(master=giaoDien)