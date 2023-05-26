import tkinter as jra
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfilename, askdirectory
from job import extract_data

# logo = "./DATA/img/logo.ico"
img_render = './DATA/img/img.png'
bg_color = "white"
stop_color = "#263942"
btn_color = "#ffffff"
text_btn_color = "#263942"

def openThuMuc(link=""):
    os.startfile(f'{os.path.realpath("") + link}')

class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        title_tool = "BSC Analyzer"
        master.title(title_tool)
        # master.iconbitmap(logo)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x, y = ws / 2 - 300 / 2, hs / 2 - 300
        master.geometry('%dx%d+%d+%d' % (300, 150, x, y))

        # create a space 
        jra.Label().pack()
        # entry
        # self.url_input = jra.Entry(master, width=30)
        # self.url_input.pack()
        # jra.Label().pack()

        self.hi_there = jra.Button(self)
        self.hi_there["text"] = "Bắt đầu chạy chương trình"
        self.hi_there["command"] = self.PressCheck
        self.hi_there.pack()

        self.openThuMuc = jra.Button(self)
        self.openThuMuc["text"] = "Mở thư mục"
        self.openThuMuc["command"] = openThuMuc
        self.openThuMuc.pack()

        self.pack()

    def PressCheck(self, event=None):
        # get text from entry
        folder_path = askopenfilename(initialdir="")
        extract_data(folder_path)
        if messagebox.askyesno("Đã hoàn thành!", "Mở thư mục?"):
            openThuMuc()


root = jra.Tk()
app = Application(master=root)
app.mainloop()