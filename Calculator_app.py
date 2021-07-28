# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:58:39 2021

@author: user
"""

from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial
from math import *


convert_constant = 1
inverse_convert_constant = 1

def fsin(arg):
    return sin(arg * convert_constant)


def fcos(arg):
    return cos(arg * convert_constant)


def ftan(arg):
    return tan(arg * convert_constant)


def arcsin(arg):
    return inverse_convert_constant * (asin(arg))


def arccos(arg):
    return inverse_convert_constant * (acos(arg))


def arctan(arg):
    return inverse_convert_constant * (atan(arg))


def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)

   
def calc(entry):
    input_info = entry.get()        
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.resizable(250, 250)
    popup.geometry("250x250")
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()

def convert_deg(self):
    global convert_constant
    global inverse_convert_constant
    convert_constant = pi / 180
    inverse_convert_constant = 180 / pi
    self.btn_Rad["foreground"] = 'white'
    self.btn_Deg["foreground"] = 'orange'

def convert_rad(self):
    global convert_constant
    global inverse_convert_constant
    convert_constant = 1
    inverse_convert_constant = 1
    self.btn_Rad["foreground"] = 'orange'
    self.btn_Deg["foreground"] = 'white'


def cal():
    root = Tk()
    root.title("Calc")
    root.resizable(1000, 1000)

    entry_font = font.Font(size=15)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=8,
               sticky=N + W + S + E, padx=5, pady=5)

    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'
    other_button_bg = '#DDDDDD'
    text_fg = '#FFFFFF'
    button_active_bg = '#C0C0C0'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg)

    button7 = num_button(text='7', bg=num_button_bg,
                         command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5)

    button10 = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=4, column=3, pady=5)

    button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2, pady=5)

    button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3, pady=5)

    button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5)

    button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=2, column=3, pady=5)

    button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
    #button0.grid(row=5, column=0, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)
    button0.grid(row=5, column=0,  pady=5)

    button13 = num_button(text='.', command=lambda: get_input(entry, '.'))
    button13.grid(row=5, column=1, pady=5)

    button14 = Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3, pady=5)

    button15 = Button(root, text='del', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=1, column=0, columnspan=2,
                  padx=3, pady=5, sticky=N + S + E + W)

    button16 = Button(root, text='C', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=1, column=2, pady=5)

    button17 = Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=3, pady=5)

    button18 = Button(root, text='^', fg=text_fg,bg=num_button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '**'))
    button18.grid(row=5, column=2, pady=5)
    
    button19 = num_button(text='√x', bg=cal_button_bg,command=lambda: get_input(entry, 'sqrt('))
    button19.grid(row=2, column=4, pady=5)

    button20 = num_button(text='(', bg=cal_button_bg,command=lambda: get_input(entry, '('))
    button20.grid(row=3, column=4, pady=5)
    
    button21 = num_button(text=')',bg=cal_button_bg, command=lambda: get_input(entry, ')'))
    button21.grid(row=4, column=4, pady=5)

    button22 = num_button(text="π", bg=cal_button_bg,command=lambda: get_input(entry,'pi'))
    button22.grid(row=5, column=4, pady=5)

    button23 = num_button(text="x2", bg=cal_button_bg,command=lambda: get_input(entry,'*'))
    button23.grid(row=1, column=4, pady=5)

    button25 = num_button(text="n!", command=lambda: get_input(entry, 'factorial('))
    button25.grid(row=2, column=7, pady=5)

    btn_sin_inverse = num_button(text=u"sin-\u00B9",
                                         command=lambda: get_input(entry,'arcsin('))
    btn_sin_inverse.grid(row=4, column=6, pady=5)
        # cos inverse function
    btn_cos_inverse = num_button(text=u"cos-\u00B9",
                                         command=lambda: get_input(entry,'arccos('))
    btn_cos_inverse.grid(row=5, column=6, pady=5)
        # tan inverse function
    btn_tan_inverse = num_button(text=u"tan-\u00B9",
                                         command=lambda: get_input(entry,'arctan('))
    btn_tan_inverse.grid(row=1, column=7, pady=5)

    # sin function that returns value from -1 to 1 by default
    btn_sin = num_button(text="sin", command=lambda: get_input(entry,'sin('))
    btn_sin.grid(row=1, column=6)
        # cos function that returns value from -1 to 1 by default
    btn_cos = num_button(text="cos", command=lambda: get_input(entry,'cos('))
    btn_cos.grid(row=2, column=6)
        # tan function
    btn_tan = num_button(text="tan", command=lambda: get_input(entry,'tan('))
    btn_tan.grid(row=3, column=6)

    root.mainloop()


if __name__ == '__main__':
    cal()
    