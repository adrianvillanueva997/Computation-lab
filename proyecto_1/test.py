from proyecto_1 import File_Manager, Text_Procesing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

if __name__ == '__main__':
    # /home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/
    # /home/xiao/Documents/proyecto_Comp1/dataset_entrenamiento/buenas/
    fm = File_Manager.File_Manager(path='/home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/')
    reviews = fm.extract_data_from_files()
    tp = Text_Procesing.Text_Processing(reviews)
    processed_reviews = tp.process_reviews()
    print(processed_reviews)
    cv = CountVectorizer(tokenizer=None)
    cv.fit(processed_reviews)
    print(cv.vocabulary_)
    encode = cv.transform(processed_reviews)
    print(encode)
    print(type(encode))
    print(encode.toarray())

    tv = TfidfVectorizer()
    tv.fit(processed_reviews)
    vector = tv.transform(processed_reviews)
    print(vector.shape)
    print(vector.toarray())

    vec = HashingVectorizer(n_features=10)
    content = vec.transform(processed_reviews)
    print(content.shape)
    print(content.toarray())

