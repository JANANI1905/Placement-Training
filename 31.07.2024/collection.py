u = int(input())
v = list(map(int,input().strip().split()))
w= int(input())
x = []
for i in range(w):
    a,b = list(map(int,input().strip().split()))
    if a in v:
        x.append(b)
        v.remove(a)
print (sum(x))