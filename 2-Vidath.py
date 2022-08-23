list = []
n = input('Enter the numbers to be sorted')
len =0
num= n.split()
for i in num:
    list.append(int(i))
    len =len +1
def mergeSort(A, p, r):
    if p<r:
        q= (p+r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A,p,q,r)
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1)
    R = [0]*(n2)
    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    i=0
    j=0
    k=p
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k] = R[j]
            j=j+1
        k=k+1
    while i<n1:
        A[k] = L[i]
        i=i+1
        k=k+1
    while j<n2:
        A[k] = R[j]
        j=j+1
        k=k+1
mergeSort(list, 0, len-1)
print(list)