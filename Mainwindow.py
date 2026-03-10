import tkinter as tk
from tkinter import *
from tkinter import ttk
# from tkinter import font
import CreateModelWindow

def newWindow():
        window = CreateModelWindow.CreateWindow()

class MainWindow(Tk): # класс окна создания модели
    def __init__(self):
        super().__init__()
        # self.root = Tk()     # создаем корневой объект - окно
        self.title("Карточка модели")     # устанавливаем заголовок окна
        self.geometry("1200x700+50+50")
        self.resizable(True, False)
        self.minsize(200,150)
        self.maxsize(1280,728)   

        # кнопки управления

        self.MenuFrame = tk.Frame(self, background="#77dd77")
        self.MenuFrame.pack(fill=X, anchor=NW)

        self.create = tk.Button(self.MenuFrame, text="Создать модель", command=newWindow ,background="#d7fac8")
        self.create.pack(anchor=NW, padx=[10, 5], pady=[10, 5])

        # отображение информации о моделях
        
        self.MainFrame = tk.Frame(self) 
        self.MainFrame.pack(fill="both", expand=True)

        # модуль поиска модели

        self.ModelSearch = tk.Frame(self.MainFrame, background="#ffffff") #background="#d7fac8"
        self.ModelSearch.place(relwidth=0.33, relheight=0.5)

        self.ModelSearchLabelFrame = tk.LabelFrame(self.ModelSearch, bd=0, background="#d7fac8")
        self.ModelSearchLabelFrame.pack(padx=[10, 5], pady=[10, 5], expand=True, fill="both") 

        ttk.Label(self.ModelSearchLabelFrame, text="Structural models search", padding=5, background="#77dd77", font="Arial 11 normal roman").pack(anchor=NW, fill='both')

        # комбобокс

        self.Substances = ['protein', 'carbohydrate', 'fat']
        sub = StringVar(value=self.Substances[0])
        self.Combobox = ttk.Combobox(self.ModelSearchLabelFrame, values=self.Substances, textvariable=sub, background="#d7fac8")
        self.Combobox.pack(anchor=NW, padx=5, pady=[5, 0])
        # self.Combobox.bind("<<ComboboxSelected>>", self.selected)

        # поиск: поле + кнопка

        self.Find = tk.Frame(self.ModelSearchLabelFrame ,background="#d7fac8")
        self.Find.pack(anchor=NW, fill=X)

        self.ModelSearchEntry = tk.Entry(self.Find, width=23)
        self.ModelSearchEntry.pack(anchor=NW, padx=5, pady=[5, 0], side=LEFT)

        self.SearchButton = tk.Button(self.Find, text='Search',background="#d7fac8")
        self.SearchButton.pack(anchor=NW)

        # содержание таблицы
        
        self.SearchFrame = tk.Frame(self.ModelSearchLabelFrame, background="#d7fac8", bd=0) # "#b8e6a2"
        self.SearchFrame.pack(expand=True, anchor=NW, fill='both', pady=5, padx=5)

        self.SearchFrame.rowconfigure(index=0, weight=1)
        self.SearchFrame.columnconfigure(index=0, weight=1)

        self.SeachColumns = ("GNID", "Scheme name")
        self.data = [("GND00001", "-> PurE"), ("GND00002", "-> Purc"), ("GND00003", "-> Purb"), ("GND00237", "Ura + prpp -> UMP + ppi")]

        # стиль для заголовков таблицы

        self.HeadingStyle = ttk.Style()
        self.HeadingStyle.configure("Treeview.Heading", font="Arial 10 bold roman")
        
        # таблица

        self.tree = ttk.Treeview(self.SearchFrame, columns=self.SeachColumns, show="headings",)
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.tree.heading("GNID", text="GNID") # font="Arial 11 normal roman"
        self.tree.heading("Scheme name", text="Scheme name")

        self.tree.column("#1", stretch=False, minwidth=65, width=70)
        self.tree.column("#2", stretch=True, minwidth=180, width=180)

        for d in self.data:
            self.tree.insert("", END, values=d) 

        self.tree.bind("<<TreeviewSelect>>", self.ItemSelected)

        # прокрутка
        
        self.XSearchScrollBar = ttk.Scrollbar(self.SearchFrame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.XSearchScrollBar.set)
        self.XSearchScrollBar.grid(row=1, column=0, sticky="ew")
        
        self.YSearchScrollBar = ttk.Scrollbar(self.SearchFrame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.YSearchScrollBar.set)
        self.YSearchScrollBar.grid(row=0, column=1, sticky="ns")

        self.Star = Canvas(self.SearchFrame, background="white", width=10, height=10)
        self.Star.grid(row=1, column=1, sticky='nsew')

        self.Im = PhotoImage(file="star.png")
        
        self.Star.create_image(8, 8, image=self.Im)

        # модуль описания модели

        self.ModelDescription = tk.Frame(self.MainFrame, background="#ffffff")
        self.ModelDescription.place(relx=0.33, relwidth=0.67, relheight=0.5)

        self.ModelDescriptionFrame = tk.Frame(self.ModelDescription, background="#d7fac8")
        self.ModelDescriptionFrame.pack(padx=[5, 10], pady=[10, 5], expand=True, fill='both')

        self.ModelDescriptionLabel = ttk.Label(self.ModelDescriptionFrame, padding=5, background="#77dd77", font="Arial 11 normal roman", text="Description")
        self.ModelDescriptionLabel.pack(anchor=NW, fill=X)

        self.ReactionLabel = ttk.Label(self.ModelDescriptionFrame, padding=5, background="#d7fac8", text="Reaction")
        self.ReactionLabel.pack(anchor=NW, fill=X)
        
        ttk.Label(self.ModelDescriptionFrame, text="Model consist of:", background="#d7fac8", padding=[5, 0, 0, 5]).pack(anchor=NW, fill=X)

        self.DescriptionFrame = tk.Frame(self.ModelDescriptionFrame)
        self.DescriptionFrame.pack(padx=5, pady=5, expand=True, fill='both')

        self.DescriptionFrame.rowconfigure(index=0, weight=1)
        self.DescriptionFrame.columnconfigure(index=0, weight=1)

        self.DescriptionColumns = ("Alias", "Short name", "Function", "SID")
        self.DesData = [("s1", "Ura", "substrate", "SS000040"),
                        ("s1", "Ura", "substrate", "SS000040")]

        self.DescriptionTree = ttk.Treeview(self.DescriptionFrame, 
                                            columns=self.DescriptionColumns, 
                                            show="tree headings",
                                            selectmode='none')
        self.DescriptionTree.grid(row=0, column=0, sticky="nswe")

        self.DescriptionTree.column("#0", stretch=False, minwidth=50, width=50)
        self.DescriptionTree.column("#1", stretch=True, minwidth=70, width=100)
        self.DescriptionTree.column("#2", stretch=True, minwidth=200, width=200)
        self.DescriptionTree.column("#3", stretch=True, minwidth=100, width=100)
        self.DescriptionTree.column("#4", stretch=True, minwidth=100)
        
        # self.DescriptionTree.heading("#0", text="Huy")
        self.DescriptionTree.heading("Alias", text="Alias")
        self.DescriptionTree.heading("Short name", text="Short name")
        self.DescriptionTree.heading("Function", text="Function")
        self.DescriptionTree.heading("SID", text="SID")

        

        self.ImProt = tk.PhotoImage(file="protein.png")

        for d in self.DesData:
            self.DescriptionTree.insert("", END, image=self.ImProt, value=(d) )

        self.XDesScrollBar = ttk.Scrollbar(self.DescriptionFrame, orient='horizontal', command=self.DescriptionTree.xview)
        self.DescriptionTree.configure(xscrollcommand=self.XDesScrollBar.set)
        self.XDesScrollBar.grid(row=1, column=0, sticky="ew")
        
        self.YDesScrollBar = ttk.Scrollbar(self.DescriptionFrame, orient='vertical', command=self.DescriptionTree.yview)
        self.DescriptionTree.configure(yscrollcommand=self.YDesScrollBar.set)
        self.YDesScrollBar.grid(row=0, column=1, sticky="ns")

        self.Star = Canvas(self.DescriptionFrame, background="white", width=10, height=10)
        self.Star.grid(row=1, column=1, sticky='nsew')
            

        # модуль мат модели
        
        self.MathModel = tk.Frame(self.MainFrame, background="green")
        self.MathModel.place(rely=0.5, relheight=0.5, relwidth=1)

        self.mainloop()

    # def SubstanceSelected(self, event):
    #     return self.Combobox.get()

    def ItemSelected(self, event):
        selectedNumber = ""
        selectedReaction = ""
        for selItem in self.tree.selection():
            item = self.tree(selItem)
            reaction = item['value']
            selectedNumber = reaction["#0"]
            selectedReaction = reaction['#1']
        self.ModelDescriptionLabel["text"]=selectedNumber
        self.ReactionLabel["text"]=selectedReaction
    
MainWindow()
# for family in font.families():
#     print(family)