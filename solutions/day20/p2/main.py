
TARGET=34000000
#This value indicates that we think that the
#solution will be less than this value
#Since we are bruteforcing here, this saves a lot of time
REASONABLE_MAX=1500000

def main():
	#Initialize the houses
	houses = [ ]
	for h in xrange(0, REASONABLE_MAX):
		houses.append(0)
	#For each elf
	for e in xrange(1,REASONABLE_MAX+1):
		#Visit each house
		#We start at e because we can't go smaller
		#Since each elf only visits up to 50 houses, we stop at e*50 or REASONABLE_MAX
		#We increment by the elf count because it does not visit every house
		for h in xrange(e, min(e*50, REASONABLE_MAX), e):
			houses[h] += e * 11
	#Find first that has enough
	answer = -1
	for i, h in enumerate(houses):
		if h >= TARGET:
			answer = i
			break
	if i > 0:
		print "Answer: %d" % i
	else:
		print "No solution. Try increasing REASONABLE_MAX"
if __name__ == "__main__":
	main()
