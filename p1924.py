
x, y=input().split()
x=int(x)
y=int(y)
m=[31,28,31,30,31,30,31,31,30,31,30,31]
d=["SUN","MON","TUE","WED","THU","FRI","SAT"]
result=0

for i in range(x-1):
	result+=m[i]

result+=y
print(d[result%7])