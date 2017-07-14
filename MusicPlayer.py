#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/17 20:13
# @Author  : GerryDeng
# @File    : MusicPlayer.py
# @Software: PyCharm

import tkinter as tk
from tkinter import filedialog
from win32com.client import Dispatch


class Window:
    def __init__(self):
        self.root = root = tk.Tk()
        button_add = tk.Button(root, text='Add', command=self.add)
        button_add.place(x=150, y=15)
        button_play = tk.Button(root, text='Play', command=self.play)
        button_play.place(x=200, y=15)
        button_pause = tk.Button(root, text='Pause', command=self.pause)
        button_pause.place(x=250, y=15)
        button_stop = tk.Button(root, text='Stop', command=self.stop)
        button_stop.place(x=300, y=15)
        button_next = tk.Button(root, text='Next', command=self.next)
        button_next.place(x=350, y=15)
        frame = tk.Frame(root, bd=2)
        self.playList = tk.Text(frame)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.config(command=self.playList.yview())
        self.playList.pack(side=tk.LEFT)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        frame.place(y=50)
        self.wmp = Dispatch('WMPlayer.OCX')

    def main_loop(self):
        self.root.minsize(510, 380)
        self.root.maxsize(510, 380)
        self.root.mainloop()

    def add(self):
        file = filedialog.askopenfilenames(title="Python Music Player",
                                            filetypes=[('MP3', '*.mp3'),
                                                    ('WMA', '*.wma'),
                                                    ('WAV', '*.wav')])
        if file:
            media = self.wmp.newMedia(file)
            self.wmp.currentPlaylist.appedItem(media)
            self.playList.insert(tk.END, file + '\n')

    def play(self):
        self.wmp.controls.play()

    def pause(self):
        self.wmp.controls.pause()

    def next(self):
        self.wmp.controls.next()

    def stop(self):
        self.wmp.controls.stop()


window = Window()
window.main_loop()
