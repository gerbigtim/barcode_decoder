import barcode_decoder as bc  
from tkinter import *


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = False)

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

            # print(dict(list(dec_barcode.items())[0:1])) # Marke
            # print(dict(list(dec_barcode.items())[1:2])) # Art
            # print(dict(list(dec_barcode.items())[2:3])) # Material
            # print(dict(list(dec_barcode.items())[3:4])) # Größe
            # print(dict(list(dec_barcode.items())[4:5])) # Farbe



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
        self.frame1 = Frame(self)
        self.frame2 = Frame(self)
        self.frame3 = Frame(self)
        self.frame4 = Frame(self)
        
        self.frame1.pack(side=TOP)
        self.frame2.pack(side=TOP)
        self.frame3.pack(side=TOP)
        self.frame4.pack(side=TOP)

        self.bg = PhotoImage(file = "jean_maroe_wortmarke_grey.png")


        # BUTTONS DEF

        button1 = Button(self, text="Zurück",
                            command=lambda: controller.show_frame(StartPage))
        

        button2 = Button(self, text="Barcode erstellen",
                            command=lambda: controller.show_frame(PageTwo))
        

        btn1 = Button(self, text = "Code anzeigen", 
                            command=lambda: controller.onClick(1))
        btn2 = Button(self, text = "Code löschen", 
                            command=lambda: controller.onClick(2))
                            

        # ENTRY DEF
        
        self.entry_1 = StringVar()
        self.entry = Entry(self, width=14, text = self.entry_1)
        self.entry.focus() #auto cursor to entry field

        # GUI - CANVAS
        
        self.canvas1 = Canvas (self.frame1, width=400,height=400, bg = 'white')
        self.canvas1.pack(fill=BOTH, expand = True)
        self.canvas1.create_image(10,20,image = self.bg, anchor = "nw")


        # label = Label(self.frame1, text="Barcode auslesen", font=LARGE_FONT)
        # # label.pack(pady=10,padx=10)
        # label_canvas = self.canvas1.create_window(100,0,anchor ="nw", window = label)

        #field1 = Frame(background="white")

        #self.canvas1.create_text(180, 30, text = "Barcode auslesen", font =( 'bold',20),anchor="center")

        self.canvas1.create_text(20, 126, text = "Barcode:",anchor="nw")
        self.canvas1.create_window(70,124,anchor="nw",window = self.entry)
        self.canvas1.create_window(165,120,anchor="nw",window = btn1)
        self.canvas1.create_window(260,120,anchor="nw",window = btn2)

        self.canvas1.create_text(20, 160, text = "Marke",anchor="nw")
        self.canvas1.create_text(80, 160, text = "Art",anchor="nw")
        self.canvas1.create_text(140, 160, text = "Material",anchor="nw")
        self.canvas1.create_text(200, 160, text = "Größe",anchor="nw")
        self.canvas1.create_text(260, 160, text = "Farbe",anchor="nw")
        
        self.value_marke = self.canvas1.create_text(20, 180, text = "",anchor="nw")
        self.value_art = self.canvas1.create_text(80, 180, text = "",anchor="nw")
        self.value_material = self.canvas1.create_text(140, 180, text = "",anchor="nw")
        self.value_groesse = self.canvas1.create_text(200, 180, text = "",anchor="nw")
        self.value_farbe = self.canvas1.create_rectangle(260, 180, 290, 195, outline = '')



        self.canvas1.create_window(10,210, anchor= "nw", window = button1)


        # btn1.pack(side=LEFT,padx=5)
            # btn2.pack(side=LEFT,padx=5)

            # button1.pack(side = 'top', anchor='w',pady=20)
            
            
            # self.entry_label = Label(self.frame2, text = "Barcode:")

            # self.marke_label = Label(self.frame3, text = "Marke")
            # self.art_label = Label(self.frame3, text = "Art")
            # self.material_label = Label(self.frame3, text = "Material")
            # self.groesse_label = Label(self.frame3, text = "Größe")
            # self.farbe_label = Label(self.frame3, text = "Farbe")

            # self.marke_value_label = Label(self.frame3, text = "")
            # self.art_value_label = Label(self.frame3, text = "")
            # self.material_value_label = Label(self.frame3, text = "")
            # self.groesse_value_label = Label(self.frame3, text = "")
            # self.farbe_value_label = Label(self.frame3, text = "")


            # self.label_1 = Label(self, text = "")
            # self.label_2 = Label(self, text = "")
            # self.label_error = Label(self, text = "")

            
            # #field1.pack(fill='x',ipady=10)
            # #self.label_1.pack(side=BOTTOM)

            # self.marke_label.grid(row=0, column=0)
            # self.art_label.grid(row=0, column=1)
            # self.material_label.grid(row=0, column=2)
            # self.groesse_label.grid(row=0, column=3)
            # self.farbe_label.grid(row=0, column=4)
            

            # #self.label_2.pack(side = BOTTOM)

            # self.marke_value_label.grid(row=1, column=0)
            # self.art_value_label.grid(row=1, column=1)
            # self.material_value_label.grid(row=1, column=2)
            # self.groesse_value_label.grid(row=1, column=3)
            # self.farbe_value_label.grid(row=1, column=4)


            
            # #self.entry_label.pack(side=LEFT,padx=5,pady=15)
            # #self.entry.pack(side=LEFT,padx=1)

            #button2.pack(side = BOTTOM)
        
  
        # self.label_error.pack()

    def change_label(self, text, error):

        keys = list(text.keys())
        values = list(text.values())
        
        self.canvas1.itemconfigure(self.value_marke, text = values[0])
        self.canvas1.itemconfigure(self.value_art, text = values[1])
        self.canvas1.itemconfigure(self.value_material, text = values[2])
        self.canvas1.itemconfigure(self.value_groesse, text = values[3])
        self.canvas1.itemconfigure(self.value_farbe, fill ='#' + values[4])

        # self.marke_value_label.configure(text=values[0])
        # self.art_value_label.configure(text=values[1])
        # self.material_value_label.configure(text=values[2])
        # self.groesse_value_label.configure(text=values[3])
        # self.farbe_value_label.configure(bg='#'+values[4], width = 5)

        #self.label_1.configure(text=values)
        #self.label_error.configure(text=error)
        
    def change_entry(self, text):
        self.entry.delete('0', END)
        #self.label_1.configure(text=text)



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
app.iconbitmap("Jean_maroe_logo_icon.ico")
app.title("Jean Maroe Decoder")
app.geometry('360x250') 
app.mainloop()