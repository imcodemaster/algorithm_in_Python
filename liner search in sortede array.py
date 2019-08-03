#liner serch in sorted array :

def findElement(array,item):
    n = len(array)
    for i in range(n):
        if item == array[i]:
            print ('present')
        elif item < array[i]:        
            return -1
    return


        
array = [1,2,3,43,25,44,36,90,5,6,39,40,5,7,4,35,823,46,12,48,23,605,4,62]
array = sorted(array)
print (array)
item = 46

findElement(array, item)
