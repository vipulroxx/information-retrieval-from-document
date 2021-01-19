from stemming import Stemming
import math

def calCosine(val1, val2):
    num = det1 = det2 = 0
    for i in range(len(val1)):
        num += val1[i] * val2[i]
        det1 += val1[i] * val1[i]
        det2 += val2[i] * val2[i]
    det1 = math.sqrt(det1)
    det2 = math.sqrt(det2)
    return num / (det1 * det2)

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

def uniqueStemmed(tokenizedList):
    stemmed = []
    stemmer = Stemming()
    for l in tokenizedList:
        for term in l:
            if stemmer.stem(term) not in stemmed:
                stemmed.append(stemmer.stem(term))
    return stemmed

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


D = {}
for i in range(len(stemList)):
    D[i] = stemList[i]
print("\n\nDOCUMENTS")
print("-"*80)
for k, v in D.items():
        print(k, ":", v)
N = len(D)
stemList = uniqueStemmed(stopwordsList)
df = {}
for i in range(len(D)):
    for term in D[i]:
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
for i in range(len(D)):
    temp = {}
    for term in D[i]:
        temp[term] = round(D[i].count(term)/len(D[i]), 4)
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
print("\n\nTF_IDF")
print("-"*80)
printTupleValues(tf_idf)

matrix = []
for i in range(len(D)):
    temp = []
    for j in range(len(stemList)):
        temp.append(0)
    matrix.append(temp)
for i in range(len(matrix)):
    for j in range(len(stemList)):
        if (i, stemList[j]) in tf_idf:
            matrix[i][j] = tf_idf[(i, stemList[j])]

print("\n\nMATRIX")
print(matrix)


queries = ["next step isol candid gene",
           "cell contain gene open dna purifi",
           "chosen gene donor genom well",
           "well studi mai alreadi access genet librari",
           "dna known copi gene avail",
           "isol gene ligat plasmid inser bacterium",
           "genet engin variou applic medicin research"]
originalQueries = queries
queries = [i.split(' ') for i in queries]
print("\n\nTOKENIZED QUERIES")
print(queries)
queryMatrix = []
for i in range(len(queries)):
    temp = []
    for j in range(len(stemList)):
        temp.append(0)
    queryMatrix.append(temp)
tfq = []
for i in range(len(queries)):
    temp = {}
    for term in queries[i]:
        temp[term] = round(queries[i].count(term)/len(queries[i]), 4)
    tfq.append(temp)
print(tfq)
tf_idfq = {}
for i in range(len(tfq)):
    for k,v in tfq[i].items():
        tf_idfq[i, k] = round(v * idf[k], 4)
print("TFIDFQ\n")
print(tf_idfq)
for i in range(len(queryMatrix)):
    for j in range(len(stemList)):
        if (i, stemList[j]) in tf_idfq:
            queryMatrix[i][j] = tf_idfq[(i, stemList[j])]

print("\n\nQUERY MATRIX")
print(queryMatrix)
cosineSimilarity = []
for i in range(len(queryMatrix)):
    temp = []
    for j in range(len(matrix)):
        temp.append(calCosine(queryMatrix[i], matrix[j]))
    cosineSimilarity.append(temp)
print("\n\nCosine similarity")
print(cosineSimilarity)
print("\n\nINFORMATION RETRIEVED FROM TEXT")
for i in range(len(queries)):
    print(originalQueries[i], " matches the document number ", cosineSimilarity[i].index(max(cosineSimilarity[i])))