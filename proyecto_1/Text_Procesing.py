from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer
import string


class Text_Processing:
    """
    All NLP process is done here
    """

    def __init__(self):
        """
        Class constructor
        """
        self.__reviews = []

    @staticmethod
    def tokenizer(reviews):
        """
        Tokenizing process, receives a list of reviews and returns a list with a list of tokens for each review
        :param reviews:
        :return : list
        """
        stems = []
        token = word_tokenize(text=reviews, language='spanish')
        for item in token:
            stems.append(SnowballStemmer(language='spanish').stem(item))
        return stems

    @staticmethod
    def __filter_stop_words(tokens):
        """
        Removal of stop words and punctuation
        :param tokens:
        :return :list
        """
        filtered_reviews = []
        stop_words = set(stopwords.words('spanish'))
        for token in tokens:
            for word in token:
                if word not in stop_words and word not in string.punctuation:
                    filtered_reviews.append(word)
        return filtered_reviews

    @staticmethod
    def __stemmer(filtered_reviews):
        """
        Stemmer, must receive a list of filtered reviews, otherwise it won't work as expected
        :param filtered_reviews:
        :return:list
        """
        stemmer = SnowballStemmer('spanish')
        stemmed_reviews = []
        for word in filtered_reviews:
            stemmed_reviews.append(stemmer.stem(word))
        return stemmed_reviews

    def process_reviews(self, reviews):
        """
        Public function that does all the NLP process
        :return:list
        """
        self.__reviews = reviews
        lower_reviews = [word.lower() for word in self.__reviews]
        tokens = self.tokenizer(lower_reviews)
        filtered_reviews = self.__filter_stop_words(tokens)
        stemmed_reviews = self.__stemmer(filtered_reviews)

        return stemmed_reviews

    def graph_reviews(self,reviews):
        """
        Dani didn't want this graph, but it may be useful (or not), returns a frequency word distribution graph
        :return: plot
        """
        processed_reviews = self.process_reviews(reviews)
        fdist = FreqDist(processed_reviews)
        print(fdist)
        fdist.plot(30, cumulative=False)
        return fdist

    def transform_data(self, processed_reviews):
        pass
