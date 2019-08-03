 
#bubblesort

''' bubble sort ka simple funda hai
sorting via swapping
do no. ko compare karo left wala bada hai to right me swap kar do ar isis trha use end tk le jao
for n no. of list it takes n-1 passes.
 jaise ki yha

bubble sort function banne ke bad
 i ki value get kari , range 0 se lenght of list -1  tk
 matlb total kitne pass honge
 fr ye to hua no of passes k bare me
 ab comapre b karna hai do index ko
 to j and j+ 1
 vo value kha se aai
 second for loop inside first loop
 jo chalega 0 se leker len og list - 1 -i (- i = i ki value ko minus karwa hua chalega )
 isse j ki or j+1 ki value aa gyi
 fr compare kar lo
 or fr swapping karlo
 swapping third variable se b kar skte the Temperory variable leke
 but direct kar skte hai

 fr aap again j wale for loop me jaynge (kb tk - agar len(list 10) hai to for for i = 0
 to i ka loop 0 se 9 tk chaega
 or j ka loop 0-8 tk chalega,
 fr i = 1 to i ka loop 1- 9,
 or j ka loop 1 - 7 (kuki largest number right side me sort hota ja rha hai isily))


fr condition over
so i loop me i ki value change
ese hi
last me call the function
and print statement 


'''
#userinput ke ly sotres the input in variable a
#split the inputs and store in same variable
#but its work as string
print ('Enter many number by putting , in between them :- ')
a = input('Enter any string :' )
a = a.split(',')
l = len(a)
print ('unsorted list : ', a)

def bubblesort(a):
    for i in range(0, l-1):
        for j in range(0, l-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a 


bubblesort(a)
print ('Sorted list : ', a)
