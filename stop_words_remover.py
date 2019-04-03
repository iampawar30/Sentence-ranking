from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
#from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet

def remover(stop):
    stopWords = set(stopwords.words('english')+list(punctuation))
    tempsyn=word_tokenize(stop.lower())
    tempsyn= [word for word in tempsyn if word not in stopWords]
    tempsyn=' '.join(tempsyn)
    #words = stop.split()
    #stop=" ".join(sorted(set(words), key=words.index))
    #print(stop)
    return tempsyn


def createInput(lines):
    global finInput
    for i in range(len(lines)):
        temp=remover(lines[i])
        finInput.append(temp)


lines = [line.rstrip('\n') for line in open('Input.txt')]
finInput=[]


createInput(lines)

print(finInput)
#print(lines)


#print remover("a the is coffee is hot  drink may be")
