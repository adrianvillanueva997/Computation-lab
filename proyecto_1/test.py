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

    vectorizer = Vectorizer.Vectorizer()
    df = vectorizer.generate_dataframe(g_processed_reviews, b_processed_reviews, n_processed_reviews)
    vectorized_reviews = vectorizer.count_vectorizer(df)
    X_train, X_test, y_train, y_test = vectorizer.generate_train_test_data(vectorized_reviews)
    models = Models.Models(X_train, y_train, X_test, y_test)
    probability, conf_matrix = models.multinomial_naive_bayes()

    print(probability)
    print(conf_matrix)

    plot = models.generate_plot_learning_curve(title="Learning Curve", X=X_test, y=y_test)
    plot.show()
