#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 25, 2022 12:23:12 AM CEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

class Toplevel1:
    def __init__(self, kadala_support, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.parent = kadala_support
        self.parent.ui = self

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("649x520+517+178")
        top.minsize(120, 1)
        top.maxsize(7444, 1061)
        top.resizable(0,  0)
        top.title("Tiny Tina's Wonderlands - Kadala !")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.text_name = tk.StringVar()
        self.text_gold = tk.StringVar()
        self.text_price = tk.StringVar()
        self.label_gambled = tk.StringVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(x=10, y=10, height=500, width=360)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Labelframe3 = tk.LabelFrame(self.Frame1)
        self.Labelframe3.place(x=20, y=10, height=315, width=90)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Offhand''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.Button4 = tk.Button(self.Labelframe3)
        self.Button4.place(x=20, y=150, height=24, width=42, bordermode='ignore')

        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=kadala_support.select_offhand)
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(state='disabled')
        self.Button4.configure(text='''Select''')

        self.label_melee = tk.Label(self.Labelframe3)
        self.label_melee.place(x=5, y=17, height=21, width=34
                , bordermode='ignore')
        self.label_melee.configure(activebackground="#f9f9f9")
        self.label_melee.configure(activeforeground="black")
        self.label_melee.configure(anchor='w')
        self.label_melee.configure(background="#d9d9d9")
        self.label_melee.configure(compound='left')
        self.label_melee.configure(disabledforeground="#a3a3a3")
        self.label_melee.configure(foreground="#000000")
        self.label_melee.configure(highlightbackground="#d9d9d9")
        self.label_melee.configure(highlightcolor="black")
        self.label_melee.configure(text='''Label''')

        self.Labelframe4 = tk.LabelFrame(self.Frame1)
        self.Labelframe4.place(x=120, y=10, height=75, width=220)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='''Weapon 1''')
        self.Labelframe4.configure(background="#d9d9d9")
        self.Labelframe4.configure(highlightbackground="#d9d9d9")
        self.Labelframe4.configure(highlightcolor="black")

        self.Button4_1 = tk.Button(self.Labelframe4)
        self.Button4_1.place(x=90, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1.configure(activebackground="#ececec")
        self.Button4_1.configure(activeforeground="#000000")
        self.Button4_1.configure(background="#d9d9d9")
        self.Button4_1.configure(command=kadala_support.select_weapon_1)
        self.Button4_1.configure(compound='left')
        self.Button4_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1.configure(foreground="#000000")
        self.Button4_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1.configure(highlightcolor="black")
        self.Button4_1.configure(pady="0")
        self.Button4_1.configure(state='disabled')
        self.Button4_1.configure(text='''Select''')

        self.label_w1 = tk.Label(self.Labelframe4)
        self.label_w1.place(x=10, y=20, height=21, width=34, bordermode='ignore')

        self.label_w1.configure(activebackground="#f9f9f9")
        self.label_w1.configure(activeforeground="black")
        self.label_w1.configure(anchor='w')
        self.label_w1.configure(background="#d9d9d9")
        self.label_w1.configure(compound='left')
        self.label_w1.configure(disabledforeground="#a3a3a3")
        self.label_w1.configure(foreground="#000000")
        self.label_w1.configure(highlightbackground="#d9d9d9")
        self.label_w1.configure(highlightcolor="black")
        self.label_w1.configure(text='''Label''')

        self.Labelframe4_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1.place(x=120, y=90, height=75, width=220)
        self.Labelframe4_1.configure(relief='groove')
        self.Labelframe4_1.configure(foreground="black")
        self.Labelframe4_1.configure(text='''Weapon 2''')
        self.Labelframe4_1.configure(background="#d9d9d9")
        self.Labelframe4_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1.configure(highlightcolor="black")

        self.Button4_1_1 = tk.Button(self.Labelframe4_1)
        self.Button4_1_1.place(x=90, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1.configure(activebackground="#ececec")
        self.Button4_1_1.configure(activeforeground="#000000")
        self.Button4_1_1.configure(background="#d9d9d9")
        self.Button4_1_1.configure(command=kadala_support.select_weapon_2)
        self.Button4_1_1.configure(compound='left')
        self.Button4_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1.configure(foreground="#000000")
        self.Button4_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1.configure(highlightcolor="black")
        self.Button4_1_1.configure(pady="0")
        self.Button4_1_1.configure(state='disabled')
        self.Button4_1_1.configure(text='''Select''')

        self.label_w2 = tk.Label(self.Labelframe4_1)
        self.label_w2.place(x=5, y=17, height=21, width=34, bordermode='ignore')
        self.label_w2.configure(activebackground="#f9f9f9")
        self.label_w2.configure(activeforeground="black")
        self.label_w2.configure(anchor='w')
        self.label_w2.configure(background="#d9d9d9")
        self.label_w2.configure(compound='left')
        self.label_w2.configure(disabledforeground="#a3a3a3")
        self.label_w2.configure(foreground="#000000")
        self.label_w2.configure(highlightbackground="#d9d9d9")
        self.label_w2.configure(highlightcolor="black")
        self.label_w2.configure(text='''Label''')

        self.Labelframe4_1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1.place(x=120, y=170, height=75, width=220)
        self.Labelframe4_1_1.configure(relief='groove')
        self.Labelframe4_1_1.configure(foreground="black")
        self.Labelframe4_1_1.configure(text='''Weapon 3''')
        self.Labelframe4_1_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1.configure(highlightcolor="black")

        self.Button4_1_1_1 = tk.Button(self.Labelframe4_1_1)
        self.Button4_1_1_1.place(x=90, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1.configure(command=kadala_support.select_weapon_3)
        self.Button4_1_1_1.configure(compound='left')
        self.Button4_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1.configure(pady="0")
        self.Button4_1_1_1.configure(state='disabled')
        self.Button4_1_1_1.configure(text='''Select''')

        self.label_w3 = tk.Label(self.Labelframe4_1_1)
        self.label_w3.place(x=10, y=20, height=21, width=34, bordermode='ignore')

        self.label_w3.configure(activebackground="#f9f9f9")
        self.label_w3.configure(activeforeground="black")
        self.label_w3.configure(anchor='w')
        self.label_w3.configure(background="#d9d9d9")
        self.label_w3.configure(compound='left')
        self.label_w3.configure(disabledforeground="#a3a3a3")
        self.label_w3.configure(foreground="#000000")
        self.label_w3.configure(highlightbackground="#d9d9d9")
        self.label_w3.configure(highlightcolor="black")
        self.label_w3.configure(text='''Label''')

        self.Labelframe4_1_1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1.place(x=120, y=250, height=75, width=220)
        self.Labelframe4_1_1_1.configure(relief='groove')
        self.Labelframe4_1_1_1.configure(foreground="black")
        self.Labelframe4_1_1_1.configure(text='''Weapon 4''')
        self.Labelframe4_1_1_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1.configure(highlightcolor="black")

        self.Button4_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1)
        self.Button4_1_1_1_1.place(x=90, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1.configure(command=kadala_support.select_weapon_4)
        self.Button4_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1.configure(text='''Select''')

        self.label_w4 = tk.Label(self.Labelframe4_1_1_1)
        self.label_w4.place(x=5, y=17, height=21, width=34, bordermode='ignore')
        self.label_w4.configure(activebackground="#f9f9f9")
        self.label_w4.configure(activeforeground="black")
        self.label_w4.configure(anchor='w')
        self.label_w4.configure(background="#d9d9d9")
        self.label_w4.configure(compound='left')
        self.label_w4.configure(disabledforeground="#a3a3a3")
        self.label_w4.configure(foreground="#000000")
        self.label_w4.configure(highlightbackground="#d9d9d9")
        self.label_w4.configure(highlightcolor="black")
        self.label_w4.configure(text='''Label''')

        self.Labelframe4_1_1_1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1_1.place(x=20, y=330, height=75, width=100)
        self.Labelframe4_1_1_1_1.configure(relief='groove')
        self.Labelframe4_1_1_1_1.configure(foreground="black")
        self.Labelframe4_1_1_1_1.configure(text='''Ring 1''')
        self.Labelframe4_1_1_1_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1_1.configure(highlightcolor="black")

        self.Button4_1_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1_1)
        self.Button4_1_1_1_1_1.place(x=30, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1_1.configure(command=kadala_support.select_ring_1)
        self.Button4_1_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1_1.configure(text='''Select''')

        self.label_r1 = tk.Label(self.Labelframe4_1_1_1_1)
        self.label_r1.place(x=5, y=17, height=21, width=34, bordermode='ignore')
        self.label_r1.configure(activebackground="#f9f9f9")
        self.label_r1.configure(activeforeground="black")
        self.label_r1.configure(anchor='w')
        self.label_r1.configure(background="#d9d9d9")
        self.label_r1.configure(compound='left')
        self.label_r1.configure(disabledforeground="#a3a3a3")
        self.label_r1.configure(foreground="#000000")
        self.label_r1.configure(highlightbackground="#d9d9d9")
        self.label_r1.configure(highlightcolor="black")
        self.label_r1.configure(text='''Label''')

        self.Labelframe4_1_1_1_1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1_1_1.place(x=130, y=330, height=75, width=100)
        self.Labelframe4_1_1_1_1_1.configure(relief='groove')
        self.Labelframe4_1_1_1_1_1.configure(foreground="black")
        self.Labelframe4_1_1_1_1_1.configure(text='''Shield''')
        self.Labelframe4_1_1_1_1_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1_1_1.configure(highlightcolor="black")

        self.Button4_1_1_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1_1_1)
        self.Button4_1_1_1_1_1_1.place(x=30, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1_1_1.configure(command=kadala_support.select_shield)
        self.Button4_1_1_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1_1_1.configure(text='''Select''')

        self.label_shield = tk.Label(self.Labelframe4_1_1_1_1_1)
        self.label_shield.place(x=5, y=17, height=21, width=34
                , bordermode='ignore')
        self.label_shield.configure(anchor='w')
        self.label_shield.configure(background="#d9d9d9")
        self.label_shield.configure(compound='left')
        self.label_shield.configure(disabledforeground="#a3a3a3")
        self.label_shield.configure(foreground="#000000")
        self.label_shield.configure(text='''Label''')

        self.Labelframe4_1_1_1_1_1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1_1_1_1.place(x=240, y=330, height=75, width=100)
        self.Labelframe4_1_1_1_1_1_1.configure(relief='groove')
        self.Labelframe4_1_1_1_1_1_1.configure(foreground="black")
        self.Labelframe4_1_1_1_1_1_1.configure(text='''Amulet''')
        self.Labelframe4_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1_1_1_1.configure(highlightcolor="black")

        self.Button4_1_1_1_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1_1_1_1)
        self.Button4_1_1_1_1_1_1_1.place(x=30, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1.configure(command=kadala_support.select_amulet)
        self.Button4_1_1_1_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1_1_1_1.configure(text='''Select''')

        self.label_amulet = tk.Label(self.Labelframe4_1_1_1_1_1_1)
        self.label_amulet.place(x=5, y=17, height=21, width=34
                , bordermode='ignore')
        self.label_amulet.configure(anchor='w')
        self.label_amulet.configure(background="#d9d9d9")
        self.label_amulet.configure(compound='left')
        self.label_amulet.configure(disabledforeground="#a3a3a3")
        self.label_amulet.configure(foreground="#000000")
        self.label_amulet.configure(text='''Label''')

        self.Labelframe4_1_1_1_1_2 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1_1_2.place(x=20, y=410, height=75, width=100)
        self.Labelframe4_1_1_1_1_2.configure(relief='groove')
        self.Labelframe4_1_1_1_1_2.configure(foreground="black")
        self.Labelframe4_1_1_1_1_2.configure(text='''Ring 2''')
        self.Labelframe4_1_1_1_1_2.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1_1_2.configure(highlightcolor="black")

        self.Button4_1_1_1_1_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1_1_2)
        self.Button4_1_1_1_1_1_1_1_1.place(x=30, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1_1.configure(command=kadala_support.select_ring_2)
        self.Button4_1_1_1_1_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1_1_1_1_1.configure(text='''Select''')

        self.label_r2 = tk.Label(self.Labelframe4_1_1_1_1_2)
        self.label_r2.place(x=5, y=17, height=21, width=34, bordermode='ignore')
        self.label_r2.configure(activebackground="#f9f9f9")
        self.label_r2.configure(activeforeground="black")
        self.label_r2.configure(anchor='w')
        self.label_r2.configure(background="#d9d9d9")
        self.label_r2.configure(compound='left')
        self.label_r2.configure(disabledforeground="#a3a3a3")
        self.label_r2.configure(foreground="#000000")
        self.label_r2.configure(highlightbackground="#d9d9d9")
        self.label_r2.configure(highlightcolor="black")
        self.label_r2.configure(text='''Label''')

        self.Labelframe4_1_1_1_1_2_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1_1_2_1.place(x=130, y=410, height=75, width=100)
        self.Labelframe4_1_1_1_1_2_1.configure(relief='groove')
        self.Labelframe4_1_1_1_1_2_1.configure(foreground="black")
        self.Labelframe4_1_1_1_1_2_1.configure(text='''Mod''')
        self.Labelframe4_1_1_1_1_2_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1_1_2_1.configure(highlightcolor="black")

        self.Button4_1_1_1_1_1_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1_1_2_1)
        self.Button4_1_1_1_1_1_1_1_1_1.place(x=30, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(command=kadala_support.select_mod)
        self.Button4_1_1_1_1_1_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1_1_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1_1_1_1_1_1.configure(text='''Select''')

        self.label_mod = tk.Label(self.Labelframe4_1_1_1_1_2_1)
        self.label_mod.place(x=5, y=17, height=21, width=34, bordermode='ignore')

        self.label_mod.configure(anchor='w')
        self.label_mod.configure(background="#d9d9d9")
        self.label_mod.configure(compound='left')
        self.label_mod.configure(disabledforeground="#a3a3a3")
        self.label_mod.configure(foreground="#000000")
        self.label_mod.configure(text='''Label''')

        self.Labelframe4_1_1_1_1_2_1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe4_1_1_1_1_2_1_1.place(x=240, y=410, height=75, width=100)
        self.Labelframe4_1_1_1_1_2_1_1.configure(relief='groove')
        self.Labelframe4_1_1_1_1_2_1_1.configure(foreground="black")
        self.Labelframe4_1_1_1_1_2_1_1.configure(text='''Spell''')
        self.Labelframe4_1_1_1_1_2_1_1.configure(background="#d9d9d9")
        self.Labelframe4_1_1_1_1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_1_1_1_1_2_1_1.configure(highlightcolor="black")

        self.Button4_1_1_1_1_1_1_1_1_1_1 = tk.Button(self.Labelframe4_1_1_1_1_2_1_1)
        self.Button4_1_1_1_1_1_1_1_1_1_1.place(x=30, y=40, height=24, width=42
                , bordermode='ignore')
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(command=kadala_support.select_spell)
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(compound='left')
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(pady="0")
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(state='disabled')
        self.Button4_1_1_1_1_1_1_1_1_1_1.configure(text='''Select''')

        self.label_spell = tk.Label(self.Labelframe4_1_1_1_1_2_1_1)
        self.label_spell.place(x=5, y=17, height=21, width=34
                , bordermode='ignore')
        self.label_spell.configure(anchor='w')
        self.label_spell.configure(background="#d9d9d9")
        self.label_spell.configure(compound='left')
        self.label_spell.configure(disabledforeground="#a3a3a3")
        self.label_spell.configure(foreground="#000000")
        self.label_spell.configure(text='''Label''')

        self.Labelframe5 = tk.LabelFrame(self.top)
        self.Labelframe5.place(x=380, y=170, height=75, width=240)
        self.Labelframe5.configure(relief='groove')
        self.Labelframe5.configure(foreground="black")
        self.Labelframe5.configure(text='''Target''')
        self.Labelframe5.configure(background="#d9d9d9")
        self.Labelframe5.configure(highlightbackground="#d9d9d9")
        self.Labelframe5.configure(highlightcolor="black")

        self.label_from = tk.Label(self.Labelframe5)
        self.label_from.place(x=20, y=30, height=21, width=164
                , bordermode='ignore')
        self.label_from.configure(activebackground="#f9f9f9")
        self.label_from.configure(activeforeground="black")
        self.label_from.configure(anchor='w')
        self.label_from.configure(background="#d9d9d9")
        self.label_from.configure(compound='left')
        self.label_from.configure(disabledforeground="#a3a3a3")
        self.label_from.configure(foreground="#000000")
        self.label_from.configure(highlightbackground="#d9d9d9")
        self.label_from.configure(highlightcolor="black")
        self.label_from.configure(text='''None''')

        self.Button1 = tk.Button(self.Labelframe5)
        self.Button1.place(x=190, y=30, height=24, width=38, bordermode='ignore')

        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=kadala_support.del_from)
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(state='disabled')
        self.Button1.configure(text='''Clear''')

        self.Button3 = tk.Button(self.top)
        self.Button3.place(x=380, y=320, height=34, width=243)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=kadala_support.gamble)
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(state='disabled')
        self.Button3.configure(text='''Gamble''')

        self.Button3_1 = tk.Button(self.top)
        self.Button3_1.place(x=380, y=10, height=34, width=243)
        self.Button3_1.configure(activebackground="#ececec")
        self.Button3_1.configure(activeforeground="#000000")
        self.Button3_1.configure(background="#d9d9d9")
        self.Button3_1.configure(command=kadala_support.load_save)
        self.Button3_1.configure(compound='left')
        self.Button3_1.configure(disabledforeground="#a3a3a3")
        self.Button3_1.configure(foreground="#000000")
        self.Button3_1.configure(highlightbackground="#d9d9d9")
        self.Button3_1.configure(highlightcolor="black")
        self.Button3_1.configure(pady="0")
        self.Button3_1.configure(text='''Browse''')

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(x=380, y=50, height=55, width=240)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Character name''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(x=10, y=20, height=20, width=214, bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(state='readonly')
        self.Entry1.configure(textvariable=self.text_name)

        self.label_status = tk.Label(self.top)
        self.label_status.place(x=480, y=480, height=21, width=56)
        self.label_status.configure(activebackground="#f9f9f9")
        self.label_status.configure(activeforeground="black")
        self.label_status.configure(anchor='w')
        self.label_status.configure(background="#d9d9d9")
        self.label_status.configure(compound='left')
        self.label_status.configure(disabledforeground="#a3a3a3")
        self.label_status.configure(foreground="#000000")
        self.label_status.configure(highlightbackground="#d9d9d9")
        self.label_status.configure(highlightcolor="black")
        self.label_status.configure(text='''Waiting...''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Labelframe1_1 = tk.LabelFrame(self.top)
        self.Labelframe1_1.place(x=380, y=110, height=55, width=240)
        self.Labelframe1_1.configure(relief='groove')
        self.Labelframe1_1.configure(foreground="black")
        self.Labelframe1_1.configure(text='''Gold available''')
        self.Labelframe1_1.configure(background="#d9d9d9")
        self.Labelframe1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_1.configure(highlightcolor="black")

        self.Entry1_1 = tk.Entry(self.Labelframe1_1)
        self.Entry1_1.place(x=10, y=20, height=20, width=214
                , bordermode='ignore')
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")
        self.Entry1_1.configure(state='readonly')
        self.Entry1_1.configure(textvariable=self.text_gold)

        self.Labelframe1_1_1 = tk.LabelFrame(self.top)
        self.Labelframe1_1_1.place(x=380, y=250, height=55, width=240)
        self.Labelframe1_1_1.configure(relief='groove')
        self.Labelframe1_1_1.configure(foreground="black")
        self.Labelframe1_1_1.configure(text='''Price''')
        self.Labelframe1_1_1.configure(background="#d9d9d9")
        self.Labelframe1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_1_1.configure(highlightcolor="black")

        self.Entry1_1_1 = tk.Entry(self.Labelframe1_1_1)
        self.Entry1_1_1.place(x=10, y=20, height=20, width=214
                , bordermode='ignore')
        self.Entry1_1_1.configure(background="white")
        self.Entry1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(foreground="#000000")
        self.Entry1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1.configure(insertbackground="black")
        self.Entry1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1.configure(selectforeground="white")
        self.Entry1_1_1.configure(state='readonly')
        self.Entry1_1_1.configure(textvariable=self.text_price)

        self.Button3_2 = tk.Button(self.top)
        self.Button3_2.place(x=380, y=410, height=64, width=243)
        self.Button3_2.configure(activebackground="#ececec")
        self.Button3_2.configure(activeforeground="#000000")
        self.Button3_2.configure(background="#d9d9d9")
        self.Button3_2.configure(command=kadala_support.save_to)
        self.Button3_2.configure(compound='left')
        self.Button3_2.configure(disabledforeground="#a3a3a3")
        self.Button3_2.configure(foreground="#000000")
        self.Button3_2.configure(highlightbackground="#d9d9d9")
        self.Button3_2.configure(highlightcolor="black")
        self.Button3_2.configure(pady="0")
        self.Button3_2.configure(state='disabled')
        self.Button3_2.configure(text='''Save to''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(x=580, y=360, height=21, width=22)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''0''')
        self.Label1.configure(textvariable=self.label_gambled)
        self.label_gambled.set('''0''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(x=380, y=360, height=21, width=85)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Items gambled''')

def start_up():
    kadala_support.main()

if __name__ == '__main__':
    kadala_support.main()




