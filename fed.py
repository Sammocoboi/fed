# Куча
# приоритетная очередь достать минимум за O(nlong)
# для топ K - не сортируем весь массив держим кучу размера K

# heaprq python - мин куча на вершине самый маленький

#K наибольший в [3,2,1,5,6,4] k = 2 ответ ()

# import heapq 
# def kthlargest(array,k):
#     heap = array[:k]
#     heapq.heapify(heap)
#     for value in array[k:]:
#         if value > heap[0]:
#             heapq.heapreplace(heap,value)

#     return heap[0]
# print(kthlargest([3,2,1,5,6,4],2))
# Шаги как работает 
# [3,2,1,5,6,4]
# 1 - берем первый k = [3,2] после heapify вершина 2
# куча - два  прендентенда  на топ 2
# 2 - 1 не больше 2 - выкидываем 
# 3 - 5 > 2 двойка отпадает остатся [3,5] 
# 4 - 6 > 3 тройка выпадет куча [5,6]
# 5 - 4 меньше 5 чётвёрка вылетает остается [5,6]

# в куче два самых больших элемента [5,6] вершина наименьший из них
# время O(nlog k) опять (k) полная сортировка была бы 0(nlong)

# когда брать топ-K,слить K-списков 
# мединана потока, Дейкстра
# Когда не брать нужен весь отсортированный ряд тогда sorted


# индес 0 1 2 3 4 5
# значения 1 2 4 5 3 6

# слово K не часть кучи это размер K самых больших 
# k по величене 
# K кратчайший пусть 
# Куча нужна потому что чтоб достать миним или заменить его стоит O(logK)
# а не O(k)

# [3,2,1,5,6,4] 
# второй по величине 5 первый 6 
# сортировка даст ответ за O(nlogn)
# Куча рамзер K за O(nlonk) при k=2 и милионе чисел это важно
# идея в min-heap держим k самых больших из уже увиденных 
# корень самый маленький из k тоесть текущий k

# почему min-heap хотя ищем большее 
# корень min-heap худший из сохранённых 
# его сравниваем с новым его и выкидываем 
# Max-heap так не умеет максимум выкидывать каждый раз не надо 
# heapreplace - снять корень и положить новое одной операцией O(logk)

# в пустую min-heap по очереи кладут 5,1,4,2 k = 3 что в в корне после каждой встаквки 

# print(kthlargest([5,1,4,2],3))
# import heapq
# heap = []

# for value in (5,1,4,2):
#     heapq.heappush(heap,value)
#     print(heap[0])

# first_out = heapq.heappop(heap)

# третий по величине в [7,1,5,3,6,4]
# корень худший из трёх тоесть сам третий
# корень худший из трёх тоесть сам третий 


# [2,2,2,2] k=1 
# прив всех равных k по величне равен этому числу 
# > в условии специально строгое рвеный корень менять незачем

#words = "abacba" k=2

# топ k самых чатсых 



#сначала словарь частот O(n) потом min-heap размера k по частям
# в конце куча содержит k самых частых но в 
# порядке от меньшей частоты к большей для ответа 
# обычно разворачивают 

# частоты повторий - это словарь отвер k - куча размера k
# время O(nlonk)

import heapq
from collections import Counter

def topkqent(words,k):
    freq = Counter(words)
    # min-heap (частота слов) размер не больше k
    heap = []
    for word,count in freq.items():
        heapq.heappush(heap,(count,word))
        if len(heap)>k:
            heapq.heappop(heap)
    sortheap = []

    n = len(heap)
    for i in range(n):
       
        max_idx = i
        for j in range(i + 1, n):
            if heap[j] > heap[max_idx]:
                max_idx = j
      
        heap[i], heap[max_idx] = heap[max_idx], heap[i]
    return heap
           
    




def topSplit(words):
    wordssplit = list(words)
    return wordssplit

storj = "abacba"
word = topSplit(storj)

print(topkqent(word,2))