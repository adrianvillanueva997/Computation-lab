import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split


class Vectorizer:
    """
    Class that does all the vectorization and generation process of the whole data frame and the test/train slitted data
    """

    def __init__(self, g_reviews, b_reviews, n_reviews):
        """
        Class constructor
        """
        self.__data_frame = pd.DataFrame()
        self.__g_reviews = g_reviews
        self.__b_reviews = b_reviews
        self.__n_reviews = n_reviews
        self.__vectorized_reviews = None

    def generate_dataframe(self):
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
            data['labels'].append(1)

        for review in self.__b_reviews:
            data['reviews'].append(review)
            data['labels'].append(2)

        for review in self.__n_reviews:
            data['reviews'].append(review)
            data['labels'].append(3)

        self.__data_frame = pd.DataFrame(data)

    def count_vectorizer(self, to_array=False):
        """
        Convert a collection of text documents to a matrix of token counts
        :param to_array:
        """
        cv = CountVectorizer()
        vectorized_reviews = cv.fit_transform(self.__data_frame['reviews'])
        if to_array:
            self.__vectorized_reviews = vectorized_reviews.toarray()
        else:
            self.__vectorized_reviews = vectorized_reviews

    def term_frequency_vectorizer(self, to_array=False):
        """
        Convert a collection of text documents to a matrix of token occurrences
        :param to_array:
        """
        tf = TfidfVectorizer()
        vectorized_reviews = tf.fit_transform(self.__data_frame['reviews'])
        if to_array:
            self.__vectorized_reviews = vectorized_reviews.toarray()
        else:
            self.__vectorized_reviews = vectorized_reviews

    def hash_vectorizer(self, to_array=False):
        """
        Convert a collection of raw documents to a matrix of TF-IDF features.
        :param to_array:
        """
        hs = HashingVectorizer()
        vectorized_reviews = hs.fit_transform(self.__data_frame['reviews'])
        if to_array:
            self.__vectorized_reviews = vectorized_reviews.toarray()
        else:
            self.__vectorized_reviews = vectorized_reviews

    def generate_train_test_data(self, test_size=0.1, random_state=None,
                                 train_size=None):
        """
        Generate train/test data given some vectorized reviews
        :param train_size: represent the proportion of the dataset to include in the test split. (if float, it should be between 0 and 1)
        :param test_size: represent the proportion of the dataset to include in the train split. (if float, it should be between 0 and 1)
        :param random_state: seed used by the random number generator. If it's none it is generated by numpy
        :return: X_train, X_test, y_train, y_test
        """
        x_train, x_test, y_train, y_test = train_test_split(self.__vectorized_reviews, self.__data_frame['labels'],
                                                            test_size=test_size,
                                                            random_state=random_state,
                                                            train_size=train_size)

        return x_train, x_test, y_train, y_test
