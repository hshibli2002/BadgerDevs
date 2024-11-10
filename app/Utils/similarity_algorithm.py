from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_cosine_similarity(keyword, text):
    documents = [keyword, text]
    tfidf_vectorizer = TfidfVectorizer().fit_transform(documents)
    similarity = cosine_similarity(tfidf_vectorizer)[0, 1]
    return similarity
