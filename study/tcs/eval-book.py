def NANDEVAL(n,m,L,X):
    s = len(L)
    t = max(max(a,b,c) for (a,b,c) in L)+1
    Vartable = [0]*t
    def GET(V, i): return V[i]
    def NAND(a, b):
        if a == b and b == 1:
            return 0
        else:
            return 1
    def UPDATE(V,i,b):
        V[i]=b
        return V
    for i in range(n):
        Vartable = UPDATE(Vartable, i, X[i])

    for (i,j,k) in L:
        a = GET(Vartable, j)
        b = GET(Vartable, k)
        c = NAND(a,b)
        Vartable = UPDATE(Vartable, i, c)
    return [GET(Vartable, t-m+j) for j in range(m)]


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
for i in range(len(X)):
    res = NANDEVAL(n, m, L, X[i])
    print(res)

