import barcode_decoder as bc  
from tkinter import *

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def get_page_instance(self, pagename):
        return self.frames[pagename]

    def onClick(self, args):
        if args == 1:
            dec = bc.Decoder('DecodeSheet.txt')
            barcode = self.get_page_instance(PageOne).entry_1.get()
            dec_barcode = dec.decode(barcode)


            #label change @ pageOne/change_label
            PageOne.change_label(self.get_page_instance(PageOne), dec_barcode, "")
        
        if args == 2:
            #label change @ pageOne/change_label
            PageOne.change_entry(self.get_page_instance(PageOne),"")
            

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Wähle die Funktion:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = Button(self, text="Barcode auslesen",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = Button(self, text="Barcode erstellen",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Barcode auslesen", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #field1 = Frame(background="white")

        button1 = Button(self, text="Zurück zur Funktionswahl",
                            command=lambda: controller.show_frame(StartPage))
        

        button2 = Button(self, text="Barcode erstellen",
                            command=lambda: controller.show_frame(PageTwo))
        

        btn1 = Button(self, text = "Code anzeigen", 
                            command=lambda: controller.onClick(1))
        btn2 = Button(self, text = "Code löschen", 
                            command=lambda: controller.onClick(2))
        
        self.entry_1 = StringVar()
        self.entry = Entry(self, width=14, text = self.entry_1)
        
        self.entry_label = Label(self, text = "Barcode:")
        self.label_1 = Label(self, text = "")
        self.label_error = Label(self, text = "")


        #field1.pack(fill='x',ipady=10)
        self.label_1.pack(side=BOTTOM)
        button1.pack(side = 'top', anchor='w',padx=5,pady=5)
        
        self.entry_label.pack(side=LEFT,padx=5,pady=15)
        self.entry.pack(side=LEFT,padx=1)
        self.entry.focus() #auto cursor to entry field
        btn1.pack(side=LEFT,padx=5)
        btn2.pack(side=LEFT,padx=5)
        
        
        
        #button2.pack(side = BOTTOM)
        self.label_error.pack()

    def change_label(self, text, error):
        self.label_1.configure(text=text)
        self.label_error.configure(text=error)
        
    def change_entry(self, text):
        self.entry.delete('0', END)
        self.label_1.configure(text=text)

class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()



app = SeaofBTCapp()
app.title("Jean Maroe Decoder")
app.geometry('500x150') 
app.mainloop()