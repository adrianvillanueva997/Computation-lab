import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from proyecto_1 import File_Manager


class Text_Processing:
    def __init__(self, reviews):
        self.reviews = reviews
        self.tokens = []
        self.filtered_reviews = []
        self.stop_words = set(stopwords.words('spanish'))

    def to_lower(self):
        self.reviews = [word.lower() for word in self.reviews]

    def tokenizer(self):
        for review in self.reviews:
            token = word_tokenize(text=review)
            self.tokens.append(token)

    def filter_stop_words(self):
        for token in self.tokens:
            self.filtered_reviews = [word for word in token if word not in self.stop_words]

    def stemming(self):
        sno = nltk.stem.SnowballStemmer('spanish')
        for token in self.tokens:
            for word in token:
                if word not in self.stop_words:
                    self.filtered_reviews.append(sno.stem(word))


if __name__ == '__main__':
    fm = File_Manager.File_Manager(path=r'/home/xiao/Documents/proyecto_Comp1/dataset_entrenamiento/buenas/')
    reviews = fm.extract_data_from_files()
    tp = Text_Processing(reviews)
    tp.to_lower()
    tp.tokenizer()
    print(tp.tokens)
    tp.filter_stop_words()
    tp.stemming()
    print(tp.filtered_reviews)
