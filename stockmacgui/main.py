import tkinter as tk
import random
import os
#import finanace
from tkinter import Entry
import webbrowser
class StockPage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.labels()
        self.widgets()
        self.input()


    #Labels Within our gui
    def labels(self):
        
        self.label_one = tk.Label(self, text="Stock Notifer")
        self.label_two = tk.Label(self, text="Name Of IPO")
        self.label_three = tk.Label(self, text="Time Interval")

        self.label_one.grid(column=1, row=0)

        self.label_two.grid(column=1, row=2)
        self.label_three.grid(column=1, row = 4)

    #Buttons within our gui
    def widgets(self):
        self.quitButton = tk.Button(self, text="Exit", command=self.quit)
        self.github = tk.Button(self, text="Github", command=lambda: webbrowser.open("https://github.com/codingdudepy"))
        self.contact = tk.Button(self, text="Contact")
        self.package = tk.Button(self, text="Package", command=lambda: webbrowser.open("https://pypi.org/project/yfinance/"))

        #positioning buttons
        self.github.grid(column=0, row=1)
        self.package.grid(column=2, row=1)
        self.contact.grid(column=1, row=1)
        self.quitButton.grid(column=1, row=7)


    #Defining input labels and functions for each entry
    def input(self):
        self.entry1 = Entry(self, bd =5)
        self.entry2 = Entry(self, bd=5)
        self.entry2.grid(column=1, row = 5)
        self.entry1.grid(column=1, row=3)


app = StockPage()
app.master.title("Stock notifier")
app.mainloop()
