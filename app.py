from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD, ITALIC
from pytube import YouTube

window = tk.Tk()
window.title("YouTube Downloader")
#window.iconbitmap("icona_yt.ico")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='icona_yt.png'))
window.geometry("800x600")
window.config(bg="#ffd0bf")

def download_video():
    if yt_video.get() == "":
        print("Inserire prima un URL valido")
    else:
        video_search()
        download_button.config(state=tk.DISABLED)
        yt_video.config(state=tk.DISABLED)
        download_dir = filedialog.askdirectory(title="Seleziona la cartella di destinazione")
        yt = YouTube(yt_video.get())
        video = yt.streams.get_highest_resolution()
        video.download(output_path=download_dir)
        download_button.config(state=tk.ACTIVE)
        yt_video.config(state=tk.ACTIVE)

def video_search():
    if yt_video.get() == "":
        print("Inserire prima un URL valido")
    else:
        yt = YouTube(yt_video.get())
        video = yt.streams.get_highest_resolution()

        video_label = tk.Label(window, text=yt.title, font = ("Arial", 10, BOLD), bg="#ffd0bf", fg="red")
        video_label.grid(row=6, column=0, pady=20)
    
        video_description = tk.Label(window, text=yt.description, justify=LEFT, wraplength=500, font = ("Arial", 8, ITALIC), bg="#ffd0bf", fg="black")
        video_description.grid(row=8, column=0)

        video_info = tk.Label(window, text="Durata: "+str(yt.length)+" secondi; Visualizzazioni: "+str(yt.views), justify=LEFT, wraplength=500, font = ("Arial", 8, BOLD), bg="#ffd0bf", fg="black")
        video_info.grid(row=7, column=0, pady=10)

logo_youtube = PhotoImage(file="icona_yt.png")
title_label = tk.Label(window, image=logo_youtube, font=("Arial",20, BOLD), bg="#ffd0bf", fg = "red")
title_label_text = tk.Label(window, text="Downlader", font=("Arial",20, BOLD), bg="#ffd0bf", fg = "red")

title_label.grid(row=1, column=0, pady=5)
title_label_text.grid(row=2, column=0, pady=5)

instruction_label = tk.Label(window, text="Inserisci URL del video da scaricare:", font =("Arial", 12, ITALIC), bg="#ffd0bf", fg="black")
instruction_label.grid(row=3, column=0)

yt_video = tk.Entry(window, bd=3, width=80)
yt_video.grid(row=4, column=0, padx=5)

search_icon = PhotoImage(file="lente.png")
search_button = tk.Button(window, image=search_icon, width=20, height=20, font="Arial", bd=3, bg="red", fg="white", command = video_search)
search_button.grid(row=4, column = 1, pady=20)

savefile = PhotoImage(file="savefile.png")
download_button = tk.Button(window, image=savefile, width=20, height=20, font="Arial", bd=3, bg="red", fg="white", command = download_video)
download_button.grid(row=4, column = 2, pady=20)

window.mainloop()