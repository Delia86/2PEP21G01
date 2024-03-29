# pylint: disable=missing-module-docstring
import tkinter
from tkinter import messagebox
from c11_UI.App2 import LoginWindow

import os,random

from functools import partial
import re


# pylint: disable=missing-class-docstring
class MenuWindow():
    # pylint: disable=missing-function-docstring
    def __init__(self,username:str):
        self.opened_file=None
        self.username=username
        root_window= tkinter.Tk()
        root_window.title("Menu")
        self.root_window = root_window

        main_menu = tkinter.Menu(root_window)
        self.root_window.config(menu=main_menu)

        file_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)

        edit_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label="Edit", menu=edit_menu)

        view_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label="View", menu=view_menu)

        send_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label="Send", menu=send_menu)

        file_menu.add_command(label='New', command=self.file_new_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Edit', command=self.file_edit_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Close', command=self.file_close_menu)

        self.frame1=tkinter.Frame(self.root_window,width=100,height=300)
        self.frame1.pack(side=tkinter.LEFT)
        refresh_button=tkinter.Button(self.frame1,text='refresh',command=self.get_directory)
        refresh_button.pack(side=tkinter.TOP)

        self.frame2 = tkinter.Frame(self.root_window)
        self.frame2.pack(side=tkinter.RIGHT)


        self.text = tkinter.Text(self.frame2, height=25, width=80)
        self.dest_entry = tkinter.Entry(self.frame2)
        self.subj_entry = tkinter.Entry(self.frame2)
        self.search_box = tkinter.Entry(self.frame2)
        self.searched_text = self.search_box.get()
        self.result = self.text.search(self.searched_text, "0.0", tkinter.END)

        self.receive_button=tkinter.Button

    def get_directory(self):
        i=0
        for dir in os.listdir():
            if os.path.isdir(dir):
                label=tkinter.Label(self.frame1,text=str(dir))
                label.pack()
            else:
                command=partial(self.load_message,dir)
                #x = random.randint(0, 10)
                #self.__setattr__('message' + str(i), dir[::])
                #y = self.__getattribute__('message' + str(x))
                label = tkinter.Button(self.frame1, text=str(dir), command=command)
                label.pack()



    def load_message(self,dir:str):

        with open(dir,'r')as file:
            self.opened_file = dir
            content=file.read()
        for line in content.splitlines():
            destination = re.match(r'^To:(.+)', line)
            if destination:
                self.dest_entry.insert('0',destination.group(1))
            continue
            subject=re.search(r'^Subject:(.+)', line)
            if subject:
                self.subj_entry.insert('0',subject.group(1))
            continue

        self.text.insert(tkinter.END,line +'\n')




    def run(self):
        self.root_window.mainloop()

    @staticmethod
    def file_new_menu():
        print("Creating new file...")
        # self.root_window.mainloop()
        new_main_window = tkinter.Tk()
        new_main_window.title("Copy of menu")
        new_menu = MenuWindow(new_main_window)
        new_menu.run()

    def file_edit_menu(self):
        print("Editing new file...")
        destination = tkinter.Label(self.frame2, text="TO: ")
        destination.grid(row=0, column=1, sticky=tkinter.E)
        subject = tkinter.Label(self.frame2, text="Subject: ")
        subject.grid(row=1, column=1, sticky=tkinter.E)

        self.dest_entry.grid(row=0, column=2, sticky=tkinter.W)
        self.subj_entry.grid(row=1, column=2, sticky=tkinter.W)
        send_button = tkinter.Button(self.frame2, text="Send", command=self.send_message)
        send_button.grid(row=0, rowspan=2, column=2)
        search_button = tkinter.Button(self.frame2, text='Search', command=self.search_message)
        search_button.grid(row=3, column=1)
        self.search_box.grid(row=3, column=2, columnspan=2, sticky=tkinter.NE + tkinter.SW)

        self.text.grid(row=2, columnspan=4)

    def save(self):
        to=self.dest_entry.get()
        subject=self.subj_entry.get()
        header=f"To: {to}\nSubject: {subject}\n"
        text=self.text.get('0.0',tkinter.END)
        result=header+text
        with open(self.opened_file,'w') as file:
            file.write(result)


    def search_message(self):
        # pylint: disable=use-maxsplit-arg
        var=str(int(self.result.split('.')[1]) + len(self.searched_text))
        self.text.tag_add('selection', self.result, self.result.split(".")[0] + '.' + var)
        self.text.tag_config("selection", background="yellow")

    def send_message(self):
        if not self.dest_entry.get():
            messagebox.showinfo("Warning", "Missing destination")
            return
        if not self.subj_entry.get():
            messagebox.showinfo("Warning", "Missing subject")
            return
        if not self.text.get("0.0", tkinter.END).strip():
            messagebox.showinfo("Warning", "Missing text")
            return

        answer = messagebox.askquestion("Confirmation", "Are you sure you want to send?")
        if answer == "yes":
            print("Running code...")
            self.save()
        else:
            print("Canceling...")

    def file_close_menu(self):
        self.root_window.quit()

login=LoginWindow()
login.run()


menu = MenuWindow(login.login_info)
menu.run()