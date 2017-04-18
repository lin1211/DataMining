if __name__ == "__main__":
	#read file
	f=open('initialDataset.txt','r')
	f2=open('newDataset.txt','w')
	for line in f:
		# line=line.strip('\n')
		# line=line.strip('\r')
		attribute=line.split(' ')
		if '?' not in attribute:
			f2.write(line)
	f.close()
	f2.close()