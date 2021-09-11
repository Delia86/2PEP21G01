import tkinter

def user_pass():
    user="User1"
    passw="Password1"
    if state.get()==1:
        if username.get() != user:
            print("username is wrong")
        if password.get() != passw:
            print("password is wrong")
    else:
        print('box not checked')


main_window=tkinter.Tk()
main_window.title("Login")

label1=tkinter.Label(main_window,text='Username: ',bg='pink')
label1.grid(row=0,column=0,sticky=tkinter.E)
label1.config(width='20')

label2=tkinter.Label(main_window,text='Password: ',bg='pink')
label2.grid(row=1,column=0,sticky=tkinter.E)
label2.config(width='20')

username=tkinter.Entry(main_window)
username.grid(row=0,column=1)


password=tkinter.Entry(main_window)
password.grid(row=1,column=1)

login=tkinter.Button(main_window,text='login',highlightbackground='green',command=user_pass)
login.grid(row=3,column=0,sticky=tkinter.E)

cancel=tkinter.Button(main_window,text='cancel',highlightbackground='red',command=quit)
cancel.grid(row=3,column=1,sticky=tkinter.W)

state=tkinter.IntVar()
check_box = tkinter.Checkbutton(main_window,text="I'm not a robot",bg='light blue',variable=state)
check_box.grid(row=4,column=0,columnspan=2)

main_window.mainloop()