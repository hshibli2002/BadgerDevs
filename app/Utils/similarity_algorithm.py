from fuzzywuzzy import fuzz


def calculate_similarity(keyword, text):
    return fuzz.token_set_ratio(keyword.lower(), text.lower()) / 100.0  # Scale to 0-1 range
