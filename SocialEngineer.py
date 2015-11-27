#!usr/bin/python
import time
import os
StartTime=time.time()
Dict=[]
def make():
	for i in Dict:
		password=''
		password+=i	
		for i in Dict:
			if i==password:
				continue
			else:	
				line=password
				line+=i
				File.write(line+'\n')			
				print line+'\t'
#main
print "use\'to quote your input,like:'jack'"
Dict.append(input('first name:'))
Dict.append(input('last name:'))
Dict.append(input('brithday:'))
File=file(input('OutFile:'),'w')
make()
File.close()		
print '\nthe script is end........use time:',time.time()-StartTime,'second'
