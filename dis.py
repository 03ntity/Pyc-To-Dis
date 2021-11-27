import dis, sys, marshal


file = sys.argv[1]
with open(file,'rb') as rese:
	rese.seek(16)
	az = dis.dis(marshal.load(rese))
