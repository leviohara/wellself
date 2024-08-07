import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import time
import math

# Main Colors
lightscara = "#C8BBD7"
darkscara = "#282552"
whitescara = "#D9D9D9"
lightnahida = "#E2F2A7"
darknahida = "#9FBF2A"

# Home Window + Config
main_window = tk.Tk()
main_window.configure(bg=lightscara)

main_window.title("Home")
main_window.geometry("700x800")

# Definir atributos da janela

# Definir tamanho mínimo
main_window.minsize(400, 300)  # largura x altura

# Definir tamanho máximo
main_window.maxsize(800, 600)  # largura x altura

# Impedir que o usuário altere o tamanho da tela
main_window.resizable(False, False) 

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

xicon = Image.open("iconsx.png")
xicon = xicon.resize((20, 20))
closeimg = ImageTk.PhotoImage(xicon)

menuicon = Image.open("iconsmenu.png")
menuicon = menuicon.resize((40, 40))
menuimg = ImageTk.PhotoImage(menuicon, master=main_window)
menuicon.putalpha(255)

# Keep a reference to the image
main_window.image = photoimg

# Def functions
def pattern_menu():
    xicon = Image.open("iconsx.png")
    xicon = xicon.resize((20, 20))
    closeimg = ImageTk.PhotoImage(xicon)
  
    menuicon = Image.open("iconsmenu.png")
    menuicon = menuicon.resize((40, 40))
    menuimg = ImageTk.PhotoImage(menuicon, master=main_window)
    menuicon.putalpha(255)
    # Menu Button
    button_menu = tk.Button(main_window, image=menuimg, relief="flat", bg=darkscara, highlightthickness=0, bd=0, command=open_menu)
    button_menu.pack(side="right")
    button_menu.place(x=650, y=20)

    # Menu options
    options = tk.Menu(main_window, tearoff=0)
    options.add_command(image=closeimg, command=hide_menu)
    options.add_separator()
    options.add_command(label="Configurações")
    options.add_command(label="Conta")
    options.add_command(label="Ajuda")
    options.add_command(label="Comunidade")
    options.config(bd=0, bg=lightnahida, fg=darknahida)

    return xicon, menuicon, button_menu, options

def profile_open():
    def back_btt():
        profile_page.withdraw()
        main_window.deiconify()

    main_window.withdraw()
    profile_page = tk.Toplevel(main_window)
    profile_page.title("Profile")
    profile_page.geometry("700x800")
    profile_page.configure(bg=lightscara)
    # Definir tamanho mínimo
    main_window.minsize(400, 300)

    # Definir tamanho máximo
    main_window.maxsize(800, 600)
    # Impedir que o usuário altere o tamanho da tela
    main_window.resizable(False, False) 

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
    button_frame = tk.Frame(header_frame, bg=darkscara, width=200, height=100)
    button_frame.pack(fill="none", expand=False, pady=0)

    # IMG PROFILE
    image = Image.open("scara.jpg")
    image = image.resize((90, 90))
    profile_photoimg = ImageTk.PhotoImage(image)

    # Keep a reference to the image
    profile_page.image = profile_photoimg

    # Icon to change
    profile_button = ttk.Button(button_frame, image=profile_photoimg, style="RoundButton.TButton")
    profile_button.image = profile_photoimg
    profile_button.place(relx=0.5, rely=0.5, anchor="center")

    btt_back = tk.Button(profile_page, command=back_btt, width=20, text="Voltar", bg=whitescara)
    btt_back.pack(side="left")
    profile_page.mainloop()

