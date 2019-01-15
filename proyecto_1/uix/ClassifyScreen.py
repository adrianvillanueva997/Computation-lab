from tkinter import *

from proyecto_1.uix import MainScreen as MS
from tkinter.filedialog import askdirectory
from proyecto_1.ETL import Models


class ClassifyScreenController():

    def handle_event(self, window, command, **kwargs):
        if command == "EXIT":
            self.exit(window)
        elif command == "BACK":
            self.goto_previous(window)
        elif command == "SELECT_PATH":
            self.select_path(window)
        elif command == "SELECT_MODEL":
            self.select_model(window)
        elif command == "SELECT_VECTOR":
            self.select_path(window)
        elif command == "SELECT_GOOD":
            self.select_path(window)
        elif command == "SELECT_NEUTRAL":
            self.select_path(window)
        elif command == "SELECT_BAD":
            self.select_path(window)
        elif command == "IMPORT_MODEL":
            self.import_model()
        elif command == "CLASSIFY":
            self.classify(window)
        else:
            print("Unrecognized command %s" % command)

    def exit(self, window):
        print("TODO implement exit")

    def goto_previous(self, window):
        window.root.remove_frame()
        MS.MainScreen(window.root)

    def select_path(self, window):
        folder = askdirectory()
        window.selectPath_entry.delete(0, END)
        window.selectPath_entry.insert(END, folder)
        print("TODO implement select_path")

    def select_model(self, window):
        Models.load_model()
        #generate_unlabeled_data(data)
    def import_model(self):
        #Do we need this? Doesn't seem like so
        print("TODO implement import_model")

    def classify(self):
        print("TODO implement classify")


class ClassifyScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master

        # back-exit Frame ---------------------------------------------------------------------->
        self.exit_Frame = Frame(self.root, bg='#cbccd1') ##cbccd1

        self.controller = ClassifyScreenController()

        def send_event(command, **kwargs):
            self.controller.handle_event(self, command, **kwargs)

        self.exitButtons_Frame = Frame(self.exit_Frame, bg='#cbccd1', padx=10, pady=10)
        self.exit_btn = Button(self.exitButtons_Frame, text='Exit', padx=5, pady=5,cursor='hand2', command=lambda: send_event("EXIT"))
        self.back_btn = Button(self.exitButtons_Frame, text='Back', padx=5, pady=5,cursor='hand', command=lambda: send_event("BACK"))
        self.exitButtons_Frame.pack(side='right')
        self.exit_btn.pack(side='right', fill="both", expand=True)
        self.back_btn.pack(side='right', fill="both", expand=True)

        # some title Frame --------------------------------------------------------------------->
        self.title_Frame = Frame(self.root, bg='#cbccd1')
        self.someTitle_lbl = Label(self.title_Frame, text='Select Data and Model', bg='#cbccd1')
        self.someTitle_lbl.config(font=("Courier", 34))
        self.someTitle_lbl.pack()

        # center table Frame ------------------------------------------------------------------- >
        self.center_Frame = Frame(self.root, pady=130, bg='#cbccd1')
        self.center_Canvas = Canvas(self.center_Frame, bg='#b8b8b8')#b8b8b8
        #self.top_Frame = Frame(self.center_Canvas)
        self.myImgReviews = PhotoImage(file='resources/reviews1.png')
        self.imgReviews_lbl = Label(self.center_Canvas, image=self.myImgReviews)
        self.imgReviews_lbl.config(bg='#eaeaea', relief='sunken')
        self.selectPath_entry = Entry(self.center_Canvas, justify='left', relief=GROOVE)
        self.selectPath_entry.configure(width=40)
        self.selectPath_btn = Button(self.center_Canvas, text='Select Path', command=lambda: send_event("SELECT_PATH"))
        self.selectPath_btn.configure(cursor='hand')

        self.center_Canvas.pack(padx=50, ipadx=150)
        #self.top_Frame.pack(side=TOP)
        self.imgReviews_lbl.pack(side=LEFT, padx=15, pady=15)
        self.selectPath_entry.pack(side=LEFT, padx=5)
        self.selectPath_btn.pack(side=LEFT, padx=15)

        # Unlabeled path Frame ------------------------------------------------------------------->
        self.unlabeledCenter_Frame = Frame(self.root, bg='#cbccd1')

        self.top_Frame = Frame(self.unlabeledCenter_Frame, bg='#cbccd1')
        self.good_Entry = Entry(self.top_Frame, justify=LEFT, relief=GROOVE)
        self.good_Entry.configure(width=50)
        self.good_btn = Button(self.top_Frame, text='Save Good', padx=10,cursor='hand',
                               command=lambda: send_event("SELECT_GOOD"))

        self.mid_Frame = Frame(self.unlabeledCenter_Frame, bg='#cbccd1')
        self.neutral_Entry = Entry(self.mid_Frame, justify=LEFT, relief=GROOVE)
        self.neutral_Entry.configure(width=50)
        self.neutral_btn = Button(self.mid_Frame, text='Save Neutral', padx=10,cursor='hand',
                                  command=lambda: send_event("SELECT_NEUTRAL"))

        self.bottom_Frame = Frame(self.unlabeledCenter_Frame,bg='#cbccd1')
        self.bad_Entry = Entry(self.bottom_Frame, justify=LEFT, relief=GROOVE)
        self.bad_Entry.configure(width=50)
        self.bad_btn = Button(self.bottom_Frame, text='Save Bad', padx=10,cursor='hand',
                              command=lambda: send_event("SELECT_BAD"))

        self.top_Frame.pack(side=TOP)
        self.mid_Frame.pack(side=TOP)
        self.bottom_Frame.pack(side=TOP)
        self.good_Entry.pack(side=LEFT, padx=20)
        self.good_btn.pack(side=LEFT)
        self.neutral_Entry.pack(side=LEFT, padx=20)
        self.neutral_btn.pack(side=LEFT)
        self.bad_Entry.pack(side=LEFT, padx=20)
        self.bad_btn.pack(side=LEFT)


        # Bottom left menu ------------------------------------------------------------------->
        self.selectModel_Frame = Frame(self.root, pady=15, bg='#cbccd1')
        self.myImgModel = PhotoImage(file='resources/selectModel.png')
        self.imgModel_lbl = Label(self.selectModel_Frame, image=self.myImgModel)
        self.imgModel_lbl.configure(relief='sunken')

        #self.modelVar.trace('w', self.select_model)
        self.left_Frame = Frame(self.selectModel_Frame)
        self.model_entry = Entry(self.selectModel_Frame, justify='left', relief=GROOVE)
        self.model_btn = Button(self.selectModel_Frame, text='Select Model', padx=10,
                                command=lambda: send_event("SELECT_MODEL"),cursor='hand')
        self.right_Frame = Frame(self.selectModel_Frame)
        self.vector_entry = Entry(self.selectModel_Frame, justify='left', relief=GROOVE)
        self.vector_btn = Button(self.selectModel_Frame, text='Select Vector', padx=10,
                                command=lambda: send_event("SELECT_VECTOR"),cursor='hand')

        self.imgModel_lbl.pack(side=LEFT, padx=5)
        self.left_Frame.pack(side=LEFT)
        self.right_Frame.pack(side=LEFT)
        self.model_entry.pack(side=TOP)
        self.model_btn.pack(side=TOP, pady=3)
        self.vector_entry.pack(side=TOP)
        self.vector_btn.pack(side=TOP, pady=3)

        # Bottom right menu
        #self.rightBtn_Frame = Frame(self.root, bg='lightblue')
        self.buttonLeft_Frame = Frame(self.root, bg='lightblue')
        self.importModel_btn = Button(self.buttonLeft_Frame, text='Import Model', padx=10,pady=10,
                                      command=lambda: send_event("IMPORT_MODEL"),cursor='hand')
        self.importModel_btn.pack(side=RIGHT)

        self.buttonRight_Frame = Frame(self.root, bg='purple')
        self.startTraining_btn = Button(self.buttonRight_Frame, text='Classify', padx=10,pady=10,
                                        command=lambda: send_event("CLASSIFY"),cursor='hand')
        self.startTraining_btn.pack()

        self.exit_Frame.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)
        self.title_Frame.grid(row=1, column=0, columnspan=3, pady=1, sticky=N+S)
        self.center_Frame.grid(row=2, column=0, columnspan=3, padx=65, sticky=N + S)
        self.unlabeledCenter_Frame.grid(row=3, column=0, columnspan=3, sticky=N+S+W+E)
        #self.unlabeledCenter_Frame.grid(row=2, column=3, sticky=W+E)
        self.selectModel_Frame.grid(row=4, column=0, padx=65, sticky=W)
        #self.rightBtn_Frame.grid()
        self.buttonLeft_Frame.grid(row=4, column=1, padx=65, sticky=E)
        self.buttonRight_Frame.grid(row=4, column=2, padx=65, sticky=E)

        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.root.mainloop()
