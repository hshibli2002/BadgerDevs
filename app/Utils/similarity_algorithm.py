"""Summary:
In this snippet, we are defining a utility function that calculates the cosine similarity between
a keyword and a text using the TF-IDF algorithm.
The function takes a keyword and a text as input, computes the TF-IDF vectors for both, and then
calculates the cosine similarity between them.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_cosine_similarity(keyword, text):
    """
    Calculate the cosine similarity between a keyword and a text using the TF-IDF algorithm.

    :param keyword: The keyword to compare.
    :param text: The text to compare.

    :return: The cosine similarity between the keyword and the text.
    """
    documents = [keyword, text]
    tfidf_vectorizer = TfidfVectorizer().fit_transform(documents)
    similarity = cosine_similarity(tfidf_vectorizer)[0, 1]
    return similarity
