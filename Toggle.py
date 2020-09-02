#Author: Dmitri Lyalikov
#Rev. A1, 9/1/2020

import tkinter as tk
from tkinter import *

class Toggle(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.grid(row = 0, column = 0, sticky = NW)
        self.configure(background='grey')
        self.frame.configure(background='light blue')
        self.title('Harmonic Oscillator')
        self.minsize(700, 450)

        self.Mass = Label(self.frame, text = 'Mass', font = 'Helvetica 10 bold')
        self.Mass.grid(row = 3, column = 0, padx = 1, pady = 5, sticky = NW)
        self.Chassis_Label = Label(self.frame, text = 'Input Parameters', font = 'Helvetica 10 bold')
        self.Chassis_Label.grid(row = 0, column = 0,  sticky = NW)

        self.Mass_label = Label(self.frame, text = 'Mass')
        self.Mass_label.grid(row = 1, column = 0, padx = 5, sticky = NW)
        self.Mass = ['Mass', Scale(self.frame, orient=HORIZONTAL, from_ = 1, to = 10, command = self.print_value)]
        self.Mass[1].grid(row = 1, column = 1, sticky = NW, columnspan = 2)

        self.Spring_label = Label(self.frame, text = 'Spring Constant')
        self.Spring_label.grid(row = 2, column = 0, padx = 5, sticky = SW)
        self.Spring = ['Spring Constant', Scale(self.frame, orient=HORIZONTAL, from_ = 1, to = 10, command = self.print_value)]
        self.Spring[1].grid(row = 2, column = 1, pady = 5, sticky = SW, columnspan = 2)

    def print_value(self, val):
        print(val)
