#!/usr/bin/python2

import os


	



print "\nto check report of the namenode enter the commmand\n"
os.system("tput setaf 2")
print "]#hadoop dfsadmin -report"
os.system("tput setaf 0")
hreport=raw_input()
while(hreport!="hadoop dfsadmin -report"):
	print "command not found\n re-enter the command"
	hreport1=raw_input()			
	if(hreport1=="hadoop dfsadmin -report"):
		print "command ok"
				
		break
os.system("hadoop dfsadmin -report")





os.system("tput setaf 1")

print "\nto exit from namenode enter the commmand\n"
print "\n\nAnd after exit again type exit to show menu"
os.system("tput setaf 0")
os.system("tput setaf 2")
print "]#exit"
os.system("tput setaf 0")
hexit=raw_input()
while(hexit!="exit"):
	print "command not found\n re-enter the command"
	hexit1=raw_input()			
	if(hexit1=="exit"):
		print "command ok"
				
		break
os.system("exit")

