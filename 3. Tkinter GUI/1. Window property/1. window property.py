from tkinter import *

win = Tk()

# changing title name
win.title("Window Property Using Tkinter")

# changing icon
# Format in .ico
win.iconbitmap(r"sample logo.ico")

# Transparenting the window
# alpha 0 to 1
win.attributes('-alpha', 1)

# background color
# win.config(bg= "red")

win['bg'] = "yellow"

# main loop
win.mainloop()