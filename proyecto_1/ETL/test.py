from proyecto_1.ETL import Models, Vectorizer, File_Manager

if __name__ == '__main__':
    fm = File_Manager.File_Manager()
    good_reviews = fm.extract_data_from_files('/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/')
    bad_reviews = fm.extract_data_from_files('/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/malas/')
    neutral_reviews = fm.extract_data_from_files(
        '/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/neutras/')
    vectorizer = Vectorizer.Vectorizer(good_reviews, bad_reviews, neutral_reviews)
    x_train, x_test, y_train, y_test = vectorizer.generate_train_test_data(vectorizer='count_vect', to_array=True,
                                                                           test_size=0.1, random_state=None)
    models = Models.Models(x_train, y_train, x_test, y_test)
    models.tree_decision_classifier()
    cross_validation_score, conf_matrix, cross_validation_variance, classification_score = models.generate_classification_model_statistics()
    print(f'Cross Validation score: {cross_validation_score}')
    print(f'Confussion matrix: {conf_matrix}')
    print(f'Cross Validation Variance: {cross_validation_variance}')
    print(f'Classification score: \n{classification_score}')
    plot = models.plot_sklearn_learning_curve(title="Learning Curve", X=x_train, y=y_train)
    plot.show()
    plot = models.plot_confusion_matrix()
    plot.show()
    models.plot_tree_graph()

    models.export_model(path='', model_name='decission_tree')

    models.load_model('test.sav')

    """
    
    x_train, x_test, y_train, y_test, vocabulary_size, maxlen = vectorizer.generate_keras_train_test_data()
    models.keras_sequential_model(vocabulary_size, maxlen)
    X_train, X_test, y_train, y_test = vectorizer.generate_train_test_data(vectorizer='count_vect', to_array=True,
                                                                           test_size=0.1, random_state=None)

    cross_validation_score, conf_matrix, cross_validation_variance, classification_score = models.generate_classification_model_statistics()
    
    #plot = models.plot_sklearn_learning_curve(title="Learning Curve", X=X_train, y=y_train)
    #plot = models.plot_confusion_matrix()
    
    """
