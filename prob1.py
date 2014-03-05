'''multiple of 3 or 5 below 1000 '''
def multiple():
	li,s=[],0
	for i in range(1,100):
		if i%3==0 or i%5==0:
			li.append(i)
			s+=i
	print 'list of 3 or 5 multiples ',li
	print 'sum of 3 or 5 multiples %d '%s	
	
if __name__=="__main__":
	multiple()
