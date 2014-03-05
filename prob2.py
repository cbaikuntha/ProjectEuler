'''finding the all even terms sum in the fibonacci series below 4 million'''
def fibo(n):
	t1,t2,t3,li,i,s=1,2,0,[],0,0
	while(i<n):
		t3=t1+t2
		t1=t2
		t2=t3
		i+=1
		if t3 < 40000000 and t3%2==0:
			li.append(t3)
			s+=t3
	print 'fibonacci series sum  ',s,li
	
if __name__=="__main__":
	fibo(100)
