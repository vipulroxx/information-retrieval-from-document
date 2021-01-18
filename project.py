from stemming import Stemming
https://github.com/mayank408/TFIDF/blob/master/TFIDF.ipynb
def stemmed(stopwords):
    stemmed = []
    stemmer = Stemming()
    for term in stopwords:
        stemmed.append(stemmer.stem(term))
    return stemmed

def stopwords(tokenized):
    stop_words_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 
                   'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 
                   'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
                  'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 
                  'o', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
                  'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
                  'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
                  'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
                  'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
                  'very', 'can', 'will', 'just', 'don', 's', 't', 'should', 'now']
    stop_words = []
    for term in tokenized:
        if term not in stop_words_list:
            stop_words.append(term)
    return stop_words

def tokenize(original_words):
    punctuations = [',', ';', '-', '(', ')', '\\', ' ', '\t', '\n', '.', '[', ']']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = []
    for line in original_words:
        for term in line:
            for i in range(len(term)):
                if term[i] in punctuations or term[i] in numbers:
                    term = term.replace(term[i], ' ')
            term = term.strip(" ")
            if term != '':
                words.append(term)
    return words

file = open("doc.txt", "r")
lines = file.readlines()
original_words = []
for line in lines:
    line = line.strip("\n")
    line = line.strip("\t")
    original_words.append(line.split(' '))
print("\nTOKENIZATION")
print("-"*80)
tokenized = tokenize(original_words)
print(tokenized)
print("\nSTOP WORD REMOVAL")
print("-"*80)
stopwords = stopwords(tokenized)
print(stopwords)
print("\nSTEMMING")
print("-"*80)
stemmed = stemmed(stopwords)
print(stemmed)