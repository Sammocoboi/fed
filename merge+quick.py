import random
import time

list_qwe=[]
for i in  range(1_000_000):
    list_qwe.append(random.randint(0,999999))

#quick
def quick_sort(array:list):
    if len(array)<=1:
        return array

    pivot = array[len(array)//2]
    low=[x for x in array if x<pivot]
    middle = [x for x in array if x==pivot]
    right = [x for x in array if x>pivot]

    return quick_sort(low)+middle+quick_sort(right)

# print(quick_sort(list_qwe))



#merge 

def merge_sort(array):
    if len(array)<=1:
        return array
    pivot = len(array)//2
    left=merge_sort(array[:pivot])
    right=merge_sort(array[pivot:])

    return sort_merge(left,right)

def sort_merge(left,right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


list_qwe=[]
for i in  range(1_000_000):
    list_qwe.append(random.randint(0,999999))

print(merge_sort(list_qwe))
