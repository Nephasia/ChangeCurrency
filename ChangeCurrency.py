#pip3 install forex-python - do pobrania paczki

from tkinter import *
from tkinter import messagebox
from forex_python.converter import CurrencyRates
from TextWithLabel import *

class NegativeValueError(Exception):
    pass

class Application(object):

    color = "lightgray"
    font = 'Helvetica 10 bold'

    def __init__(self):
        self.okno=Tk()
        self.okno.configure(background=self.color)
        self.okno.geometry("300x300")
        self.okno.title("Konwerter walut")
        self.ramka = Frame(self.okno, bg=self.color)
        self.ramka.grid()
        
        self.createWidgets()
        self.ramka.grid_columnconfigure(0, weight=2)
        self.ramka.grid_columnconfigure(1, weight=0)
        self.okno.mainloop()

    def createWidgets(self):
        etykieta1=Label(self.ramka, bg=self.color, text="Wprowadź kwotę w PLN", anchor='w',font=self.font)
        etykieta1.grid(row=0,column=0,sticky=W)

        self.pole1=Entry(self.ramka)
        self.pole1.grid(row=0,column=1,sticky=W)
        self.przycisk1=Button(self.ramka, bg=self.color,text="Przelicz", width=20,font=self.font)
        self.przycisk1.grid(row=1,column=0,sticky=W,pady=10)
        self.przycisk1["command"]=self.changeCurrency

        c = CurrencyRates()

        TextWithLabel.setFirstRow(3)
        TextWithLabel.setFont(self.font)
        TextWithLabel.setBgColor(self.color)

        self.TextWithLabel = []
        self.TextWithLabel.append(TextWithLabel(self.ramka, "EUR", c.get_rate('PLN', 'EUR')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "USD", c.get_rate('PLN', 'USD')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "GBP", c.get_rate('PLN', 'GBP')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "CHF", c.get_rate('PLN', 'CHF')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "AUD", c.get_rate('PLN', 'AUD')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "JPY", c.get_rate('PLN', 'JPY')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "SEK", c.get_rate('PLN', 'SEK')))
        self.TextWithLabel.append(TextWithLabel(self.ramka, "CZK", c.get_rate('PLN', 'CZK')))

    def refreshView(self, zl):
        for i in self.TextWithLabel:
            i.refresh(zl)
        
    def changeCurrency(self):
        try:
            zl = float(self.pole1.get())
            
            if float(self.pole1.get())< 0:
                raise NegativeValueError   

        except NegativeValueError:
            messagebox.showerror("Błąd!","Nie można przewalutować ujemnej kwoty!")
        except:
            messagebox.showerror("Błąd!","Podane dane muszą być liczbami dodatnimi!")
        else:
           self.refreshView(zl)

app = Application()
