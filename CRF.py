data = [(['Linux', 'is', 'the', 'best', 'OS'], ['OS','IR','IR','IR','IR']),

(['Ubuntu', 'is', 'my', 'favourite', 'OS'], ['OS','IR','IR','IR','IR'])]

corpus = []

for (doc, tags) in data:

    doc_tag = []

    for word, tag in zip(doc,tags):

        doc_tag.append((word, tag))

    corpus.append(doc_tag)

def doc2features(doc, i):

    word = doc[i][0]

    

    # Features from current word

    features={

        'word.word': word,

    }

    # Features from previous word

    if i > 0:

        prevword = doc[i-1][0]

        features['word.prevword'] = prevword

    else:

        features['BOS'] = True # Special "Beginning of Sequence" tag

        

    # Features from next word

    if i < len(doc)-1:

        nextword = doc[i+1][0]

        features['word.nextword'] = nextword

    else:

        features['EOS'] = True # Special "End of Sequence" tag

    return features

 

def extract_features(doc):

    return [doc2features(doc, i) for i in range(len(doc))]

 

X = [extract_features(doc) for doc in corpus]

print(X)




doc = '''Andrew Yan-Tak Ng is a Chinese American computer scientist.

He is the former chief scientist at Baidu, where he led the company's

Artificial Intelligence Group. He is an adjunct professor (formerly 

associate professor) at Stanford University. Ng is also the co-founder

and chairman at Coursera, an online education platform. Andrew was born

in the UK in 1976. His parents were both from Hong Kong.'''
doc2features(doc,0)
