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


    def onClick(self, args):
        if args == 1:
            print("test")
            # Label allgemein ändern wäre hier cool

            #a = self.bc_encoded

            #barcode = entry_1_txt.get()
            #dec_barcode = dec.decode(barcode)
            #self.label_1.configure(text = dec_barcode)
            #print(self.dec_barcode)
            #dec = bc.Decoder('DecodeSheet.txt')
        
        #if args == 2:
        #    print("button 2 clicked")
        #return self.label_1

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        btn1 = Button(self, text = "Code anzeigen", 
                            command=lambda: controller.onClick(1))
        
        
        entry = Entry(self, width=14)
        self.label_1 = Label(self, text = "")
        
        entry.pack()
        btn1.pack()
        self.label_1.pack()
        #self.label_1.configure(text=SeaofBTCapp.onClick.label_label)

    #    pass
    #     bc_encoded = StringVar()
    #     bc = entry.get()
    #     return bc_encoded



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
app.mainloop()