# DIARY PAGE CONFIG
def diary_open():
    def back_btt():
        diary_page.withdraw()
        main_window.deiconify()
    main_window.withdraw()
    diary_page = tk.Toplevel(main_window)
    diary_page.title("Diary")
    diary_page.geometry("700x800")
    diary_page.configure(bg=lightscara)
    # Definir tamanho mínimo
    main_window.minsize(400, 300)
    # Definir tamanho máximo
    main_window.maxsize(800, 600)
    # Impedir que o usuário altere o tamanho da tela
    main_window.resizable(False, False) 

        # Style
    style = ttk.Style()
    style.configure("RoundButton.TButton", foreground="black", background="white", borderwidth=0, focusthickness=0, highlightthickness=0)
    style.map("RoundButton.TButton", background=[("active", "gray")])
    style.configure("RoundButton.TButton", padding=(0, 0), width=0, height=100)

    # Frame Header
    header_frame = tk.Frame(diary_page, bg=darkscara, height=100)
    header_frame.pack(fill="x", pady=10)

    #FRAME MENU
    # menu_frame = tk.Frame(diary_page)
    # menu_frame.place(relx=1, rely=0, anchor="ne", width=100, height=100)

    # header_label = tk.Label(header_frame, font=("Arial", 18, "bold"), fg="white", bg=darkscara)
    # header_label.pack(side="left", padx=10)

    # IMG PROFILE
    image = Image.open("scara.jpg")
    image = image.resize((90, 90))
    diary_photoimg = ImageTk.PhotoImage(image)

    # Keep a reference to the image
    diary_page.image = diary_photoimg

    # Labels
    # label_title = tk.Label(font=("Arial", 18, "bold"), fg="white", bg=darkscara)
    # # main_label = 
    btt_back = tk.Button(diary_page, command=back_btt, width=20, text="Voltar", bg=whitescara, )
    btt_back.pack(side="left")

    # MENU PATTERN 
    xicon = Image.open("iconsx.png")
    xicon = xicon.resize((20, 20))
    closeimg = ImageTk.PhotoImage(xicon)
  
    menuicon = Image.open("iconsmenu.png")
    menuicon = menuicon.resize((40, 40))
    menuimg = ImageTk.PhotoImage(menuicon, master=main_window)
    menuicon.putalpha(255)

    # Menu Button
    button_menu = tk.Button(diary_page, image=menuimg, relief="flat", bg=darkscara, highlightthickness=0, bd=0, command=open_menu)
    button_menu.pack(side="right")
    button_menu.place(x=650, y=20)

    # Menu options
    options = tk.Menu(diary_page, tearoff=0)
    options.add_command(image=closeimg, command=hide_menu)
    options.add_separator()
    options.add_command(label="Configurações")
    options.add_command(label="Conta")
    options.add_command(label="Ajuda")
    options.add_command(label="Comunidade")
    options.config(bd=0, bg=lightnahida, fg=darknahida)

    diary_page.mainloop()


# DIARY BUTTON CONFIG
# def on_enter(e):
#     e.widget.config(relief="raised", font=("Arial", 15), bg=darkscara, fg='white')
# def on_leave(e):
#     e.widget.config(relief="flat", font=("Arial", 12))

def open_menu():
    options.post(main_window.winfo_x(), main_window.winfo_y())
    
def popup_menu(event):
    options.post(event.x, event.y)
def hide_menu():
    options.unpost()

# Button Frame
button_frame = tk.Frame(header_frame, bg=darkscara)
button_frame.pack(fill="x", pady=10)

# Icon to profile
profile_button = ttk.Button(button_frame, image=photoimg, style="RoundButton.TButton", compound="left", command=profile_open)
profile_button.image = photoimg
profile_button.pack(side="left", anchor="nw", pady=0, padx=(0, 10))


# Clock Config
def update_time():
    current_time = time.strftime("%H:%M")
    clock_label.config(text=current_time)
    main_window.after(1000, update_time)
class Clock(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, bd=0, highlightthickness=0)
        self.current_time = time.localtime()
        self.draw_lines()
        self.config(bg=lightscara)
    def draw_lines(self):
        hora = self.current_time.tm_hour
        min = self.current_time.tm_min
        if min == 0:
            self.current_time = time.localtime()
            hora = self.current_time.tm_hour % 12 + self.current_time.tm_min / 60
        self.create_oval(50, 50, 150, 150, fill=darkscara, outline='white', width=2)
        self.create_oval(99, 99, 101, 101, fill='white', outline='white') 
        self.create_line(100, 100, 100 + 50 * math.sin(math.radians(hora * 15)), 100 - 50 * math.cos(math.radians(hora * 15)), fill='white', width=2)
        self.after(60000, self.draw_lines)

clock_tool = Clock(main_window, width=200, height=200)
clock_tool.place(x=45, y=130)

clock_label = tk.Label(main_window, font=('Helvetica', 24), fg=darkscara, bg=lightscara)
clock_label.place(x=100, y= 300)

# Diary Section
diary_frame = tk.Frame(main_window, bg=lightscara, width=200, height=200)
diary_frame.place(x=400, y=160)
title_d= tk.Label(diary_frame, bg=darkscara, fg='white', text="Título", font=("Arial", 15))
title_d.pack(fill="x", padx=10, pady=20)
# Diary Button
btt_d= tk.Button(diary_frame, bg=lightscara, relief="flat", fg=darkscara, text="Comece a escrever...", borderwidth=0, highlightthickness=0, font=("Arial", 13), command=diary_open)
# btt_d.bind("<Enter>", on_enter)
# btt_d.bind("<Enter>", on_leave)
btt_d.pack(padx=10, pady=10)

# Menu Button
button_menu = tk.Button(main_window, image=menuimg, relief="flat", bg=darkscara, highlightthickness=0, bd=0, command=open_menu)
button_menu.pack(side="right")
button_menu.place(x=650, y=20)

# Menu options
options = tk.Menu(main_window, tearoff=0)
options.add_command(image=closeimg, command=hide_menu)
options.add_separator()
options.add_command(label="Configurações")
options.add_command(label="Conta")
options.add_command(label="Ajuda")
options.add_command(label="Comunidade")
options.config(bd=0, bg=lightnahida, fg=darknahida)


update_time()

main_window.mainloop()