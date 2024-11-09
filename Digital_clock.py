import tkinter as tk

from time import strftime

root =  tk.Tk()
root.title('Digital_Clock')

def time():
    string =  strftime('%H:%M:%S \n %D')
    label.config(text = string)
    label.after(1000,time)

label =  tk.Label(root, font= ('calibri', 30, 'bold'), background = 'blue', foreground = 'black')
label.pack(anchor = 'center')

time()
root.mainloop()