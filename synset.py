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



