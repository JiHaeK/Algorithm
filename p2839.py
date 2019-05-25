n = int(input())
cnt5=-1
cnt3=0
for i in range(int(n//5), -1, -1) :
	if(n-5*i)%3==0:
		cnt5=i
		cnt3=(n-5*i)//3
		break
print(int(cnt5+cnt3))


