'''Largest palindrome product for 3-digit numbers'''
li=[]
def palindromepro():
	for i in range(998*999,10000,-1):
		rev=reverse(i)
		if i==rev:
			print 'reverse :',i
			li=fact(i)
			continue
			
		else:
			continue
	print li[0]	
def reverse(n):
	reve=0
	while(n!=0):
		r=n%10
		n=n/10
		reve=reve*10+r
	
	return reve
def fact(m):
	j=0
	for i in range(999,100,-1):
		j=m/i
		
		if m%i==0 and (j in range(100,1000)):
			li.append([i,j])
			break	
			
		else:
			continue
	return li
	
		

if __name__=="__main__":
	print palindromepro()
