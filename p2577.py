a=int(input())
b=int(input())
c=int(input())

result=a*b*c
a=[0]*10

for i in str(result) :
	a[int(i)]+=1

for i in a :
	print(i)