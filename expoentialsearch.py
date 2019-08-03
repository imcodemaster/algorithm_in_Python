#exponential algorithm

'''
funda -
sorted arrray needed
first compare arr[0] element to x (element to be founded)
if available return

unless take a variable i and start with 1 index
compare
if got good
varna multiply by 2 to check element exponentially
if founded good
if in any case i > x
back to i/2 position and start a binary search

'''

#codes
#binary search implementation find mid value
# stating and ending pointr divede by 2
#if mid value is an element return it
#unless
#go to left and right half respectively 
def binarySearch(arr, start , n , key):
    start = 0
    end = n-1
    while start <= end:
        mid = int((start + end)/2)
        if key == arr[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1


def expoSearch (arr, key , n) :
    if arr[0] == key : #checking 0th position
        pass #if yes then return
    i = 1 #taking i as 1 to check exponential 1, 2, 4 .. and so on in every iteration
    while i < n and arr[i] <= key: #condition i value smaller than n and i value shold smaller or equal to finding element
        i = i * 2 #if not than go to exponential index to search again in next iteration
    return binarySearch(arr, i/2, min(i,n) , key)    #calling binary search to get the position of finding element if not present in exponentiasl position

#driverCode :
arr = [1,2,3,4,5,6,7,8,9,10,78,89]
n = len(arr)
print ('size of array ' , n) #jarurat thi ni print karwane ki but pata ho ki kitne ka array tha isisly kia 
key = 1
index = expoSearch (arr, key , n )



        
