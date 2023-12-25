import nltk
nltk.download('all')
import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import json

text = "Огород — участок земли, огороженный.забором и предназначенный для выращивания овощей."

def get_tokenized_words(text):
    words = word_tokenize(text, language = "russian")
    stop_words = stopwords.words("russian")
    filtered_words = list(filter(lambda word: word not in stop_words, words))
    return filtered_words

def lemmatize(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    return lemmatized_words


def get_stemmed_words(words_list) :
    stemmer = SnowballStemmer(language = "russian")
    stemmed_words = []
    for word in words_list:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words

def mark_words(words):
    marked_words = pos_tag(words, lang='rus')
    return marked_words

def write_in_json(content, path):
    words_in_json = json.dumps(content, ensure_ascii=False)
    json_file = open(path, "w")
    json_file.write(words_in_json)
    json_file.close()

def pipeline(text):
    tokenized_words = get_tokenized_words(text)
    lemmatized_words = lemmatize(tokenized_words)
    stemmed_words = get_stemmed_words(lemmatized_words)
    marked_words = mark_words(stemmed_words)
    print(marked_words)
    write_in_json(marked_words, "venv/words.json")

pipeline(text)