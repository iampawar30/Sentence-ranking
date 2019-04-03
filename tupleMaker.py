import itertools
def tupleit(s):
    global t
    t=[]
    #names = ['Jack Matthews', 'Mick LaSalle', 'Claudia Puig', 'Lisa Rose', 'Toby', 'Gene Seymour']
    combos = itertools.combinations(s, 2)
    for name1, name2 in combos:
        p=(name1, name2)
        t.append(p)
    t=list(map(list, dict(t).items()))
    t= list(set(map(tuple,t)))
    #print(t)
    return t



#s=" a beverage consisting of an infusion of ground coffee beans he ordered a cup of coffee"
#s=s.split()
#print tupleit(s)
