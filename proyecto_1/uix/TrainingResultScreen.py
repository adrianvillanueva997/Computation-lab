from tkinter import *

from proyecto_1.uix import MainScreen as MS
from proyecto_1.uix import TrainScreen as TS


class TrainingResultScreenController():

    def handle_event(self, window, command, **kwargs):
        if command == "EXIT":
            self.exit(window)
        elif command == "BACK":
            self.goto_previous(window)
        elif command == "RETURN_TO_MENU":
            self.goto_main_menu(window)
        elif command == "SAVE_MODEL":
            self.save_model()
        else:
            print("Unrecognized command %s" % command)

    def exit(self, window):
        print("TODO implement exit")

    def goto_previous(self, window):
        window.root.remove_frame()
        TS.TrainScreen(window.root)

    def goto_main_menu(self, window):
        window.root.remove_frame()
        MS.MainScreen(window.root)

    def save_model(self):
        print("TODO implement save_model")


class TrainingResultScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master

        self.exit_Frame = Frame(self.root, padx=10, pady=10, bg='#cbccd1')

        self.controller = TrainingResultScreenController()

        def send_event(command):
            self.controller.handle_event(self, command)

        self.exit_btn = Button(self.exit_Frame, text='Exit', padx=5, pady=5, command=lambda: send_event("EXIT"))
        self.back_btn = Button(self.exit_Frame, text='Back', padx=5, pady=5, command=lambda: send_event("BACK"))
        self.exit_btn.pack(side='right', fill="both", expand=True)
        self.back_btn.pack(side='right', fill="both", expand=True)

        # some title Frame --------------------------------------------------------------------->
        self.title_Frame = Frame(self.root)
        self.someTitle_lbl = Label(self.title_Frame, text='Training Results', bg='#cbccd1')
        self.someTitle_lbl.config(font=("Courier", 34))
        self.someTitle_lbl.pack()

        # center table Frame ------------------------------------------------------------------->
        self.center_Frame = Frame(self.root, pady=75, bg='#cbccd1')
        self.confusionMatrix_btn = Button(self.center_Frame, text='Confusion Matrix', bg='#cbccd1',
                                          command=lambda: send_event("EMPTY"))
        self.confusionMatrix_btn.config(font=("Courier", 18))
        self.dataSpace_text = Text(self.center_Frame)
        self.confusionMatrix_btn.pack(side=TOP, anchor='nw', pady=5)
        self.dataSpace_text.pack(side=TOP)

        # Bottom left menu
        self.returnMenu_Frame = Frame(self.root, pady=15, bg='#cbccd1')
        self.returnMenu_btn = Button(self.returnMenu_Frame, text='Return to Menu', padx=10,
                                     command=lambda: send_event("RETURN_TO_MENU"))
        self.returnMenu_btn.pack(side=LEFT, padx=10)

        # Bottom right menu
        self.saveModel_Frame = Frame(self.root, pady=15, bg='#cbccd1')
        self.saveModel_btn = Button(self.saveModel_Frame, text='Return to Menu', padx=10,
                                    command=lambda: send_event("SAVE_MODEL"))
        self.saveModel_btn.pack(side=RIGHT, padx=10)

        self.exit_Frame.grid(row=0, column=0, columnspan=2, sticky=E)
        self.title_Frame.grid(row=1, column=0, columnspan=2, pady=68, sticky=N + S)
        self.center_Frame.grid(row=2, column=0, columnspan=2, padx=65, sticky=N + S)
        self.returnMenu_Frame.grid(row=3, column=0, padx=65, sticky=W)
        self.saveModel_Frame.grid(row=3, column=1, padx=65, sticky=E)

        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.root.mainloop()
