from nltk.corpus import wordnet as wn
def polysemys(word):
    global poly
    #poly=(wn.synsets(word, pos='n'))
    k = wn.synsets(word)[0]
    poly=k.hypernyms()[0].hyponyms()
    print(poly)

def hyponyms(word):
    global hypo
    s = wn.synsets(word)[0]
    hypo=s.hypernyms()[0].hyponyms()
    print(hypo)


def ranksense(sense1,sense2):
    global ashrank
    #ashrank+=sense1.wup_similarity(sense2)
    if(sense1.lemma_names()[0]==sense2.lemma_names()[0]):
        ashrank=ashrank+0.5


def main():
    global ashrank
    ashrank=0
    #for i in range(len(hypo)):
    #    for j in range(len(hypo)):
    #        ranksense(hypo[i],hypo[j])
    for i in range(len(hypo)):
        for j in range(len(poly)):
            ranksense(hypo[i],poly[j])


#print(poly[0],hypo[0])
#if(poly[0].lemma_names()[0]==hypo[0].lemma_names().[0]):
#    print("True")
#else:
#    print("False")

polysemys("fast")
hyponyms("coffee")
main()
print("<+>",poly[0],hypo[0])
print("sentence Rnak is ",ashrank)
