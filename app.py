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

#Funzione che scarica i Video completi
def download_video():
    if yt_video.get() == "":
        print("Inserire prima un URL valido")
    else:
        video_search()
        download_button.config(state=tk.DISABLED)
        yt_video.config(state=tk.DISABLED)
        audiosave_button.config(state=tk.DISABLED)
        download_dir = filedialog.askdirectory(title="Seleziona la cartella di destinazione")
        yt = YouTube(yt_video.get())
        video = yt.streams.get_highest_resolution()
        video.download(output_path=download_dir)
        download_button.config(state=tk.ACTIVE)
        yt_video.config(state=tk.ACTIVE)
        audiosave_button.config(state=tk.ACTIVE)

#Funzione che ricerca su YouTube il video richiesto e fornisce tutti i dettagli (titolo, descrizione e lunghezza video)
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

#Funzione per scaricare l'audio dai video. Il formato scelto è Mp4
def download_audio():
    if yt_video.get() == "":
        print("Inserire prima un URL valido")
    else:
        video_search()
        download_button.config(state=tk.DISABLED)
        yt_video.config(state=tk.DISABLED)
        audiosave_button.config(state=tk.DISABLED)
        download_dir = filedialog.askdirectory(title="Seleziona la cartella di destinazione")
        yt = YouTube(yt_video.get())
        audio = yt.streams.get_by_itag(140)
        audio.download(output_path=download_dir)
        download_button.config(state=tk.ACTIVE)
        yt_video.config(state=tk.ACTIVE)
        audiosave_button.config(state=tk.AACTIVE)

#Imposto l'app
# in alto, il logo di YouTUbe, con la scritta "Downloader" sotto di esso  
logo_youtube = PhotoImage(file="icona_yt.png")
title_label = tk.Label(window, image=logo_youtube, font=("Arial",20, BOLD), bg="#ffd0bf", fg = "red")
title_label_text = tk.Label(window, text="Downlader", font=("Arial",20, BOLD), bg="#ffd0bf", fg = "red")
title_label.grid(row=1, column=0, pady=5)
title_label_text.grid(row=2, column=0, pady=5)

#Sotto il titolo dell'app, la nostra "call to action"
instruction_label = tk.Label(window, text="Inserisci URL del video da scaricare:", font =("Arial", 12, ITALIC), bg="#ffd0bf", fg="black")
instruction_label.grid(row=3, column=0)

#La barra di testo in cui inserire l'URL del video di YouTube
yt_video = tk.Entry(window, bd=3, width=80)
yt_video.grid(row=4, column=0, padx=5)

#I tre pulsanti d'azione:
#Ricerca
search_icon = PhotoImage(file="lente.png")
search_button = tk.Button(window, image=search_icon, width=20, height=20, bd=3, bg="red", command = video_search)
search_button.grid(row=4, column = 1, pady=20)

#Salva video
savefile = PhotoImage(file="savefile.png")
download_button = tk.Button(window, image=savefile, width=20, height=20, bd=3, bg="red", command = download_video)
download_button.grid(row=4, column = 2, pady=20)

#Salva audio
audiosave = PhotoImage(file="audiosave.png")
audiosave_button = tk.Button(window, image=audiosave, width=20, height=20, bd=3, bg="red", command= download_audio)
audiosave_button.grid(row=4, column=3, pady=20)

window.mainloop()
