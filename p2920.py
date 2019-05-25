n=[]
n=list(map(int, input().split(" ")))

ascen=[1, 2, 3, 4, 5, 6, 7, 8]
desen=[8, 7, 6, 5, 4, 3, 2, 1]

if (n == ascen) :
	print("ascending")
elif (n == desen) :
	print("descending")
else :
	print("mixed")

	