import keyboard
from tkinter import Tk, Toplevel, Label, TOP, Button, mainloop


def get_cursor_location(window: Tk) -> (int, int):
    x = window.winfo_pointerx() - window.winfo_rootx()
    y = window.winfo_pointery() - window.winfo_rooty()
    return x,y



history = []
MAXIMUM_SIZE = 25
WINDOW_WIDTH=250
WINDOW_HEIGHT=250
window = Tk()

def paste():
    print("Paste pressed")

while True:  # making a loop

    if keyboard.is_pressed("ctrl"):
        if keyboard.is_pressed("c"):
            a = Tk()
            clipboard = a.clipboard_get()
            a.destroy()
            if clipboard not in history:
                history.append(clipboard)
                if len(history) > MAXIMUM_SIZE:
                    history.pop(0)
        elif keyboard.is_pressed("shift") and keyboard.is_pressed("v"):
            window = Tk()
            window.bind("<ButtonPress-1>", window.destroy)
            cursor_x, cursor_y = get_cursor_location(window)
            window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{cursor_x}+{cursor_y-WINDOW_HEIGHT}')
            for row, text in enumerate(history):
                lab = Button(window, text=text, width=WINDOW_WIDTH, command=paste)
                lab.grid(row=row)
            mainloop()
