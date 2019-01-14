from tkinter import *

from proyecto_1.uix import MainScreen as MS


class ClassifyScreenController():

    def handle_event(self, window, command, **kwargs):
        if command == "EXIT":
            self.exit(window)
        elif command == "BACK":
            self.goto_previous(window)
        elif command == "SELECT_PATH":
            self.select_path()
        elif command == "SELECT_MODEL":
            self.select_model()
        elif command == "IMPORT_MODEL":
            self.import_model()
        elif command == "CLASSIFY":
            self.classify()
        else:
            print("Unrecognized command %s" % command)

    def exit(self, window):
        print("TODO implement exit")

    def goto_previous(self, window):
        window.root.remove_frame()
        MS.MainScreen(window.root)

    def select_path(self):
        print("TODO implement select_path")

    def select_model(self):
        print("TODO implement select_model")

    def import_model(self):
        print("TODO implement import_model")

    def classify(self):
        print("TODO implement classify")


class ClassifyScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master

        # back-exit Frame ---------------------------------------------------------------------->
        self.exit_Frame = Frame(self.root, bg='red') ##cbccd1

        self.controller = ClassifyScreenController()

        def send_event(command):
            self.controller.handle_event(self, command)

        self.exitButtons_Frame = Frame(self.exit_Frame, bg='pink')
        self.exit_btn = Button(self.exitButtons_Frame, text='Exit', padx=5, pady=15, command=lambda: send_event("EXIT"))
        self.back_btn = Button(self.exitButtons_Frame, text='Back', padx=5, pady=15, command=lambda: send_event("BACK"))
        self.exitButtons_Frame.pack(side='right')
        self.exit_btn.pack(side='right', fill="both", expand=True)
        self.back_btn.pack(side='right', fill="both", expand=True)

        # some title Frame --------------------------------------------------------------------->
        self.title_Frame = Frame(self.root)
        self.someTitle_lbl = Label(self.title_Frame, text='Select Data and Model', bg='blue')
        self.someTitle_lbl.config(font=("Courier", 34))
        self.someTitle_lbl.pack()

        # center table Frame ------------------------------------------------------------------->
        self.center_Frame = Frame(self.root, pady=130, bg='green')
        self.center_Canvas = Canvas(self.center_Frame, bg='#b8b8b8')
        self.myImgReviews = PhotoImage(file='resources/reviews1.png')
        self.imgReviews_lbl = Label(self.center_Canvas, image=self.myImgReviews)
        self.imgReviews_lbl.config(bg='#b8b8b8')
        self.selectPath_entry = Entry(self.center_Canvas, justify='right')
        self.selectPath_btn = Button(self.center_Canvas, text='Select Path', command=lambda: send_event("SELECT_PATH"))
        self.center_Canvas.pack()
        self.imgReviews_lbl.pack(side=LEFT, padx=15, pady=15)
        self.selectPath_entry.pack(side=LEFT, padx=5)
        self.selectPath_btn.pack(side=LEFT, padx=15)

        # Unlabeled path Frame ------------------------------------------------------------------->
        self.unlabeledCenter_Frame = Frame(self.root, bg='pink')


        # Bottom left menu ------------------------------------------------------------------->
        self.selectModel_Frame = Frame(self.root, pady=15, bg='orange')
        self.myImgModel = PhotoImage(file='resources/selectModel.png')
        self.imgModel_lbl = Label(self.selectModel_Frame, image=self.myImgModel)
        self.left_Frame = Frame(self.selectModel_Frame)
        self.model_entry = Entry(self.selectModel_Frame, justify='left')
        self.model_btn = Button(self.selectModel_Frame, text='Select Model', padx=10,
                                command=lambda: send_event("SELECT_MODEL"))
        self.right_Frame = Frame(self.selectModel_Frame)
        self.vector_entry = Entry(self.selectModel_Frame, justify='left')
        self.vector_btn = Button(self.selectModel_Frame, text='Select Vector', padx=10,
                                command=lambda: send_event("SELECT_MODEL"))

        self.imgModel_lbl.pack(side=LEFT, padx=5)
        self.left_Frame.pack(side=LEFT)
        self.right_Frame.pack(side=LEFT)
        self.model_entry.pack(side=TOP)
        self.model_btn.pack(side=TOP, pady=3)
        self.vector_entry.pack(side=TOP)
        self.vector_btn.pack(side=TOP, pady=3)

        # Bottom right menu
        self.buttonLeft_Frame = Frame(self.root, bg='lightblue')
        self.importModel_btn = Button(self.buttonLeft_Frame, text='Import Model', padx=10,pady=10,
                                      command=lambda: send_event("IMPORT_MODEL"))
        self.importModel_btn.pack(side=LEFT)

        self.buttonRight_Frame = Frame(self.root, bg='purple')
        self.startTraining_btn = Button(self.buttonRight_Frame, text='Classify', padx=10,pady=10,
                                        command=lambda: send_event("CLASSIFY"))
        self.startTraining_btn.pack()

        self.exit_Frame.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)
        self.title_Frame.grid(row=1, column=0, columnspan=3, pady=95, sticky=N+S)
        self.center_Frame.grid(row=2, column=0, columnspan=2, padx=65, sticky=N + S)
        self.unlabeledCenter_Frame.grid(row=2, column=3, sticky=W+E)
        self.selectModel_Frame.grid(row=3, column=0, padx=65, sticky=W)
        self.buttonLeft_Frame.grid(row=3, column=1, padx=65, sticky=E)
        self.buttonRight_Frame.grid(row=3, column=2, padx=65, sticky=E)

        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.root.mainloop()
