Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

      start  end   high  low   
#11/1  11    14    16    10
#11/2  12    15    17    10
#11/3  13    11    14    11
#11/4  12    10    13     8
#11/5  11    13    14    10


N = int(input())

a = []
for i in range(N):
    a.append(list(map(int,input().split())))

lst2 = [ flatten for inner in a for flatten in inner ]
print(a[0][0],a[N-1][1],max(lst2),min(lst2))
