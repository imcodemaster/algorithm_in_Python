import random

#bubbbleSort

def bubblesort(array):
    for i in range (0, l - 1):
        for j in range (0, l-1-i):
            if array [j] > array[j+ 1]:
                array[j], array[j+1] = array[j+1], array [j]

    return array

                
#selectionsort
def selectionsort(array):
    for i in range (0, l):
        minimum = i
        for j in range (i+1, l):
            if array[minimum] > array[j]:
                array[minimum], array[j] = array[j], array[minimum]

    return array



#insertionsort

def insertionsort(sample):
    for i in range(1, len(sample)):
        j =i
        while (j!=0 and sample[j] < sample[j-1]):
            sample[j-1], sample[j] = sample[j], sample[j-1]
            j -=1

#quick sort
def quick_sort(array):
    ARRAY_LENGTH = len(array)  
    if( ARRAY_LENGTH <= 1): 
        return array 
    else:  
        PIVOT = array[0] 
        GREATER = [ element for element in array[1:] if element > PIVOT ]
        LESSER = [ element for element in array[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

    

#merge sort
    
def mergeSort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
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
    
 #heap sort


def heapify (array, i , l) :
    largest  = i
    left  = 2*i + 1
    right = 2*i + 2

    if left < l and array[left] > array [largest]:
        largest = left

    if right < l and array [right] > array [largest] :
        largest = right

    if largest != i :
        
        array[largest], array[i] = array[i], array[largest]
        heapify(array, largest, l)


def heapsort (array):
    l = len(array)
    for i in range (l, -1,-1) :
        heapify (array, i , l )
        
    for i in range (l - 1, 0, -1):
        array [0], array [i] = array [i], array [0]
        heapify (array, 0 , i )
    return array 
        
print ('Number Sorting Program :\n \n ')
n = int(input('How many number you want to Sort: \n'))
print ('So you want to sort ', n, ' numbers.\n')

q = int(input('You are going to enter number\n 1. Manually \n  Or we sort \n2. Random numbers , \n Choose corresponding number.'))

if q == 1 :
    array = []
    print ("Enter any number and hit Enter, repeat this process untill you enter ", n , "numbers.")
    for i in range(n):  
        numbers = int(input("\n Enter any number: \t"))
        array.append(numbers)
    print ('\n List we are going to sort ', array)
 

if q == 2 :
    
    array = [random.randint(1, 1000000) for _ in range(n)]
    print(array)   

l = len(array)

print ('\n Which sort you want to run : \n \n1. Bubble sort, \n2. Selection Sort, \n3. Insertion Sort, \n4. Quick Sort, \n5. Merge sort, \n6. Heap Sort ')

var = int(input ('\n \n Enter number for corresponding sorting Algorithum  :'))


if var ==1 :
    bubblesort(array)
    print ('Bubble Sort : ',array)
elif var ==2 :
    selectionsort (array)
    print ('Selection Sort : ' , array)
elif var == 3 :
    insertionsort (array)
    print ('Insertion Sort : ',array)
elif var == 4 :
    print ('Quick sort :', quick_sort(array))
elif var == 5 :
    mergeSort (array)
    print ('merge sort  :', array)
elif var == 6 :
    heapsort (array)
    print ('Heap sort  :', array)
else :
    print ('Enter number to run Sort')


#task completed



















