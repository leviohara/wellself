import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import time

# Main Colors
lightscara = "#C8BBD7"
darkscara = "#282552"
whitescara = "#D9D9D9"

# Home Window + Config
main_window = tk.Tk()
main_window.configure(bg=lightscara)

main_window.title("Wellself")
main_window.geometry("700x800")

# Frame Header
header_frame = tk.Frame(main_window, bg=darkscara, height=100)
header_frame.pack(fill="x", pady=10)

header_label = tk.Label(header_frame, font=("Arial", 18, "bold"), fg="white", bg=darkscara)
header_label.pack(side="left", padx=10)

# Style
style = ttk.Style()
style.configure("RoundButton.TButton", foreground="black", background="white", borderwidth=0, focusthickness=0, highlightthickness=0)
style.map("RoundButton.TButton", background=[("active", "gray")])
style.configure("RoundButton.TButton", padding=(0, 0), width=0, height=100)

# IMG
image = Image.open("scara.jpg")
image = image.resize((90, 90))
photoimg = ImageTk.PhotoImage(image)

# Def functions
def profile_open():
    main_window.destroy()
    profile_page = tk.Tk()
    profile_page.title("Profile")
    profile_page.geometry("700x800")
    profile_page.configure(bg=lightscara)

    # Style
    style = ttk.Style()
    style.configure("RoundButton.TButton", foreground="black", background="white", borderwidth=0, focusthickness=0, highlightthickness=0)
    style.map("RoundButton.TButton", background=[("active", "gray")])
    style.configure("RoundButton.TButton", padding=(0, 0), width=0, height=100)

    # Frame Header
    header_frame = tk.Frame(profile_page, bg=darkscara, height=100)
    header_frame.pack(fill="x", pady=10)

    header_label = tk.Label(header_frame, font=("Arial", 18, "bold"), fg="white", bg=darkscara)
    header_label.pack(side="left", padx=10)
    text_var = tk.Label(header_frame, fg="white", bg=darkscara)
    text_var.pack()

    # Button Frame
    button_frame = tk.Frame(header_frame, bg=darkscara)
    button_frame.pack(fill="x", pady=10)

    # IMG
    image = Image.open("scara.jpg")
    image = image.resize((90, 90))
    photoimg = ImageTk.PhotoImage(image)

    # Icon to change
    profile_button = ttk.Button(button_frame, image=photoimg, style="RoundButton.TButton", compound="left")
    profile_button.image = photoimg
    profile_button.pack(side="left", anchor="nw", pady=0, padx=(0, 10))

    profile_page.mainloop()

# Button Frame
button_frame = tk.Frame(header_frame, bg=darkscara)
button_frame.pack(fill="x", pady=10)

# Icon to profile
profile_button = ttk.Button(button_frame, image=photoimg, style="RoundButton.TButton", compound="left", command=profile_open)
profile_button.image = photoimg
profile_button.pack(side="left", anchor="nw", pady=0, padx=(0, 10))

# Frame for grid
grid_frame = tk.Frame(main_window)
grid_frame.rowconfigure(5, weight=1)  
grid_frame.columnconfigure(2, weight=1)
grid_frame.pack(fill="both", expand=True)

# Clock Config
def update_time():
    current_time = time.strftime("%H:%M")
    clock_label.config(text=current_time)
    main_window.after(1000, update_time)

clock_label = tk.Label(grid_frame, font=('Helvetica', 24), fg=darkscara, bg=lightscara)
clock_label.place(x=-5, y=0, anchor="ne")
clock_label.pack()


update_time()

main_window.mainloop()