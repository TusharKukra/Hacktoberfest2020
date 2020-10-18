name = input('Enter file:')
if len(name)<1 : name = 'mbox-short.txt'
#The 'mbox-short.txt' file can be downloaded from the link: https://www.py4e.com/code3/mbox-short.txt
handle = open(name)
plist = list()
pdict = dict()
pfinal = dict()
for line in handle :
	line = line.rstrip()
	if line.startswith('From:') :
		continue
	elif line.startswith('From') :
		pdict = line.split()
		pdict = pdict[5].split(':')
		pfinal[pdict[0]] = pfinal.get(pdict[0], 0) + 1
for (k,v) in sorted(pfinal.items()) :
	print(k,v)
