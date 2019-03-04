#!usr/bin/python
# coding=gbk
import sys
import time
StartTime=time.time()

letter_number=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']

def make(line,level,array):
	for i in array:
		password=line
		password+=i	
		if level>0:
			make(password,level-1,array)
		else:
			File.write(password+'\n')			
			print password+'\t',



typeof=sys.argv[1]
level=int(sys.argv[2])
filePath=sys.argv[3]


# if len(level)==1:
# 	print "python DictCreater.py [dictType] [bit length] [outfile path]\nExample:\tpython DictCreater.py n 3 password.txt"
# elif type(int(level))!=int:
# 	print 'your bit length was trouble'
# elif len(level)==0:
# 	print 'your file path invalid'
# else:	


array=''

if typeof=='l':
	array=letter
elif typeof=='n':
	array=number
elif typeof=='ln':
	array=letter_number

File=file(filePath,'w')

for index in range(0,level):
	make('',index,array)
	
File.close()		

print '\nthe script is end........use time:',time.time()-StartTime,'second'