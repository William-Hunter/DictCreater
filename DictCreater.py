#!usr/bin/python
# coding=gbk
import sys

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
File=file(sys.argv[2],'w')
def make(line,level):
	level-=1	
	for i in letter:
		password=line
		password+=i	
		if level>0:
			make(password,level)
		else:
			File.write(password+'\n')			
			print password+'\t',
#main
count=0
for i in sys.argv:
	count+=1
if count==1:
	print "python DictCreater.py [bit length] [outfile path]\nExample:\tpython DictCreater.py 3 password.txt"
elif type(int(sys.argv[1]))!=int:
	print 'your bit length was trouble'
elif len(sys.argv[1])==0:
	print 'your file path invalid'
else:
	make('',int(sys.argv[1]))		
	
File.close()		
print '\nthe script is end.........'