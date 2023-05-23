import tkinter as jra
from tkinter import messagebox
from tkinter import font as tkfont

from MODEL.get_value import get_setting_value
from faker_thread import TheOne


class ScanerCanvas(jra.Frame):
    def __init__(self, master=None,bg_color = "white"):
        super().__init__(master)

        self.font = tkfont.Font(family='Helvetica', size=11, weight="bold")
        self.bg_color = bg_color

        self.timer = 60
        self.theone = None
        self.old_holders = ""

        # <------------------------------ parent ------------------------------>
        self.huongDan = jra.Label(self, text="\nInit Complete", bg=self.bg_color)
        self.huongDan.grid(row=0, column=1)

        self.left = jra.Frame(self, width=30, bg=self.bg_color)
        self.left.grid(row=1, column=0)

        self.right = jra.Frame(self, width=50, bg=self.bg_color)
        self.right.grid(row=1, column=1)
        # <------------------------------ parent ------------------------------>

        row_idx = 0
        # <------------------------------ row 0  ------------------------------>
        # right
        self.btn = jra.Button(self.left, text="Run", font=self.font,bg="#61F276",width=15)
        self.btn.configure(command=self.run_scaner)
        self.btn.grid(row=row_idx, column=0)
        # left
        self.token = jra.Entry(self.right, font=self.font,bg=self.bg_color,width=30)
        self.token.grid(row=row_idx, column=0)
        row_idx += 1
        # <------------------------------ row 0  ------------------------------>
        # <------------------------------ row 1  ------------------------------>
        # right
        label1 = jra.Label(self.left, text="Note", font=self.font, bg=self.bg_color,width=20)
        label1.grid(row=row_idx, column=0)
        # left
        self.note = jra.Text(self.right, font=self.font,bg=self.bg_color,width=30,height=2)
        self.note.grid(row=row_idx, column=0)
        row_idx += 1
        # <------------------------------ row 1  ------------------------------>
        # <------------------------------ row 2  ------------------------------>
        # right
        label2 = jra.Label(self.left, text="Name", font=self.font, bg=self.bg_color)
        label2.grid(row=row_idx, column=0)
        # left
        self.name = jra.Entry(self.right, font=self.font,bg=self.bg_color,width=30)
        self.name.grid(row=row_idx, column=0)
        row_idx += 1
        # <------------------------------ row 2  ------------------------------>
        # <------------------------------ row 3  ------------------------------>
        # right
        label3 = jra.Label(self.left, text="New Holders", font=self.font, bg=self.bg_color)
        label3.grid(row=row_idx, column=0)
        # left
        self.new = jra.Entry(self.right, font=self.font,width=30,bg="#C7CAC6")
        self.new.grid(row=row_idx, column=0)
        row_idx += 1
        # <------------------------------ row 3  ------------------------------>
        # <------------------------------ row 4  ------------------------------>
        # right
        label4 = jra.Label(self.left, text="Old Holders", font=self.font, bg=self.bg_color)
        label4.grid(row=row_idx, column=0)
        # left
        self.old = jra.Entry(self.right, font=self.font,width=30,bg="#C7CAC6")
        self.old.grid(row=row_idx, column=0)
        row_idx += 1
        # <------------------------------ row 4  ------------------------------>

        self.configure(bg=self.bg_color)

    def run_scaner(self):
        self.timer = get_setting_value()
        # get token with try catch
        token = self.token.get()
        if token == "":
            messagebox.showinfo("Error", "Token is empty")
            return
        print(token)
        print(self.timer)
        self.is_running = True

        self.get_and_change(token=token)

        self.huongDan.configure(text="\nRun Complete")
        self.btn.configure(text="Stop",bg="#DB6C6B")
        self.btn["command"] = self.stop_thread

    def stop_thread(self):
        self.theone.is_alive_mine = False

    def stop_scaner(self):
        self.is_running = False
        # clear entry and text field
        self.token.delete(0, 'end')
        self.note.delete(1.0, 'end')
        self.name.delete(0, 'end')
        self.new.delete(0, 'end')
        self.old.delete(0, 'end')

        self.huongDan.configure(text="\nStop Complete")
        self.btn.configure(text="Run",bg="#61F276")
        self.btn["command"] = self.run_scaner
        

    def get_and_change(self,token):
        self.theone = TheOne(address=token,ui = self,timer = self.timer)
        self.theone.start()

    def update_ui(self,holders, name, date):
        self.old.delete(0, 'end')
        self.old.insert(0, self.old_holders)

        self.name.delete(0, 'end')
        self.name.insert(0, name)
        self.new.delete(0, 'end')
        self.new.insert(0, holders)
        self.huongDan.configure(text="\nUpdate "+str(date))
        self.old_holders = holders
