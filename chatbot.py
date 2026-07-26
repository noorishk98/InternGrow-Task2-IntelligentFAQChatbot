import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv("faqs.csv")

questions = df["question"].tolist()
answers = df["answer"].tolist()

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

def get_answer(user_query):
    query_processed = preprocess(user_query)
    query_vector = vectorizer.transform([query_processed])

    similarities = cosine_similarity(query_vector, faq_vectors)

    best_idx = similarities.argmax()
    best_score = similarities[0][best_idx]

    if best_score < 0.3:
        return "Sorry, I couldn't understand your question. Please try again."

    return answers[best_idx]
