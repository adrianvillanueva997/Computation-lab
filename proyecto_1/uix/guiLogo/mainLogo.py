from tkinter import *

class mainLogo():
    def __init__(self):
        self.root = Tk()
        self.root.title("Bienvenidos")
        self.root.geometry('800x600')
        self.root.minsize(800, 600)
        self.root.config(bd='10')
        self.root.config(relief='groove')
        self.root.config(bg='#cbccd1')

        # help-exit Frame
        self.exit_Frame = Frame(self.root, bg='#dfdfdf')

        def salir():
            self.root.destroy()

        self.exit_btn = Button(self.exit_Frame, text='Exit', padx=5, pady=5, command=salir)
        self.help_btn = Button(self.exit_Frame, text='Help', padx=5, pady=5)
        #self.exit_btn.config(relief='groove')
        self.exit_btn.pack(side='right', fill="both", expand=True)
        self.help_btn.pack(side='right', fill="both", expand=True)

        # img logo Frame
        self.logo_Frame = Frame(self.root,width=1000, height=800)

        self.myImg = PhotoImage(file='py.png')
        self.img_lbl = Label(self.logo_Frame, image=self.myImg)
        self.img_lbl.pack(fill="both", expand=True)
        self.img_lbl.config(bg='#cbccd1')

        # Three Dudes Inc. logo
        self.tdiName_Frame = Frame(self.root)

        self.tdiName_lbl = Label(self.tdiName_Frame, text='Three Dudes Inc.', bg='#cbccd1')
        self.tdiName_lbl.config(font=("Courier", 34))
        self.tdiName_lbl.pack()

        # button Frame
        # self.btn_Frame = Frame(self.mainFrame)
        self.btn_left_Frame = Frame(self.root, width=150, height=150)
        self.btn_right_Frame = Frame(self.root, width=150, height=150)

        # self.btn_left_Frame.pack(side='left', fill="both", expand=True)
        # self.btn_right_Frame.pack(side='right', fill="both", expand=True)

        self.myImg1 = PhotoImage(file='training.png')
        self.entrenamiento_btn = Button(self.btn_left_Frame, image=self.myImg1, padx='5', pady='5')
        self.myImg2 = PhotoImage(file='class.png')
        self.clasificador_btn = Button(self.btn_right_Frame, image=self.myImg2, padx='5', pady='5')
        #self.entrenamiento_btn = Button(self.btn_left_Frame, text='Entrenamiento',padx='10',pady='10')
        #self.clasificador_btn = Button(self.btn_right_Frame, text='Clasificador', padx='10', pady='10')
        self.entrenamiento_btn.pack()
        self.clasificador_btn.pack()

        # posicion de los mainFrame en el grid
        self.exit_Frame.grid(row=0, column=0,columnspan=2, sticky=E, padx= 5, pady=5)
        self.logo_Frame.grid(row=1, column=0,columnspan=2, sticky=N+S+E+W)
        self.tdiName_Frame.grid(row=2, column=0, columnspan=2, sticky=N+S)
        self.btn_left_Frame.grid(row=3, column=0, sticky=W, padx=85, pady=65)
        self.btn_right_Frame.grid(row=3, column=1, sticky=E, padx=85, pady=65)

        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.root.mainloop()

mainLogo()