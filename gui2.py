# more on labels, packing

import tkinter as tk

root = tk.Tk()
root.title("Welcome")
root.geometry('400x600')


myimage = tk.PhotoImage(file='rubber-duck-icon.png')

main_title = tk.Label(root, text="Welcome to the app", font=('Arial',24))
main_title.pack(pady = 20)

main_image = tk.Label(root, text='duct', image=myimage)
main_image.pack()

instructions = tk.Label (root,text="Please follow all instructions" )
instructions.pack(pady=(20, 5), anchor='w')

from tkinter import BOTH

body = tk.Label(root, text="Sucess!")
body.config(bg="FFFCC66")
body.pack(fill=BOTH, expand=True, padx=20, pady=20)


root.mainloop()