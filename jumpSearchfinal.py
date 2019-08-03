#jump search
#importing math modules
import math
#creating function Jumpserch with three parameter,
#array me serch karna hai
#x ko serch karna hai isly x b lia
#n no of lenght of array kha tk karna hai x ko search
def jumpsearch(arr, x ,n ):
    #higher pointer y khud choose karega based on n ka square root value jo aaygi    
    high = math.sqrt(n) 
#low pointer set to zero
    low = 0
    if arr[0] == x :
        print (x, 'presented at index : 0')
#ab jb high pointer or  no of array size ka min.
    #matlb dono me jo b choti value hai usme -1 karke jo aaya
    #agar vo chota hai x (target element se to :)
    #low value ko high value se replace or high value fr under root n step aage 
    while arr[int(min(high , n) - 1)] < x :
        low = high
        high += math.sqrt(n)

        #kb tk chalega ese ?
        #jb tk lower value total size of array ke barabar ya badi ni hoti
        # barabar matlb end of array tk pahuch gye or bdi matlb array se aage tk pahuch gye to yha pr
        #search karne ka fayda bhi ni hai ab, so
        if low >= n :
            print ('not presented ')
        #jb x value mil jaye ..
        #mtlb lower pointer se badi ho or highr pointer se choti ho to
        #linear search chalaynge
    while arr[int(low)] < x :
        low += 1
        #iterate lower pointer and inceasre 1 step if not found
        if arr[int(low)]==x : #if founder lower pointer contain value = x
            #then
            print ('Given item ', x ,' is present at index :',low)
        # (case if x not present in array)
        if low == min(high , n) :
            #checked the min value of higher pointer and n
            #if equal to low it means item not present
            print(' not prsented in entire array ')


#driver code
arr = [1,23,40,5,67,89,109,8,76,54,32,12,33,4,45,6]
arr = sorted(arr)
print(arr)
n = len(arr)
x = 109

jumpsearch(arr, x, n)

#Question : bhai index 0 ki value ka search result ni dikha rha ..
''' if x == arr[0]
     print ('present at index 0')
esi ek if condition dal skte hai
'''
#mene daldi hai ..
#kam b kar rhi hai 



