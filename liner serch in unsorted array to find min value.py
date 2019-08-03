#finding the smallest number in unsorted array :
#liner serh algorithm

def smallestitem(array):
    n = len(array)
    smallest = array[0] 
    for i in range( 1 , n):
        if array[i] < smallest:
            smallest = array[i]
    print (smallest)
            
array = [12,32,14,109,43,85,42,912,4,57,2,3,9,10,8,41,6,2,4,98,6,5,3,7,85,6,4,35,7,8,34,4,63,20,4,23]
smallestitem(array)
