'''largest prime factor of the number 600851475143 '''
import math
def primefactor(n):
	li=[]

	for i in xrange(2,n+1):
		count=0
		for j in xrange(2,i+1):
			if i%j==0:
				count+=1
		if count==1:
			if n%i==0:
				li.append(i)
	print 'largest prime factor of the number %d is %d'%(n,li[len(li)-1])
	
	
'''def prime(n):
	sub_n = n/2
	li=[]
	for i in range(sub_n,1,-1):
		if n%i==0:
			for j in range(i+1):
				for m in range(j+1)
				li.append(i)
	print li
	#for i in range(sub_n,-1)
	#print 'the largest factor of %d is %d'%(n,sqt-1)'''
	
if __name__=="__main__":
	primefactor(13195)
	#prime(13195)
