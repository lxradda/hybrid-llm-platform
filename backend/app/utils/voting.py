from collections import Counter

def majority_vote(answers):
    """
    LLM cevapları arasında çoğunluk oyu ile en çok verilen cevabı ve güven skorunu döndürür.
    """
    counter = Counter(answers)
    most_common, count = counter.most_common(1)[0]
    confidence = count / len(answers)
    return most_common, confidence