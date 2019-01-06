import os
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from proyecto_1.ETL import Text_Procesing


class Vectorizer:
    """
    Class that does all the vectorization and generation process of the whole data frame and the test/train slitted data
    """

    def __init__(self, g_reviews=None, b_reviews=None, n_reviews=None, u_reviews=None):
        """
        Class constructor
        """
        self.__data_frame = pd.DataFrame()
        self.__g_reviews = g_reviews
        self.__b_reviews = b_reviews
        self.__n_reviews = n_reviews
        self.__u_reviews = u_reviews
        self.__vectorizer = None

    def __generate_training_dataframe(self):
        """
        Generates and returns a data frame given the previously preprocessed reviews
        :param g_reviews:
        :param b_reviews:
        :param n_reviews:
        """
        data = {
            'reviews': [],
            'labels': []
        }

        for review in self.__g_reviews:
            data['reviews'].append(review)
            data['labels'].append('G')

        for review in self.__b_reviews:
            data['reviews'].append(review)
            data['labels'].append('B')

        for review in self.__n_reviews:
            data['reviews'].append(review)
            data['labels'].append('N')

        self.__data_frame = pd.DataFrame(data)

    def __generate_unlabeled_dataframe(self, file_names):
        data = {
            'file_names': file_names,
            'reviews': [],
            'labels': [],
        }
        for review in self.__u_reviews:
            data['reviews'].append(review)
            data['labels'].append('U')

        self.__data_frame = pd.DataFrame(data)

    def __count_vectorizer_train(self, x_train, x_test):
        """
        Convert a collection of text documents to a matrix of token counts
        :param to_array:
        """
        tp = Text_Procesing.Text_Processing()
        stop_words = set(stopwords.words('spanish'))
        cv = CountVectorizer(tokenizer=tp.tokenizer, stop_words=stop_words)
        cv.fit(x_train)
        x_train = cv.transform(x_train).toarray()
        x_test = cv.transform(x_test).toarray()
        self.__vectorizer = cv
        return x_train, x_test

    def export_vectorizer(self, path, model_name):
        try:
            extension = '.vocab'
            file_name = str(model_name) + str(extension)
            full_path = os.path.join(path, file_name)
            pickle.dump(self.__vectorizer, open(full_path, "wb"))
        except Exception as e:
            print(e)

    def load_vectorizer(self, path):
        try:
            self.__vectorizer = pickle.load(open(path, 'rb'))
        except Exception as e:
            print(e)

    def generate_train_test_data(self, vectorizer, test_size=0.1, random_state=None,
                                 train_size=None):
        """
        Generate train/test data given some vectorized reviews
        :param train_size: represent the proportion of the dataset to include in the test split. (if float, it should be between 0 and 1)
        :param test_size: represent the proportion of the dataset to include in the train split. (if float, it should be between 0 and 1)
        :param random_state: seed used by the random number generator. If it's none it is generated by numpy
        :return: X_train, X_test, y_train, y_test
        """
        self.__generate_training_dataframe()
        x_train, x_test, y_train, y_test = train_test_split(self.__data_frame['reviews'],
                                                            self.__data_frame['labels'],
                                                            test_size=test_size,
                                                            random_state=random_state,
                                                            train_size=train_size)
        if vectorizer == "count_vect":
            x_train, x_test = self.__count_vectorizer_train(x_train=x_train, x_test=x_test)
        elif vectorizer == "tfid":
            x_train, x_test = self.__term_frequency_vectorizer_train(x_train=x_train, x_test=x_test)

        else:
            return None

        return x_train, x_test, y_train, y_test

    def generate_unlabeled_data(self, file_names):
        self.__generate_unlabeled_dataframe(file_names)
        unlabeled_data = self.__vectorizer.transform(self.__data_frame['reviews']).toarray()
        return unlabeled_data

    def update_unlabeled_dataframe(self, predicted_data):
        self.__data_frame['labels'] = predicted_data

    def plot_dataframe(self):
        plot = self.__data_frame['labels'].value_counts().plot('bar')
        plt.show()
        return plot

    def export_dataframe_csv(self):
        self.__data_frame.to_csv('export.csv')
