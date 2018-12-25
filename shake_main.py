#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
shake_main.py
===========
Programme qui adapte au format epub3 les fichiers générés par la plateforme Publiwide 
Ce programme initialise quelques variables et lance la fonction new_job de la classe fet_class.py
fichiers : shake_main.py, shake_lib.py
auteur : josmet
date : 26.12.2018

modifications :
VERSION 0.00a - initialisation du projet shake

"""

VERSION_FILE = "shake_main.py"
VERSION_NO = "0.00a"
VERSION_DATE = "26.12.2018"
VERSION_AUTEUR = "Joseph Métrailler"
VERSION_DESCRIPTION = "Initialisation du projet"

# external libraries
# from shutil import copyfile
import tkinter as tk
import time
from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk

# this programm files
from shake_lib import ShakeLib


def clean_quit(window_2_close):
    print("bye from QUIT button")
    window_2_close.destroy()
    sys.exit(0)

def file_job_go():
    x.file_job()

# declare the display
msgDisplay = tk.Tk()
# fix the dimensions of the application window
WIN_WIDTH = 500
# WIN_WIDTH = 800
WIN_HEIGHT = 500
TOOL_BAR_HEIGHT = 80
# Get screen width and height
screenWidth = msgDisplay.winfo_screenwidth()  # width of the screen
screenHeight = msgDisplay.winfo_screenheight()  # height of the screen
# Calculate the smaller dimention between screen and application
maxWidth = min(WIN_WIDTH, screenWidth)
maxHeight = min(WIN_HEIGHT, screenHeight - TOOL_BAR_HEIGHT)
# open the application window in the center horizontaly and to the top verticaly
winPosX = (screenWidth / 2) - (int(maxWidth / 2))
winPosY = (screenHeight / 2) - (int(maxHeight / 2)) - int(TOOL_BAR_HEIGHT / 2)
# fix the geometry os the formular
msgDisplay.geometry('%dx%d+%d+%d' % (maxWidth, maxHeight, winPosX, winPosY))
msgDisplay.title("".join(["FET epub optimizer version : ", VERSION_NO, " - ", VERSION_DATE, " - ", VERSION_DESCRIPTION]))
img_tmp="logo_fet.png"
img=ImageTk.PhotoImage(Image.open(img_tmp))
msgDisplay.call('wm','iconphoto',msgDisplay,img)


# create a frame in the display formular
# lblHead = tk.Label(msgDisplay, text="Welcome in fet_epub app", fg='black', font='"Segoe UI" 9 italic').pack(anchor=W, ipadx=1, ipady=2)
# print (tkFont.Font(font='TkDefaultFont').configure())
# create a frame in the display formular

msgFrame = tk.Frame(msgDisplay)
msgFrame.pack(fill=tk.Y, expand=1)
# add listBox and scrollbar for it
varMsg = StringVar()
msgList = tk.Listbox(msgFrame)
msgList.config(width=maxWidth)
msgSbar = tk.Scrollbar(msgFrame)
msgSbar.config(command=msgList.yview)
msgList.config(yscrollcommand=msgSbar.set)
msgSbar.pack(side=tk.RIGHT, fill=tk.Y)
msgList.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# prepare the formular to be displayed
btnFrame = tk.Frame(msgDisplay)
btnFrame.pack(side=tk.BOTTOM)

# btnTest = tk.Button(btnFrame, text="Test soft", textvariable="btnTest", command=lambda: test_soft_go(),
#                     bg="coral").grid(row=0, column=2, ipadx=15, padx=2, pady=5)

#btnDirJob = tk.Button(btnFrame, text="Improve dir", textvariable="btnDirJob", command=lambda: dir_job_go(),
#                      bg="wheat3").grid(row=0, column=3, ipadx=15, padx=2, pady=5)
btnFileJob = tk.Button(btnFrame, text="Improve file", textvariable="btnFileJob", command=lambda: file_job_go(),
                       bg="wheat3").grid(row=0, column=4, ipadx=15, padx=2, pady=5)
#btnVerif = tk.Button(btnFrame, text="Verify file", textvariable="btnVerif", command=lambda: verify_job_go(),
#                     bg="wheat1").grid(row=0, column=5, ipadx=15, padx=2, pady=5)
btnQuit = tk.Button(btnFrame, text="QUIT", textvariable="btnQuit", command=lambda: clean_quit(msgDisplay),
                    bg="light blue").grid(row=0, column=6, ipadx=15, padx=2, pady=5)

# btnEssais = tk.Button(btnFrame, text="PRG essais", textvariable="btnEssais", command=lambda: prg_essais(),
#                     bg="cyan").grid(row=0, column=7, ipadx=15, padx=2, pady=15)

y = ShakeLib()
# display the formular and wait until somebody push a button
x.manage_info("To start click on a button", 1, 1)


msgDisplay.mainloop()

# Quit pressed, bye bye
print("... bye ...")
sys.exit(0)
