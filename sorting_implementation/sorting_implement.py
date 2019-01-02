import copy

def bubble_sort(list_to_sort):
    """
    performs bubble sort given list
    :param list_to_sort: unsorted list
    :return: sorted list
    """
    for i in range(0,len(list_to_sort)-1):
        for j in range(0,len(list_to_sort)-1-i):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort



def mergeSort(alist):
    """
    performs merge sort on given list
    :param alist: unsorted list
    :return: None since mutable data structure has been passed as function argument
    """
    if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

    return

if __name__=='__main__':

    list_to_sort_bubble = [10,23,2,5,1,20,17]
    list_to_sort_merge = copy.deepcopy(list_to_sort_bubble)
    print(bubble_sort(list_to_sort_bubble))
    mergeSort(list_to_sort_merge)
    print(list_to_sort_merge)





