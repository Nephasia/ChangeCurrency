from tkinter import *
from tkinter import messagebox

class TextWithLabel():

    bgColor = "gray"
    font = 'Helvetica 10 bold'
    rowInTurn = 0
    width = 20
    height = 1
    currency = 0

    def __init__(self, ramka, text, currency):
        self.pole=Text(ramka, width=self.width, height=self.height)
        self.pole.grid(row=TextWithLabel.rowInTurn,column=0,sticky=W,pady=2)
        self.etykieta=Label(ramka, bg=self.bgColor,text=text,font=self.font)
        self.etykieta.grid(row=TextWithLabel.rowInTurn, column=1, sticky=W,pady=2)
        self.currency = currency
        TextWithLabel.rowInTurn+=1

    def refresh(self, zl):

        value = zl * self.currency

        self.pole.delete(0.0, END)
        self.pole.insert(0.0, str(round(value, 4)))

    @staticmethod
    def setFirstRow(firstRow):
        TextWithLabel.rowInTurn = firstRow