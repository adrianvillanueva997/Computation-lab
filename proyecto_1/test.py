from proyecto_1 import File_Manager, Text_Procesing, Vectorizer, Models

if __name__ == '__main__':
    fm = File_Manager.File_Manager(
        path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/')
    good_reviews = fm.extract_data_from_files()

    fm = File_Manager.File_Manager(
        path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/malas/')
    bad_reviews = fm.extract_data_from_files()

    fm = File_Manager.File_Manager(
        path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/neutras/')
    neutral_reviews = fm.extract_data_from_files()

    vectorizer = Vectorizer.Vectorizer(good_reviews, bad_reviews, neutral_reviews)
    X_train, X_test, y_train, y_test = vectorizer.generate_train_test_data(vectorizer='count_vect', to_array=True,
                                                                           test_size=0.1, random_state=None)

    models = Models.Models(X_train, y_train, X_test, y_test)
    models.naive_bayes_multinomial()
    score, conf_matrix = models.generate_model_stadistics()
    print(score)
    print(conf_matrix)
    plot = models.plot_sklearn_learning_curve(title="Learning Curve", X=X_train, y=y_train)
    plot.show()

    plot = models.plot_confusion_matrix()
    plot.show()

