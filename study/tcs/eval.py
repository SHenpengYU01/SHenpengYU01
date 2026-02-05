

def eval(n, m, L, x):
    def GET(Arr, i):
        return Arr[i]
    def UPDATE(Arr, i, b):
        Arr[i] = b
        return Arr
    def NAND(a, b):
        return a == b and a == 1

    t = max(max(a,b,c) for (a,b,c) in L) + 1
    V = [0]*t
    for i in range(n):
        V[i] = x[i]
    for l in L:
        i = GET(V, l[1])
        j = GET(V, l[2])
        k = GET(V, l[0])
        UPDATE(V, k, NAND(i,j))
    return V[-m:]


n=3
m=1
L=[(3,2,2), (4,1,1), (5,3,4), (6,2,1), (7,6,6), (8,0,0), (9,7,8), (10,5,0),(11,9,10)]


X=[[0,0,0],
   [0,0,1], 
   [0,1,0],
   [0,1,1],
   [1,0,0],
   [1,0,1],
   [1,1,0],
   [1,1,1]
   ]
for i in range(8):
    res = eval(n, m, L, X[i])
    print(res)
    

