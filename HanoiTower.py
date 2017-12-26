n=int(input('请输入汉诺塔层数：'))
s=0
def hanoi(n,a,b,c):
	global s
	if n==1:
		print(a,'->',b)
		s=s+1
	else:
		hanoi(n-1,a,c,b)
		hanoi(1,a,b,c)
		hanoi(n-1,b,a,c)
hanoi(n,'a','b','c')
print(s)


		
		
