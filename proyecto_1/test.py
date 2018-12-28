from proyecto_1 import File_Manager, Text_Procesing, Vectorizer, Models

if __name__ == '__main__':
    # /home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/
    # /home/xiao/Documents/proyecto_Comp1/dataset_entrenamiento/buenas/
    fm = File_Manager.File_Manager(path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/')
    good_reviews = fm.extract_data_from_files()
    tp = Text_Procesing.Text_Processing(good_reviews)
    g_processed_reviews = tp.process_reviews()
    print(g_processed_reviews)

    fm = File_Manager.File_Manager(path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/malas/')
    bad_reviews = fm.extract_data_from_files()
    tp = Text_Procesing.Text_Processing(bad_reviews)
    b_processed_reviews = tp.process_reviews()
    print(b_processed_reviews)

    fm = File_Manager.File_Manager(path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/neutras/')
    neutral_reviews = fm.extract_data_from_files()
    tp = Text_Procesing.Text_Processing(neutral_reviews)
    n_processed_reviews = tp.process_reviews()
    print(n_processed_reviews)

    vectorizer = Vectorizer.Vectorizer(g_processed_reviews, b_processed_reviews, n_processed_reviews)
    vectorizer.generate_dataframe()
    vectorizer.count_vectorizer(to_array=False)
    X_train, X_test, y_train, y_test = vectorizer.generate_train_test_data()
    models = Models.Models(X_train, y_train, X_test, y_test)
    probability, conf_matrix = models.svm_support_vector_classification()

    print(probability)
    print(conf_matrix)

    plot = models.generate_plot_learning_curve(title="Learning Curve", X=X_train, y=y_train)
    plot.show()
