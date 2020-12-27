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
            print("test")

            dec = bc.Decoder('DecodeSheet.txt')
            barcode = self.get_page_instance(PageOne).entry_1.get()
            dec_barcode = dec.decode(barcode)

            PageOne.change_label(self.get_page_instance(PageOne), dec_barcode)
        
        #if args == 2:
        #    print("button 2 clicked")


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
        
        self.entry_1 = StringVar()
        entry = Entry(self, width=14, text = self.entry_1)
        

        self.label_1 = Label(self, text = "HUHU")
        
        entry.pack()
        btn1.pack()
        self.label_1.pack()
        #self.label_1.configure(text=SeaofBTCapp.onClick.label_label)


    def change_label(self, text):#="testtest"):
        self.label_1.configure(text=text)


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