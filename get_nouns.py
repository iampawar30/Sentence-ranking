import nltk

def get_nouns(lines):
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(lines)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    print nouns



lines = 'coffee is hot drink'
# function to test if something is a noun
get_nouns(lines)
