import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('demo')
window.geometry('300x150')

# Title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold' )
title_label.pack()

#

# run
window.mainloop()