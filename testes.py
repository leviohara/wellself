import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

menuicon = Image.open("iconsmenu.png")
menuicon.putalpha(255)
print(menuicon.getalpha())