import tkinter as tk
from random import randint as ra
import time as t

v = tk.Tk()
v.withdraw()
v.title("Close Me!")

texts = []
start = False

k = None

def rh():
    return '#{:02x}{:02x}{:02x}'.format(ra(0, 255), ra(0, 255), ra(0, 255))

def c():
    s = ""
    for i in range(10):
        s += chr(ra(0, 2250))

    return s

def e(event):
    global k
    if k == '6':
        if event.keysym == "9":
            v.destroy()

    k = event.keysym

def w():
    for i in range(101): 
        r = tk.Toplevel(v)
        r.overrideredirect()
        x = ra(0, 1080)
        y = ra(0, 720)
        r.geometry(f"250x200+{x}+{y}")
        col = rh()
        r["bg"] = col
        t = tk.Label(r, text="Test", bg=col)
        t.place(relx=.5, rely=.5, anchor=tk.CENTER)
        texts.append(t)
        r.protocol("WM_DELETE_WINDOW", w)
        r.bind("<KeyPress>", e)
        
def f():
    for i in texts:
        for a in range(10):
            i["text"] = c()

    v.after(500, f)

w()
f()
