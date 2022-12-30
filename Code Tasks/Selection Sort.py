A=[1,4,6,7,9,2,21]
def selection_sort(A):
    limit = len(A)-1
    i = 0
    
    while i < limit:                  
        minn = i
        maxx = limit
        for j in range (i+1, limit):           
            if A[j] < A[minn]:                  
               minn = j
        A[i], A[minn] = A[minn], A[i]
        i = i + 1
        
        for l in range(i+1,0):     
            if A[l] > A[maxx]:
                 maxx=l
            A[limit], A[maxx] = A[maxx], A[limit]
            limit=limit-1
    return A
print(selection_sort(A))
