# gui 1
"""
Steps to crearing a tkinder GUI app"
1. import tkinder
2. create the main GUI window(usually called root; sometimes master)
3. add widgets to the window (e.g., labels, buttons, text fields...)
4. run the root window's mainloop() method
"""
import tkinter

root = tkinter.Tk()
root.title('TEC-322')
root.geometry('200x400')
root.resizable(True, False)

root.config (bg='lightskyblue')

"""
1.pack()
2.grid()
"""
name = tkinter.Label(text = 'My name is Maksat')
name['bg'] =  name.master['bg']
name.pack()

root.mainloop()
