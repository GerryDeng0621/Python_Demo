#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/17 21:13
# @Author  : GerryDeng
# @File    : entry.py
# @Software: PyCharm

import tkinter as tk
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())
root = tk.Tk()
app = App(master=root)
app.mainloop()
