import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font


def createCheckBox(frame, reaction): # функция создания и добавления чекбоксов
        enabled = IntVar()
        reactionCheck = ttk.Checkbutton(frame, text=reaction, variable=enabled)
        reactionCheck.pack(anchor=NW, padx=5, pady=0)

def doubleCheckBox(frame, reaction): # функция создания и добавления чекбоксов
        enabled = IntVar()
        reactionCheck = ttk.Checkbutton(frame, text="", variable=enabled)
        reactionCheck.pack(side="left", anchor=NW, padx=[5, 0], pady=0)
        enabled1 = IntVar()
        reactionCheck = ttk.Checkbutton(frame, text=reaction, variable=enabled1)
        reactionCheck.pack(side="left", anchor=NW, pady=0)

    

class CreateWindow(Tk): # класс окна создания модели
    def __init__(self):
        super().__init__()

        self.title("Создание модели")
        self.geometry("1000x600") 

        self.menuFrame = tk.Frame(self, background="#77dd77")
        self.menuFrame.pack(fill=X)
        self.modName = ttk.Label(self.menuFrame , text="Model Name: ", background="#77dd77").pack(side='left', anchor=N, pady=5, padx=10)
        self.entry=ttk.Entry(self.menuFrame).pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.BackButton = ttk.Button(self.menuFrame, text='Cancel', command=lambda: self.destroy())
        self.BackButton.pack(side='right', padx=10, pady=10)
        self.CreateButton = ttk.Button(self.menuFrame, text='Create', command=lambda: self.destroy())
        self.CreateButton.pack(side='right', padx=10, pady=10)

        self.ReactCompFrame = tk.Frame(self)
        self.ReactCompFrame.pack(expand = True, fill = 'both')

        self.helpFrame1 = tk.Frame(self.ReactCompFrame, background="#77dd77") 
        self.helpFrame2 = tk.Frame(self.ReactCompFrame, background="#77dd77")
        
        self.helpFrame1.place(x = 0, y = 0, relwidth = 0.7, relheight = 1)
        self.helpFrame2.place(relx = 0.7, y = 0, relwidth = 0.3, relheight = 1) # делят фрэйм в соотношении 7:3

        self.LabelFrame1 = tk.LabelFrame(self.helpFrame1, bd=0)
        self.LabelFrame2 = tk.LabelFrame(self.helpFrame2, bd=0)

        self.LabelFrame1.pack(padx=[10, 5], pady=[5, 10], expand = True, fill = 'both') 
        self.LabelFrame2.pack(padx=[5, 10], pady=[5, 10], expand = True, fill = 'both') # делают красивые отступы и содержат канвас

        # прокрутка реакций 
        self.ReactCanvas = Canvas(self.LabelFrame1, borderwidth=0, background='#d1f0c2')
        self.ReactCanvas.pack(expand = True, fill = 'both') 
        self.ReactScrollBar = ttk.Scrollbar(self.LabelFrame1, orient='horizontal', command=self.ReactCanvas.xview)
        self.ReactScrollBar.pack(side='bottom',fill=X) # создание канваса и прокрутки на нем

        self.ReactCanvas.configure(xscrollcommand=self.ReactScrollBar.set)
        self.ReactCanvas.bind('<Configure>', # привязка прокрутки к канвасу
                              lambda x: self.ReactCanvas.configure(scrollregion=self.ReactCanvas.bbox('all')))

        self.ReactFrame1 = tk.Frame(self.ReactCanvas, background='#d1f0c2', borderwidth=0) # фрэйм, в котром хранятся элементы
        self.ReactCanvas.create_window((0,0), window=self.ReactFrame1, anchor=NW)


        # прокрутка компонентов
        self.CompCanvas = Canvas(self.LabelFrame2, borderwidth=0, background='#d1f0c2')
        self.CompCanvas.pack(expand = True, fill = 'both') 
        self.CompScrollBar = ttk.Scrollbar(self.LabelFrame2, orient='horizontal', command=self.CompCanvas.xview)
        self.CompScrollBar.pack(side='bottom',fill=X) # создание канваса и прокрутки на нем

        self.CompCanvas.configure(xscrollcommand=self.CompScrollBar.set)
        self.CompCanvas.bind('<Configure>', # привязка прокрутки к канвасу
                              lambda x: self.CompCanvas.configure(scrollregion=self.CompCanvas.bbox('all')))

        self.ReactFrame2 = tk.Frame(self.CompCanvas, background='#d1f0c2', borderwidth=0) # фрэйм, в котром хранятся элементы
        self.CompCanvas.create_window((0,0), window=self.ReactFrame2, anchor=NW)

        labelStyle = ttk.Style(self) # стиль для лэйблов
        labelStyle.configure("TLabel",
                           background="#d1f0c2",
                           size=10)
        
        checkBoxStyle = ttk.Style(self) # стиль для чекбоксов
        checkBoxStyle.configure("TCheckbutton", 
                                background="#d1f0c2",
                                family="Times New Roman",
                                size=14,
                                weight="normal", slant="roman")

        GRL = ttk.Label(self.ReactFrame1, text="Global Reactions List")
        IOC = ttk.Label(self.ReactFrame2, text="In-, Out- Components")
        f = font.Font(GRL, GRL.cget("font"))
        f.configure(underline=True)
        GRL.configure(font=f)
        IOC.configure(font=f) # подчеркиване лэйблов

        GRL.pack(anchor=NW, padx=5, pady=5)
        IOC.pack(anchor=NW, padx=5, pady=5)
        
        createCheckBox(self.ReactFrame1, "Gliucose")
        createCheckBox(self.ReactFrame1, "ff kf*e0*(s1/kms1)*(s2/kms2)/((1+s1/kms1+p1/kip1)*(1+s2/kms2+p2/kip2)) ff kf*e0*(s1/kms1)*(s2/kms2)/((1+s1/kms1+p1/kip1)*(1+s2/kms2+p2/kip2))")
        doubleCheckBox(self.ReactFrame2, "G6P")
        self.mainloop()