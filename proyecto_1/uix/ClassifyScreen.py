from tkinter import *

from proyecto_1.uix import MainScreen as MS
from proyecto_1.uix import ClassifyResultsScreen as CRS
from tkinter.filedialog import askdirectory
from proyecto_1.ETL import Models, Vectorizer, File_Manager
from tkinter.filedialog import askdirectory,askopenfilename


class ClassifyScreenController():

    def handle_event(self, window, command, **kwargs):
        if command == "EXIT":
            self.exit(window)
        elif command == "BACK":
            self.goto_previous(window)
        elif command == "EXPORT_TO_FOLDERS":
            pass
        elif command == "EXPORT_TO_CSV":
            pass
        else:
            print("Unrecognized command %s" % command)

    def exit(self, window):
        print("TODO implement exit")

    def goto_previous(self, window):
        window.root.remove_frame()
        MS.MainScreen(window.root)

    def select_path(self, window):
        self.unlabeled_path = askdirectory()
        window.selectPath_entry.delete(0, END)
        window.selectPath_entry.insert(END, self.unlabeled_path)

    def select_model(self, window):
        self.model_path = askopenfilename()
        if str(self.model_path).__contains__('.model'):
            window.model_entry.delete(0, END)
            window.model_entry.insert(END, self.model_path)
        else:
            print("ERROR: Invalid model")

    def select_vocab(self, window):
        self.vocab_path = askopenfilename()
        if str(self.vocab_path).__contains__('.vocab'):
            window.vector_entry.delete(0, END)
            window.vector_entry.insert(END, self.vocab_path)
        else:
            print("ERROR: Invalid vocab")

    def classify(self, window):
        #Check if all three fields are not null
        fm = File_Manager.File_Manager()
        print(self.unlabeled_path)
        unlabeled_reviews, u_file_names = fm.extract_data_from_files(self.unlabeled_path)
        vectorizer = Vectorizer.Vectorizer(u_reviews=unlabeled_reviews)
        vectorizer.load_vectorizer(self.vocab_path)
        x_unlabeled = vectorizer.generate_unlabeled_data(u_file_names)
        model = Models.Models()
        model.load_model(self.model_path)
        prediction = model.predict(x_unlabeled)
        #Prints
        print(prediction)
        vectorizer.update_unlabeled_dataframe(predicted_data=prediction)
        vectorizer.plot_dataframe()
        self.goto_classify_results(window, vectorizer)

    def goto_classify_resutls(self,window,vectorizer):
        window.root.remove_frame()
        CRS.ClassifyResultsScreen(window.root, vectorizer)




class ClassifyScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master

        # back-exit Frame ---------------------------------------------------------------------->
        self.exit_Frame = Frame(self.root, bg='red') ##cbccd1

        self.controller = ClassifyScreenController()

        def send_event(command, **kwargs):
            self.controller.handle_event(self, command, **kwargs)

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

        # center table Frame ------------------------------------------------------------------- >
        self.center_Frame = Frame(self.root, pady=130, bg='#cbccd1')
        self.center_Canvas = Canvas(self.center_Frame, bg='#b8b8b8')
        self.myImgReviews = PhotoImage(file='resources/reviews1.png')
        self.imgReviews_lbl = Label(self.center_Canvas, image=self.myImgReviews)
        self.imgReviews_lbl.config(bg='#b8b8b8')
        self.selectPath_entry = Entry(self.center_Canvas, justify='left')
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

        #self.modelVar.trace('w', self.select_model)
        self.left_Frame = Frame(self.selectModel_Frame)
        self.model_entry = Entry(self.selectModel_Frame, justify='right')
        self.model_btn = Button(self.selectModel_Frame, text='Select Model', padx=10,
                                command=lambda: send_event("SELECT_MODEL"))
        self.right_Frame = Frame(self.selectModel_Frame)
        self.vector_entry = Entry(self.selectModel_Frame, justify='left')
        self.vector_btn = Button(self.selectModel_Frame, text='Select Vocab', padx=10,
                                command=lambda: send_event("SELECT_VOCAB"))

        self.imgModel_lbl.pack(side=LEFT, padx=5)
        self.left_Frame.pack(side=LEFT)
        self.right_Frame.pack(side=LEFT)
        self.model_entry.pack(side=TOP)
        self.model_btn.pack(side=TOP, pady=3)
        self.vector_entry.pack(side=TOP)
        self.vector_btn.pack(side=TOP, pady=3)

        # Bottom right menu
        self.buttonLeft_Frame = Frame(self.root, bg='lightblue')
        self.importModel_btn = Button(self.buttonLeft_Frame, text='Export to Folders', padx=10,pady=10,
                                      command=lambda: send_event("EXPORT_TO_FOLDERS"))
        self.importModel_btn.pack(side=LEFT)

        self.buttonRight_Frame = Frame(self.root, bg='purple')
        self.startTraining_btn = Button(self.buttonRight_Frame, text='Export to CSV', padx=10,pady=10,
                                        command=lambda: send_event("EXPORT_TO_CSV"))
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
