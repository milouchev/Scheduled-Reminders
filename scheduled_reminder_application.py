#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:00:58 2022

@author: milouchev
"""

import tkinter as ui
import datetime

reminder = input("Enter your reminder message: ")
when = input("Enter a time in the format HH:MM (24-hour format): ")
hour, min = [int(i) for i in when.split(":")]

window = ui.Tk()
window.title("Reminder - " + str(when))
# This makes the pop-up window actually pop-up in front of other windows. Compatible with Mac.
window.attributes('-topmost', True)

def reminder_window():
    reminder_text = "\n"+" "+reminder+" "+"\n"
    reminder_label.config(text=reminder_text)
    
reminder_label = ui.Label(window, font="Garamond 72 bold")
reminder_label.pack()
  
while True:  
    if hour == datetime.datetime.now().hour and min == datetime.datetime.now().minute:
        reminder_window()
        window.mainloop()
        break
    