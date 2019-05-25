n=int(input())

def solve(i) :
	count=0
	for i in range(1, i+1) :
		if(i<100) : 
			count+=1
		elif(i<1000) :
			n100, n10, n1=str(i)[0], str(i)[1], str(i)[2]
			n100, n10, n1=int(n100), int(n10), int(n1)
			if n100-n10==n10-n1 :
				count+=1
		else :
			pass 
	return count

print(solve(n))