from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
import stop_words_remover as swr
def defexe(word):
    global defn,exa
    global gloss,temp
    temp=""
    sy=wn.synsets(word)
    w=sy[0]
    defn=w.definition()
    defn=swr.remover(defn)
    exa=w.examples()
    #exa=swr.remover(exa)
    gloss=temp+" "+defn
    for i in range(len(exa)):
        t=swr.remover(exa[i])
        gloss=gloss+" "+t
    return gloss

#print defexe("coffee")
