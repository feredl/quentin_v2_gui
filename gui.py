import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from quentin import Quentin
import re
from tkinter.filedialog import askopenfilename

#commands
def ask_file():
    path.set(value=askopenfilename())
    filename = path.get().split('/')[len(path.get().split('/'))-1]
    name.set(f"Chosen file: " + filename)

def quentin_classification():
    try:
        bool(re.search(".xlsx|.xls", path.get())) is True
        classification = Quentin(path.get(), skip_zeros.get())
        classification.show_stemma()
    except:
        messagebox.showerror(title="Error", message="Wrong file format or content!")

#WINDOW
main_window = tk.Tk()
main_window.geometry("450x275")
main_window.title("Quentin Stemma")

title = ttk.Label(main_window, 
                  text = "Quentin's method of textual criticism", 
                  background="white", font=("Verdana", 12))
title.pack(padx=10, pady=10)

path = tk.StringVar()
name = tk.StringVar()
skip_zeros = tk.IntVar()

frame = ttk.Frame(borderwidth=1)

frame_choose_file = ttk.Frame(master=frame, borderwidth=1)
ask_path = ttk.Button(master = frame, text="Browse...", 
                      command=ask_file)

path_label = ttk.Label(master = frame, text="1. Choose excel file.", 
                       font=("Verdana", 10))

path_label.pack(padx=5, pady=5, anchor=tk.NW)
ask_path.pack(padx=5, pady=5)

name_label = ttk.Label(master = frame,
                        textvariable=name)
name_label.pack(padx=5, pady=5)

frame_choose_file.pack(padx=5, pady=5, fill=tk.X, anchor=tk.NW)

skip_label = ttk.Label(master = frame,
                        text="2. Decide if you need to skip variants with empty readings.", 
                        font=("Verdana", 10))
skip_label.pack(padx=5, pady=5, anchor=tk.NW)
skip_zeros_checkbutton = ttk.Checkbutton(master = frame, text="Skip columns with zeros", 
                                         variable=skip_zeros)
skip_zeros_checkbutton.pack(padx=5, pady=10)      

frame.pack(padx=5, pady=5, fill=tk.X, anchor=tk.NW)
      
start_button = ttk.Button(text="Start", 
                          command=quentin_classification)
start_button.pack(padx=2, pady=5)

main_window.configure(background='white')
main_window.mainloop()