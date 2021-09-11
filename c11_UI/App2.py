import tkinter


class LoginWindow:
    login_info=None
    username = None
    password = None

    def __init__(self):
        self.main_window =tkinter.Tk()
        self.main_window.title('App 2')

        for count, txt in enumerate(['Username: ', 'Password: ']):
            label = tkinter.Label(self.main_window, text=txt)
            label.grid(row=count, column=0)

        for count, label in enumerate(['username', 'password']):
            self.__setattr__(label, tkinter.Entry(self.main_window))
            self.__getattribute__(label).grid(row=count, column=1)

        for count, txt in enumerate(['Login', 'Cancel']):
            button = tkinter.Button(self.main_window, text=txt, command=self.user_pass if not count else quit)
            button.grid(row=2, column=count, sticky=tkinter.E if not count else tkinter.W)

        self.state = tkinter.IntVar()
        check_box = tkinter.Checkbutton(self.main_window, text= "I'm not a robot", variable=self.state)
        check_box.grid(row=3, columnspan=2)


    def user_pass(self):
        usern = 'pinkiwinkiwinki555@gmail.com'
        passw = '1234pinki'
        if self.state.get() == 1:
            usr=self.username.get()
            print(usr)
            if usr != usern:
                print('username is wrong')
                raise RuntimeError('Wrong username')
            pwd=self.password.get()
            print(pwd)
            if pwd != passw:
                print('password is wrong')
                raise RuntimeError('Password wrong')
            self.login_info=(self.username.get(),self.password.get())
            self.main_window.quit()
        else:
            print('box not checked')
            raise RuntimeError ('Box not checked')



    def run(self):
        self.main_window.mainloop()

if __name__=='__main__':
    login = LoginWindow()
    login.run()
