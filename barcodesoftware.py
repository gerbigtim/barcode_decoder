import barcode_decoder as bc  
from tkinter import *

class Display:
    def __init__(self):
        self.root = Tk()
        self.root.title("Jean Maroe Decoder")

        #Create Widgets
        self.btn1 = Button(self.root, text = "Code anzeigen", command=lambda:self.onClick(1))
        
        self.entry_1_txt = StringVar()
        self.entry = Entry(self.root, width=14, text = self.entry_1_txt)

        self.label_1 = Label(self.root, text = "")
        
        self.entry.pack()
        self.btn1.pack()
        self.label_1.pack()
        
        self.root.mainloop()

    def onClick(self, args):
        if args == 1:
            print(self.entry_1_txt.get())
            self.dec = bc.Decoder('DecodeSheet.txt')
            self.barcode = self.entry_1_txt.get()
            self.dec_barcode = self.dec.decode(self.barcode)
            self.label_1.configure(text = self.dec_barcode)
            print(self.dec_barcode)
        if args == 2:
            print("button 2 clicked")


    # def Decoding(self):
    #     self.dec = bc.Decoder('DecodeSheet.csv')
    #     self.barcode = self.entry_1_txt.get()
    #     self.dec_barcode = self.dec.decode(self.barcode)
    #     return self.dec_barcode

# class App:
      
#     while True:     
#         barcode  = input('Barcode : ')     
#         if barcode.startswith('q'):         
#             break     
#         print(dec.decode(barcode))

# root = Tk()
# app = App(root)
# root.mainloop()

display = Display()