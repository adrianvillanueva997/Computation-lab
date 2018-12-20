from proyecto_1 import File_Manager, Text_Procesing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    # /home/xiao/datasets/proyecto_computacion/dataset_entrenamiento/buenas/
    # /home/xiao/Documents/proyecto_Comp1/dataset_entrenamiento/buenas/
    fm = File_Manager.File_Manager(path='/home/xiao/Documents/proyecto_Comp1/dataset_entrenamiento/buenas/')
    reviews = fm.extract_data_from_files()
    tp = Text_Procesing.Text_Processing(reviews)
    processed_reviews = tp.process_reviews()
    print(processed_reviews)

    names = ['text', 'label']
    df = pd.DataFrame(columns=names)

    df = df.append(pd.DataFrame(processed_reviews, columns=['text']), sort=False)
    for col in df.columns():
        df.loc[df[col] == 'label', col] = 0
    print(df)

"""
cv = CountVectorizer(tokenizer=None, stop_words=None)
    cv.fit(processed_reviews)
    print(cv.vocabulary_)
    encode = cv.transform(processed_reviews)
    print(encode)
    print(type(encode))
    data = encode.toarray()
    X_train, X_test, y_train, y_test = train_test_split(data, 1, test_size=0.1, random_state=69)
    print(X_test)
tv = TfidfVectorizer()
    tv.fit(processed_reviews)
    vector = tv.transform(processed_reviews)
    print(vector.shape)
    print(vector.toarray())

    vec = HashingVectorizer(n_features=10)
    content = vec.transform(processed_reviews)
    print(content.shape)
    print(content.toarray())
    


X = ['the food was really delicious', 'the food was really terrible']

y = [5, 2]
x_data = CountVectorizer().fit_transform(X)
gnb = GaussianNB()
a = gnb.fit(x_data.toarray(), y)
print(a)

Z = ['the food was awesome', 'the food was pretty bad']
z_data = CountVectorizer().fit_transform(Z)
gnb.fit(z_data.toarray(), y)
b = gnb.predict(z_data.toarray())
print(b)
c = gnb.predict_proba(z_data.toarray())
print(c)


"""
