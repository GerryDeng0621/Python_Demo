#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/17 20:13
# @Author  : GerryDeng
# @Site    :
# @File    : MusicPlayer.py
# @Software: PyCharm

import tkinter as tk
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)
print(sys.getdefaultencoding())

root = tk.Tk()
tk.Label(root, text="hello world").pack()
var = tk.StringVar(value="Hi")
text_input = tk.Entry(root, textvariable=var)
text_input.pack()

def print_content():
	print(var.get())
	var.set('')
tk.Button(root, text="print", command=print_content).pack()
tk.Button(root, text="Quit", command=root.destroy).pack()

root.bind('<Return>', lambda event:print_content())

text_output = tk.Message(root, textvariable=var)
text_output.pack()

root.mainloop()

