from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split

cv = CountVectorizer(tokenizer=None, stop_words=None)
cv.fit(processed_reviews)
print(cv.vocabulary_)
encode = cv.transform(processed_reviews)
print(encode)
print(type(encode))
data = encode.toarray()

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

# split
X_train, X_test, y_train, y_test = train_test_split(data, 1, test_size=0.1, random_state=69)
