n=int(input())

case=[]
total=0
for i in range(n) :
	case=list(map(str, input().split('X')))
	for j in range(len(case)) :
		for x in range(1, len(case[j])+1) : 
			total+=x
	print(total)
	total=0
	case=[]