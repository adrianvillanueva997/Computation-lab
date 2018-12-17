import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from proyecto_1 import File_Manager
import string


class Text_Processing:
    """
    All NLP process is done here
    """

    def __init__(self, reviews):
        """
        Class constructor
        :param reviews:
        """
        self.reviews = reviews

    def __tokenizer(self, reviews):
        """
        Tokenization process, recieves a list of reviews and returns a list with a list of tokens for each review
        :param reviews:
        :return: list
        """
        tokens = []
        for review in reviews:
            token = word_tokenize(text=review)
            tokens.append(token)
        return tokens

    def __filter_stop_words(self, tokens):
        """
        Removal of stop words and punctuation
        :param tokens:
        :return:
        """
        filtered_reviews = []
        stop_words = set(stopwords.words('spanish'))
        for token in tokens:
            for word in token:
                if word not in stop_words and word not in string.punctuation:
                    filtered_reviews.append(word)
        return filtered_reviews

    def __stemmer(self, filtered_reviews):
        """
        Stemmer, must receive a list of filtered reviews, otherwise it won't work as expected
        :param filtered_reviews:
        :return:
        """
        stemmer = nltk.SnowballStemmer('spanish')
        stemmed_reviews = []
        for word in filtered_reviews:
            stemmed_reviews.append(stemmer.stem(word))
        return stemmed_reviews

    def process_reviews(self):
        """
        Public function that does all the NLP process
        :return:
        """
        lower_reviews = [word.lower() for word in self.reviews]
        tokens = self.__tokenizer(lower_reviews)
        filtered_reviews = self.__filter_stop_words(tokens)
        stemmed_reviews = self.__stemmer(filtered_reviews)

        return stemmed_reviews

    def graph_reviews(self):
        """
        Dani didn't want this graph, but it may be useful (or not), returns a frequency word distribution graph
        :return:
        """
        processed_reviews = self.process_reviews()
        fdist = FreqDist(processed_reviews)
        print(fdist)
        fdist.plot(30, cumulative=False)
        return fdist
