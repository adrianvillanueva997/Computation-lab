from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, learning_curve, ShuffleSplit
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from proyecto_1 import File_Manager, Text_Procesing
import pandas as pd
from sklearn.metrics import confusion_matrix
from scikit_testing import plotter

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

    data = {
        'reviews': [],
        'label': [],
    }
    for review in g_processed_reviews:
        data['reviews'].append(review)
        data['label'].append(1)

    for review in b_processed_reviews:
        data['reviews'].append(review)
        data['label'].append(2)

    for review in n_processed_reviews:
        data['reviews'].append(review)
        data['label'].append(3)

    df = pd.DataFrame(data)

    print(df)
    print(df.shape)
    count_vectorizer = CountVectorizer()
    vectorized_reviews = count_vectorizer.fit_transform(data['reviews'])
    transformer = TfidfTransformer().fit(vectorized_reviews)
    counts = transformer.transform(vectorized_reviews)
    X_train, X_test, y_train, y_test = train_test_split(vectorized_reviews, data['label'], test_size=0.1,
                                                        random_state=10)

    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)
    model = MultinomialNB(alpha=0.01)
    model.fit(X_train, y_train)
    print(model)

    predicted = model.predict(X_test)

    print(np.mean(predicted == y_test))
    print(confusion_matrix(y_test, predicted))

    cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
    title = 'learning curve'
    curve = learning_curve(model, X_train, y_train)

    a = plotter.plot_learning_curve(model, 'Learning curve', X_test, y_test, cv=cv, n_jobs=4, ylim=(0, 1))
    a.show()
