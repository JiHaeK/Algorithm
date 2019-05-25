n=int(input())

s=n//10+n%10
tmp=int(str(n%10)+str(s%10))

for i in range(1,100) :
	if(n == tmp) :
		print(i)
		break
	else :
		s=tmp//10+tmp%10
		tmp=int(str(tmp%10)+str(s%10))



