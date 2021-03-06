import tkinter as tk
import speech_to_text as spt

# Setup variables
type_text_setting = spt.get_setting("type_text")
if type_text_setting:
    type_text_value = "on"
else:
    type_text_value = "off"

repeat_setting = spt.get_setting("repeat")
if repeat_setting:
    repeat_value = "on"
else:
    repeat_value = "off"

# Window setup
window = tk.Tk()
window.geometry("500x500")
window.title("Speech to Text")
window.configure(bg="#121212")
window.resizable(False, False)

# Icon setup
icon = """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"""
img = tk.PhotoImage(data=icon)
window.tk.call('wm', 'iconphoto', window._w, img)

# Setup frame
frame = tk.Frame(window, bg="#121212")
frame.place(relx=0.5, anchor=tk.CENTER, rely=0.17)

# Setup settings frame
options_frame = tk.Frame(window, bg="#121212")
options_frame.place(relx=0.5, anchor=tk.CENTER, rely=0.42)


# Definition setups
def start_spt(event):
    if not spt.running:
        recent_text_label.configure(text="Speech to text is running")
        window.title("Speech to Text - Running")
        spt.start()


def stop_spt(event):
    if spt.running:
        recent_text_label.configure(text="Speech to text is offline")
        window.title("Speech to Text")
        spt.stop()


def update_text(text):
    recent_text_label.configure(text=text)


def type_text_option(event):
    global type_text_setting
    type_text_setting = spt.get_setting("type_text")
    if type_text_setting:
        spt.save_setting("type_text", False)
        type_text_button.configure(text="Type text: off")
    else:
        spt.save_setting("type_text", True)
        type_text_button.configure(text="Type text: on")


def repeat_option(event):
    global repeat_setting
    repeat_setting = spt.get_setting("repeat")
    if repeat_setting:
        spt.save_setting("repeat", False)
        repeat_button.configure(text="Repeat: off")
    else:
        spt.save_setting("repeat", True)
        repeat_button.configure(text="Repeat: on")


# Creating title
title = tk.Label(window, text="Speech to Text", font="roboto 24", fg="#ffffff", bg="#121212")
title.pack(pady=(5, 0))

# Creating recent text bar
recent_text_label = tk.Label(frame, text="Speech to text is offline", width=20, height=3, bg="#1c1c1c", fg="#BB86FC", font=("roboto", 13), borderwidth=1, wraplength=150)
recent_text_label.grid(column=2, row=2, rowspan=2, padx=(5, 0), pady=(11, 0))

# Button creation
start_button = tk.Button(frame, text="Press to start", width=15, height=1, bg="#1c1c1c", fg="#BB86FC", font=("roboto", 12), borderwidth=0, activeforeground="#BB86FC", activebackground="#212121")
stop_button = tk.Button(frame, text="Press to stop", width=15, bg="#1c1c1c", fg="#BB86FC", font=("roboto", 12), borderwidth=0, activeforeground="#BB86FC", activebackground="#212121")

start_button.bind("<Button-1>", start_spt)
stop_button.bind("<Button-1>", stop_spt)

start_button.grid(column=1, row=2, pady=(15, 6))
stop_button.grid(column=1, row=3, pady=(0, 5))

# Creating options title
title = tk.Label(window, text="Options", font="roboto 24", fg="#ffffff", bg="#121212")
title.pack(pady=(90, 0))

# Creating options buttons
type_text_button = tk.Button(options_frame, text="Type text: {}".format(type_text_value), width=15, height=1, bg="#1c1c1c", fg="#BB86FC", font=("roboto", 12), borderwidth=0, activeforeground="#BB86FC", activebackground="#212121")
repeat_button = tk.Button(options_frame, text="Repeat: {}".format(repeat_value), width=15, bg="#1c1c1c", fg="#BB86FC", font=("roboto", 12), borderwidth=0, activeforeground="#BB86FC", activebackground="#212121")

type_text_button.bind("<Button-1>", type_text_option)
repeat_button.bind("<Button-1>", repeat_option)

type_text_button.grid(column=1, row=2, padx=(0, 6))
repeat_button.grid(column=2, row=2)

window.mainloop()
