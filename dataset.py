import defexample as df
import tupleMaker as tm
import sys
import stop_words_remover
def datasetter(q):
    global data_set
    #print(q)
    for i in range(len(q)):
        try:
            p=df.defexe(q[i])
            data_set.append(p)
        except:
            pass

def traindata(data_set):
    global train
    for i in range(len(data_set)):
        q=data_set[i]
        temp=tm.tupleit(q.split())
        train.append(temp)


def removeme(lst):
    for i in range(len(lst)):
        if(lst[i][0]!=lst[i][1]):
            new_train.append(lst[i])

def remove_duplicates(train):
    for i in range(len(train)):
        removeme(train[i])


def check(p,q):
    if(p[0]==q[0] and p[1]==q[1]):
        return 1
    else:
        return 0

def call(a,b):
    global temp,c
    f = open('outputFile.txt', 'w')
    for i in range(len(a)):
        for j in range(len(b)):
            p=0
            p=check(a[i],b[j])
            c=c+p

def ranker(new_train):
    global count,temp,c
    for i in range(1,len(new_train)):
        #for j in range(i+1,len(new_train)):
        count+=1
        call(new_train[0],new_train[i])
        #temp=c
    #return temp
'''def outputFile():
    global c
    f = open('outputFile.txt', 'w')
    global t,train,new_train,count
    t=0
    for i in range(len(stop_words_remover.finInput)):
        datasetter(stop_words_remover.finInput[i].split())
        traindata(data_set)
        remove_duplicates(train)
        ranker(new_train)
        print(c)
        c=0
        train=[]
        new_train=[]
        #try:
        #    t=c
        #except:
        #    pass
        #f.write(stop_words_remover.finInput[i])
        #print(t)
        #f.write(str(t))
        #f.write("\n")
        #count=0

    f.close()
'''


query=sys.argv[1]
#query_checker(query)
data_set=[]
train=[]
count=0
temp=0
c=0
new_train=[]
#outputFile()
q=query.split()
datasetter(q)
traindata(data_set)
#print(train[0])
remove_duplicates(train)
ranker(new_train)
t=count/c
print(t)
#print(new_train)
#print(data_set)

