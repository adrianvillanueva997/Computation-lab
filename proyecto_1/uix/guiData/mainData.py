from tkinter import *

class mainData():
    def __init__(self):
        self.root = Tk()
        self.root.title("data")
        self.root.geometry('1000x850')
        self.root.minsize(1000, 850)
        self.root.config(bd='10')
        self.root.config(relief='groove')
        self.root.config(bg='#cbccd1')

        # back-exit Frame ---------------------------------------------------------------------->
        self.exit_Frame = Frame(self.root, bg='#cbccd1')

        def salir():
            self.root.destroy()

        self.exit_btn = Button(self.exit_Frame, text='Exit', padx=5, pady=5, command=salir)
        self.back_btn = Button(self.exit_Frame, text='Back', padx=5, pady=5)
        # self.exit_btn.config(relief='groove')
        self.exit_btn.pack(side='right', fill="both", expand=True)
        self.back_btn.pack(side='right', fill="both", expand=True)

        # some tittle Frame ---------------------------------------------------------------------->
        self.title_Frame = Frame(self.root, bg='#cbccd1')

        self.someTitle_lbl = Label(self.title_Frame, text='Select Data and Model', bg='#cbccd1')
        self.someTitle_lbl.config(font=("Courier", 34))
        self.someTitle_lbl.pack()

        # Select Path Frame ---------------------------------------------------------------------->
        self.selectPath_Frame = Frame(self.root)
        self.selectPath_Frame.config(bg='#cbccd1')
        # self.center_Canvas = Canvas(self.selectPath_Frame, bg='#b8b8b8')
        # self.center_Canvas.pack()

        self.selectPathTable_Frame = Frame(self.selectPath_Frame)
        self.selectPathTable_Frame.pack(fill=BOTH, pady=150)
        # Good - Neutral - Bad icons
        self.myImgHappy = PhotoImage(file='happyIcon.png')
        self.imgModelHappy_lbl = Label(self.selectPathTable_Frame, image=self.myImgHappy)
        self.imgModelHappy_lbl.config(bg='#eaeaea')

        self.myImgNeutral = PhotoImage(file='neutralIcon.png')
        self.imgModelNeutral_lbl = Label(self.selectPathTable_Frame, image=self.myImgNeutral)
        self.imgModelNeutral_lbl.config(bg='#eaeaea')

        self.myImgSad = PhotoImage(file='sadIcon.png')
        self.imgModelSad_lbl = Label(self.selectPathTable_Frame, image=self.myImgSad)
        self.imgModelSad_lbl.config(pady=10, bg='#eaeaea')
        # Path Entry + button
        self.selectGood_entry = Entry(self.selectPathTable_Frame, justify='right')
        self.selectButton_btn = Button(self.selectPathTable_Frame, text='Select Path')

        self.selectNeutral_entry = Entry(self.selectPathTable_Frame, justify='right')
        self.selectButton1_btn = Button(self.selectPathTable_Frame, text='Select Path')

        self.selectBad_entry = Entry(self.selectPathTable_Frame, justify='right')
        self.selectButton2_btn = Button(self.selectPathTable_Frame, text='Select Path')
        # Grid Location
        self.imgModelHappy_lbl.grid(row=0, column=0, rowspan=2, pady=5, sticky=N+S+W+E)
        self.imgModelNeutral_lbl.grid(row=2, column=0,rowspan=2, pady=5, sticky=N+S+W+E)
        self.imgModelSad_lbl.grid(row=4, column=0,rowspan=2, pady=5, sticky=N+S+W+E)
        self.selectGood_entry.grid(row=0, column=1,padx=35, ipadx=200, sticky=N)
        self.selectNeutral_entry.grid(row=2, column=1,padx=35, ipadx=200, sticky=N)
        self.selectBad_entry.grid(row=4, column=1,padx=35, ipadx=200, sticky=N)
        self.selectButton_btn.grid(row=1, column=1, padx=35, sticky=W)
        self.selectButton1_btn.grid(row=3, column=1, padx=35, sticky=W)
        self.selectButton2_btn.grid(row=5, column=1, padx=35, sticky=W)


        # Select Model Frame ---------------------------------------------------------------------->
        self.selectModel_Frame = Frame(self.root)

        self.selectModelGrid_Frame = Frame(self.selectModel_Frame)
        self.selectModelGrid_Frame.pack(side='left', anchor='n')
        # img left Frame
        self.myImgModel = PhotoImage(file='selectModel.png')
        self.imgModel_lbl = Label(self.selectModelGrid_Frame, image=self.myImgModel)
        #self.imgModel_lbl.pack(fill="both", expand=True)
        self.imgModel_lbl.config(bg='#eaeaea')
        # entry + select btn right Frame
        self.selectModel_entry = Entry(self.selectModelGrid_Frame, justify='right')
        self.selectModel_btn = Button(self.selectModelGrid_Frame, text='Select Model')
        # Grid location
        self.imgModel_lbl.grid(row=1, column=0, rowspan=2)
        self.selectModel_entry.grid(row=1, column=1)
        self.selectModel_btn.grid(row=2, column=1)

        # start training Button Frame ---------------------------------------------------------------------->
        self.startTraining_Frame = Frame(self.root)

        self.startTraining_btn = Button(self.startTraining_Frame, text='Start Training', padx=10, pady=10)
        self.startTraining_btn.pack()

        # position of the mainData frames into the grid ---------------------------------------------------------------------->
        self.exit_Frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=E)
        self.title_Frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.selectPath_Frame.grid(row=2, column=0, columnspan=2, padx=75, sticky=N+S)
        self.selectModel_Frame.grid(row=3, column=0, padx=85, pady=65, sticky=W)
        self.startTraining_Frame.grid(row=3, column=1, padx=85, pady=65, sticky=E)

        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(1, weight=1)

        self.root.mainloop()

mainData()