import os
import tkinter as tk
from tkinter import Button, Label, Toplevel, filedialog
from tkinter import messagebox
from pydub import AudioSegment

root = tk.Tk()
root.withdraw()


def basic_convert_wav():
    filename = filedialog.askopenfilename(parent = root, title="choose a file")
    replace_filename = filename.replace("mp3","wav")
    MP3_sound = AudioSegment.from_file(filename)
    MP3_sound.export(replace_filename, format="wav")

def basic_convert_mp3():
    filename = filedialog.askopenfilename(parent = root, title="choose a file")
    replace_filename = filename.replace("mp3","wav")
    WAV_sound = AudioSegment.from_file(filename)
    WAV_sound.export(replace_filename,format="mp3")

def check_input_mp3():
    msg = messagebox.askquestion("WAV to MP3", "Are you sure you want to convert? Your WAVs will not be deleted", icon = "warning")
    if msg =='yes':
       basic_convert_mp3()
    else:
        messagebox.showinfo("Continue","The files will not be convereted")

def check_input_wav():
    msg = messagebox.askquestion("MP3 to WAV", "Are you sure you want to convert? Your MP3s will not be deleted", icon = "warning")
    if msg =='yes':
        basic_convert_wav()
    else:
        messagebox.showinfo("Continue","The files will not be convereted")


def converter_window():
    win = Toplevel()
    win.title("Converter")
    message = "What would you like to convert your files to?"
    Label(win, text=message).pack()

    
    wav_button = Button(win, text="wav",command=check_input_wav).pack()
    mp3_button = Button(win, text="mp3",command=check_input_mp3).pack()
    exit_button = Button(win, text="exit",command=exit).pack()
    root.mainloop()


def main():
    converter_window()


if __name__ =="__main__":
    main()