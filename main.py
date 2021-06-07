from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os, sys
import re
root = Tk()
root.title("Конвертер плейлистов.")
root.geometry('300x200+600+400')

def openFile():
    open_file_name = fd.askopenfilename(defaultextension=".txt",
                                        initialdir=os.getcwd(),
                                        title="Please select a file",
                                        filetypes=(("Playlist", "*.m3u8"),
                                                   ("Playlist", "*.m3u"),
                                                   ("All files", "*.*")))

    f = open(open_file_name,'r',encoding='utf-8' )       # Открывает файл для чтения



    file_name = fd.asksaveasfilename(defaultextension=".txt", filetypes=(("Playlist", "*.m3u"),
                                                                         ("Playlist", "*.m3u8"),
                                                                         ("All files", "*.*")))

    sf = open(file_name, 'w', encoding='utf-8')  # Открывает на запись файл для сохранения результат

    with f as f:
        for line in f:

            if line.find("#EXTM3U", 0, 7) == 0:
                sf.write(line)

            if line.find("#EXTINF", 0, 7) == 0:
                if line.find("#EXTINF:-1 group", 0, 16) == 0:
                    sf.write(line)
                else:
                    n = line

            if line.find("#EXTGRP", 0, 7) == 0:
                m = line[8:]
                m = m.rstrip()
                sf.write('#EXTINF:-1 group-title="'+ m +'",' +n[10:])

            if line.find("http", 0, 7) == 0:
                sf.write(line)



    f.close()                           # Закрывается файл
    print("Готово")


openFile()
root.mainloop()






