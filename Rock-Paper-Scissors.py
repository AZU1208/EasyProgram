Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #入力値
#10 
#p g 
#c c 
#p p 
#g g 
#c p 
#c p 
#g g 
#p p 
#g p 
#p g


N=int(input())
s=[input.split() for i in range(N)]

a=[]
b=[]
for h in range(0,N):
	if s[h][0]==s[h][1]:
		pass
	elif s[h][0]=="g" and s[h][1]=="c":
		a.append(h)
	elif s[h][0]=="c" and s[h][1]=="p":
		a.append(h)
	elif s[h][0]=="p" and s[h][1]=="g":
		a.append(h)
	elif s[h][0]=="g" and s[h][1]=="p":
		b.append(h)
	elif s[h][0]=="p" and s[h][1]=="c":
		b.append(h)
	elif s[h][0]=="c" and s[h][1]=="g":
		b.append(h)
		
print(len(a))
print(len(b))

