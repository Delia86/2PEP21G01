import tkinter

main_window=tkinter.Tk()
main_window.title('Python M2 UI')

label3=tkinter.Label(main_window,text='Blue Label',bg='blue')
label3.pack(fill=tkinter.X)
label4=tkinter.Label(main_window,text='Yellow Label',bg='yellow')
label4.pack(side=tkinter.BOTTOM,fill=tkinter.X)
label1=tkinter.Label(main_window,text='Red Label',bg='red')
label1.pack(side=tkinter.RIGHT,fill=tkinter.Y)
label2=tkinter.Label(main_window,text='Green Label',bg='green')
label2.pack(side=tkinter.LEFT,fill=tkinter.Y)
label5=tkinter.Label(main_window,text='Pink',bg='pink')
label5.pack(side=tkinter.LEFT,fill=tkinter.Y)


main_window.mainloop()


print('All done')