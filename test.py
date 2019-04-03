from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
#from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    #if tag.startswith('V'):
        return 'v'

    #if tag.startswith('J'):
    #    return 'a'

    #if tag.startswith('R'):
        return 'r'

    return None

def tagged_to_synset(word, tag):
    wn_tag= penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None

def sentence_similarity(sentence1, sentence2,i):
    stopWords = set(stopwords.words('english')+list(punctuation))
    tempsyn=word_tokenize(sentence2.lower())
    tempsyn= [word for word in tempsyn if word not in stopWords]
    words = sentence2.split()
    sentence2=" ".join(sorted(set(words), key=words.index))
    #print(sentence2)
    #print(sentence1)
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(sentence2)

    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    #print("synsets")
    print(synsets1)
    print(synsets2)




sentences = [
    "coffee is hot drink made from bevrage",
    "Coffee is flying in the sky",
    "coffee driving the car"
    ]

focus_sentence ="coffee "

i=0
for r in sentences:
    sentence_similarity(focus_sentence,r,i)
    i+=1
    print
