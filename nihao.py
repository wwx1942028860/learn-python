file = open("gxx.v","w")
file.write("digraph G { \n" )
D = [
		[1 , 1 , 2],
		[2 , 2 , 4],
		[3 , 3 , 6],
		[4 , 4 , 8],
		[5 , 5 , 10],
		[6 , 6 , 12]
]
for d in D:
	file.write("%d->%d[label = %d]\n"%(d[1],d[2],d[0]))
file.write("} \n")