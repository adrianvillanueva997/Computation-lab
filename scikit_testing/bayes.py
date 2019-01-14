from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB

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
