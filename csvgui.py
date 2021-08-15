import csv
import nltk
import numpy as np
import random
import string
#import jellyfish
import warnings
warnings.filterwarnings("ignore")
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
nltk.download('punkt') 
nltk.download('wordnet')
porter = PorterStemmer()
lancaster=LancasterStemmer()
snowball = SnowballStemmer("english")
"""
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    for token in tokens:
        lemmer.lemmatize(token)
    return [tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))"""
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def Port(tokens):
    m=[]
    for word in tokens:
        m.append(snowball.stem(word))
    return(m)
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
def response(ur):
    
    bs=0
    
    for i in range (0,csvreader.line_num-1):
        x=ur
        synonyms = []
        flag=0
        y=rows[i]
        #print(x)
        X = x.lower().translate(remove_punct_dict)
        #print(X)
        Y = y.lower().translate(remove_punct_dict)
        X_list = word_tokenize(X) 
        Y_list = word_tokenize(Y)
        sw = stopwords.words('english') 
        l1 =[];l2 =[]
        #print("xl,yl",X_list,Y_list)
        X_set = X_list
        Y_set = Y_list
        X_set = {w for w in X_list if not w in sw} 
        Y_set = {w for w in Y_list if not w in sw}
        
        V_set = {w for w in X_set if not w in Y_set}
        #print(V_set)
        #print(X_set,Y_set)
        #print("vset",V_set)
        X_set=set(Port(X_set))
        Y_set=set(Port(Y_set))
        #print("after stemming")
        #print(X_set,Y_set)
        for x in V_set:
            #print(x)
            for syn in wordnet.synsets(x):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            #print(synonyms)
            #print(Y_set)
        for x in synonyms:
            for y in Y_set:
                if(x==y):
                    X_set.add(y)
                    flag = flag+1;
        
                
        
        #print(flag)
        #print(X_set,Y_set)
        rvector = X_set.union(Y_set)
        #print(rvector)
        for w in rvector:
            if w in X_set: l1.append(1)
            else: l1.append(0)
            if w in Y_set: l2.append(1)
            else: l2.append(0)
        #print(l1)
        #print(l2)
        """for mm in range (flag):
            if(1 in l1):
                l1.remove(1)
            if(0 in l2):
                l2.remove(0) """
            
        c = 0
        #print(l1)
        #print(l2)
        for j in range(len(l1)):
            c+= l1[j]*l2[j]
            cosine = c / float((sum(l1)*sum(l2))**0.5)
        #print("similarity: ", cosine)
        if(cosine>bs):
            bs =cosine
            val=i
    if(bs!=0.0):
        #print(rows[val])
        return(rows1[val])
        #print("Do you need further explanation press 1")
        x= (input())
        if(x=='1'):
            print(rows2[val])
    else:
        return("Sorryy, I don't understand you")
    return

        
        
filename = "NLP.csv"
fields = [] 
rows = []
rows1 =[]
rows2=[]
ur = "xx"
with open("NLP.csv", encoding = "cp850" ) as csvfile: 
    csvreader = csv.reader(csvfile) 
    fields = next(csvreader)
    for row in csvreader: 
        rows.append(row[0])
        rows1.append(row[1])
        rows2.append(row[2])
    #print(rows)
"""
print("Helloo!!, Please enter your queries and 0 to exit")
while (ur!= "0"):
    ur = input()
    if(ur!="0"):
        
        ur = ur.lower()
        #print(ur)
        ans = response(ur)
    else:
        print("Okayyy byee...")"""
#jellyfish.jaro_distance(x, y)>0.8



      
    
