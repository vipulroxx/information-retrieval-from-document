from stemming import Stemming
import math

def printTupleValues(dict):
    k = 0
    for item in dict:
        s = "(" + str(item[0]) + "," + item[1] + ") : " + str(round(dict[item], 4))
        print(s.ljust(30), end = " ")
        k += 1
        if(k == 5):
            k = 0
            print()

def printTfDictValues(lst):
    k = 0
    for l in lst:
        dict = l
        for item in dict:
            s = item+" : "+str(dict[item])
            print(s.ljust(35),end =" ")
            k+=1
            if(k==5):
                k = 0
                print()

def printDictValues(dict):
    k = 0
    for item in dict:
        s = item + " : " + str(round(dict[item], 4))
        print(s.ljust(30), end = " ")
        k += 1
        if(k == 3):
            k = 0
            print()

def printListOfListValues(lst):
    k = 0
    for l in lst:
        for i in l:
            print(i.ljust(25),end=" ")
            k+=1
            if(k==5):
                k = 0
                print()

def stemmed(tokenizedList):
    stemmed = []
    stemmer = Stemming()
    for l in tokenizedList:
        stemmedList = []
        for term in l:
            stemmedList.append(stemmer.stem(term))
        stemmed.append(stemmedList)
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

def tokenize(line):
    punctuations = [',', '\'', ';', '-', '(', ')', '\\', ' ', '\t', '\n', '.', '[', ']']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = []
    for term in line:
        for i in range(len(term)):
            if term[i] in punctuations or term[i] in numbers:
                term = term.replace(term[i], ' ')
        term = term.strip(" ")
        if term != '':
            term = term.lower()
            term = term.strip()
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
tokenizedList = []
for line in original_words:
    tokenizedList.append(tokenize(line))
printListOfListValues(tokenizedList)
print("\n\nSTOP WORD REMOVAL")
print("-"*80)
stopwordsList = []
for l in tokenizedList:
    stopwordsList.append(stopwords(l))
printListOfListValues(stopwordsList)
print("\n\nSTEMMING")
print("-"*80)
stemList = []
stemList = stemmed(stopwordsList)
printListOfListValues(stemList)
queries = [["next step isol candid gene"],
           ["cell contain gene open DNA purifi"],
           ["chosen gene donor organism genom well"],
           ["well studi mai alreadi access genet librari"],
           ["DNA seqenc known copi gene avail"],
           ["Once isol gene ligat plasmid inser bacterium"],
           ["genet engin variou applic medicin research"]]
documents = [26, 27, 30, 30, 32, 35]

D = {}
for i in range(len(stemList)):
    D[i] = stemList[i]
print("\n\nDOCUMENTS")
print("-"*80)
for k, v in D.items():
        print(k, ":", v)
N = len(D)
df = {}
for i in range(len(stemList)):
    for term in stemList[i]:
        try:
            df[term].add(i)
        except:
            df[term] = {i}
for k,v in df.items():
    df[k] = len(v)
print("\n\nDOCUMENT FREQUENCY")
print("-"*80)
printDictValues(df)
tf = []
for i in range(len(stemList)):
    temp = {}
    for term in stemList[i]:
        temp[term] = round(stemList[i].count(term)/len(stemList[i]), 4)
    tf.append(temp)
print("\n\nTERM FREQUENCY")
print("-"*80)
printTfDictValues(tf)
idf = {}
for k,v in df.items():
    idf[k] = math.log(N/v)
print("\n\nINVERSE DOCUMENT FREQUENCY")
print("-"*80)
printDictValues(idf)
tf_idf = {}
for i in range(len(tf)):
    for k,v in tf[i].items():
        tf_idf[i, k] = round(v * idf[k], 4)
print("-"*80)
print("\n\nTF_IDF")
print("-"*80)
printTupleValues(tf_idf)