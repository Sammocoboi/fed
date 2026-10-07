import re
import nltk
from nltk.corpus import stopwords
import heapq
from collections import Counter
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
def get_words_nltk_unique(text):

    words = re.findall(r'[а-яА-ЯёЁa-zA-Z]+', text)
    wowrdslist=[]
    for w in words:
        
        if w.lower() not in russian_stopwords and w.lower() not in wowrdslist:
            wowrdslist.append(w.lower())
        
    return wowrdslist
with open("C:\\Users\\Student\\Desktop\\Пушкин Александр. Капитанская дочка - royallib.com.txt","r") as f:
    words = get_words_nltk(f.read())
    wordsunique=get_words_nltk_unique(f.read())
def topkqent(words,k):
    freq = Counter(words)
    heap = []
    for word,count in freq.items():
        heapq.heappush(heap,(count,word))
        if len(heap)>k:
            heapq.heappop(heap)
    

    n = len(heap)
    for i in range(n):
       
        max_idx = i
        for j in range(i + 1, n):
            if heap[j] > heap[max_idx]:
                max_idx = j
      
        heap[i], heap[max_idx] = heap[max_idx], heap[i]
    return heap

wordscount = topkqent(words,10)
print(wordscount)

with open("C:\\Users\\Student\\Desktop\\Пушкин Александр. Евгений Онегин - royallib.com.txt","r") as f:
    words += get_words_nltk(f.read())
    wordsunique+=get_words_nltk_unique(f.read())

with open("C:\\Users\\Student\\Desktop\\Пушкин Александр. Дубровский - royallib.com.txt","r") as f:
    words += get_words_nltk(f.read())
    wordsunique+=get_words_nltk_unique(f.read())
    
print("вов всех 3 книгах")
wordscount2 = topkqent(words,10)
print(wordscount2)

print("униканльыне слова")
print(wordsunique)
