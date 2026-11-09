
import re
import nltk
from nltk.corpus import stopwords
import heapq
from collections import deque,defaultdict
nltk.download('stopwords', quiet=True)
russian_stopwords = set(stopwords.words('russian'))
russian_stopwords.update(['это'])
words = []
wordsunique=[]
wordsiskl=[]
def get_words_nltk(text):

    words = re.findall(r'[а-яА-ЯёЁa-zA-Z]+', text)
    wowrdslist=[]
    for w in words:
        
        if w.lower() not in russian_stopwords:
            wowrdslist.append(w.lower())
        
    return wowrdslist
def group_anagrams(array):
    group = {}
    for word in array:
        
        key = "".join(sorted(word))
        group.setdefault(key,set())
        group[key].add(word)
        
    
        


    return group

with open("C:\\Users\\Student\\Desktop\\Пушкин Александр. Евгений Онегин - royallib.com.txt","r") as f:
    text = f.read()
    words = get_words_nltk(text)
    print(group_anagrams(words))

print(group_anagrams(['кот','ток']))