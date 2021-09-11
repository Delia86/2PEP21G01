import tkinter

from tkinter import messagebox

main_window = tkinter.Tk()
main_window.title("menu")


class MenuWindow():

    def __init__(self, root_window: tkinter.Tk):
        self.root_window = root_window

        main_menu = tkinter.Menu(root_window)
        self.root_window.config(menu=main_menu)

        file_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='New', command=self.file_new_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Edit', command=self.file_edit_menu)

        file_menu.add_separator()
        file_menu.add_command(label='Close', command=self.file_close_menu)

        edit_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='Edit', menu=edit_menu)

        view_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='View', menu=view_menu)

        send_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='Send', menu=send_menu)

    def run(self):
        self.root_window.mainloop()

    def file_new_menu(self):
        print('Creating new file...')
        # self.root_window.mainloop()
        new_main_window = tkinter.Tk()
        new_main_window.title("Copy of menu")
        menu = MenuWindow(new_main_window)
        menu.runpy

    def file_edit_menu(self):
        print('Editing  new file...')
        self.text = tkinter.Text(self.root_window, height=25, width=80)
        destination = tkinter.Label(self.root_window, text='TO:')
        destination.grid(row=0, column=0, sticky=tkinter.E)
        subject = tkinter.Label(self.root_window, text='SUBJECT:')
        subject.grid(row=1, column=0, sticky=tkinter.E)
        self.dest_entry = tkinter.Entry(self.root_window)
        self.dest_entry.grid(row=0, column=1, sticky=tkinter.W)
        self.dest_subject = tkinter.Entry(self.root_window)
        self.dest_subject.grid(row=1, column=1, sticky=tkinter.W)
        send_button = tkinter.Button(self.root_window, text='Send', command=self.send_message)
        send_button.grid(row=0, rowspan=2, column=2)
        search_button = tkinter.Button(self.root_window, text='Search', command=self.search_message)
        search_button.grid(row=3, column=0)
        self.search_box = tkinter.Entry(self.root_window)
        self.search_box.grid(row=3, column=1, columnspan=2, sticky=tkinter.NE + tkinter.SW)

        self.text.grid(row=2, columnspan=3)

    def send_message(self):
        if not self.dest_entry.get():
            messagebox.showinfo('Warning', 'Missing destination')
            return

        if not self.dest_subject.get():
            messagebox.showinfo('Warning', 'Missing subject')
            return

        if not self.text.get(0.0, tkinter.END.strip()):
            messagebox.showinfo('Warning', 'Missing text')
            return

        answer = tkinter.messagebox.askquestion('Confirmation', 'Are you sure you want to send?')
        if answer == 'yes':
            print('Running code...')
        else:
            print('Canceling...')

    def search_message(self):

        self.searched_text = self.search_box.get()
        self.result = self.text.search(self.searched_text, '0.0', tkinter.END)
        print(self.result)
        self.text.tag_add('selection', self.result, self.result.split(".")[0] + '.' + str(
            int(self.result.split('.')[1]) + len(self.searched_text)))
        self.text.tag_config('selection', background='yellow')

    def file_close_menu(self):
        self.root_window.quit()


menu = MenuWindow(main_window)
menu.run()
