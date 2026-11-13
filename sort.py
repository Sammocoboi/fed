# есть список из 8 милионов целых чисел в диапозоне от 0 до 999999 какой тип сортировки вам подойдёт
import random
import time
from collections import Counter
list_qwe=[]
for i in  range(8_000_000):
    list_qwe.append(random.randint(0,999999))
start_time= time.perf_counter()
counts = Counter(list_qwe)
counter = dict(sorted(counts.items()))
print(counter)
sort_list=[]
for index,i in counter.items():
    sort_list.extend([int(index)]*i)
print(sort_list)
print(f"заняло {time.perf_counter()-start_time}")