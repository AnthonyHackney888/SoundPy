import os
import tkinter as tk
from tkinter import Button, Label, filedialog,messagebox
from tkinter.constants import LEFT, TOP
from pydub import AudioSegment



def warning_for_init():
    msg = messagebox.askquestion("WAV to MP3", "No inital directory has been chosen", icon = "warning")
    if msg =='yes':
        init_directory()
    else:
        messagebox.showinfo("Continue","The files will not be convereted")
        exit()


def warning_for_dst():
    msg = messagebox.askquestion("WAV to MP3", "No destination directory has been chosen", icon = "warning")
    if msg =='yes':
        dest_directory()
    else:
        messagebox.showinfo("Continue","The files will not be convereted")
        exit()

def finished_window():
    msg = messagebox.showinfo(title="Music Converter", message="Music converted")
    exit()
'''
The initial directory selection
to batch convert
return: path for directory to convert
'''
def init_directory():
    #add if statment to handle empty destination
    path = filedialog.askdirectory()
    
    if path == '':
        #No init file path selected
        warning_for_init()
    else:
        return path
   

'''
The destination directory selection
to batch convert
return: path 
'''
def dest_directory():
    #add if statment to handle empty destination
    path = filedialog.askdirectory()
    
    if path == '':
        #No init file path selected
        warning_for_dst()
    else:
        return path
  

    

'''
Runs Batch conversions for wav to mp3
'''
def conversion_to_wav():
    dir = init_directory()
    #inital directory to convert MP3 to WAV
    dst = dest_directory()
    #Destination of converted MP3s
    

    audio=os.listdir(dir)
    for filename in audio:
        wavName = filename.replace(".mp3","")
        try:
            sound = AudioSegment.from_file("{}/{}".format(dir,filename))
            if "{}/{}.wav" not in audio:
                sound.export("{}/{}.wav".format(dst,wavName),format="wav")
        except Exception as e:
            pass
    finished_window() 


'''
Runs Batch conversions for mp3 to wav
'''
def conversion_to_mp3():

    dir = init_directory()
    dst = dest_directory()
    
    audio=os.listdir(dir)
    for filename in audio:
        wavName = filename.replace(".wav","")
        try:
            sound = AudioSegment.from_file("{}/{}".format(dir,filename))
            #if statment to check for duplicate file
            if "{}/{}.mp3" not in audio:
                sound.export("{}/{}.mp3".format(dst,wavName),format="mp3")
        except Exception as e:
            pass
    #notification for when process is completed
    finished_window() 


def check_input_mp3():
    msg = messagebox.askquestion("WAV to MP3", "Are you sure you want to convert? Your WAVs will not be deleted", icon = "warning")
    if msg =='yes':
        conversion_to_mp3()
    else:
        messagebox.showinfo("Continue","The files will not be convereted")


def check_input_wav():
    msg = messagebox.askquestion("MP3 to WAV", "Are you sure you want to convert? Your MP3s will not be deleted", icon = "warning")
    if msg =='yes':
        conversion_to_wav()
    else:
        messagebox.showinfo("Continue","The files will not be convereted")



def converter_window():
    root = tk.Tk()
    root.geometry('240x110')
    root.title("Music Converter")
    message = "What would you like to convert your files to?"
    Label(root, text=message).pack(side=TOP,pady = 10)


    wav_button = Button(root, text="wav",width = 10,height = 2,command=check_input_wav)
    mp3_button = Button(root, text="mp3",width = 10,height = 2,command=check_input_mp3)
    exit_button = Button(root, text="exit",width = 10,height = 2,command=exit)

    wav_button.pack(side=LEFT)
    mp3_button.pack(side=LEFT)
    exit_button.pack(side=LEFT)

    #resizing not needed
    root.resizable(0,0)
    root.mainloop()

def main():
    converter_window()


if __name__ =="__main__":
    main()