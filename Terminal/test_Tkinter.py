import datetime
import tkinter as tk

def actualisation():
    maintenant = datetime.datetime.now()
    heure = maintenant.strftime("%H:%M:%S")
    ETQ.configure(text=heure)
    FEN.after(1000, actualisation)
    
ma_variable  = tk.IntVar()
ROOT = tk.Tk()
ROOT.withdraw()

FEN = tk.Toplevel(ROOT)

ETQ = tk.Label(FEN,
               background="yellow",
               foreground="black",
               variable = ma_variable
               )

ECG = tk.Scale(FEN,
               orient= "horizontal",
               from_=0, to= 255,
               
               )

BTN = tk.Button(FEN,
                text = "Quitter",
                command= quit,
                relief="sunken")

ETQ.pack(side = "left")
BTN.pack()
ECG.pack()
actualisation()

ROOT.mainloop()