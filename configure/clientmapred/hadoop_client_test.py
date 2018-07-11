#!/usr/bin/python2

import os


os.system("tput setaf 1")
print "\nnow we will make folder to upload on hadoop cluster"
fol=raw_input("enter folder name:-")
print "\nto make folder enter the commmand\n"
#print "\n\nAnd after exit again type exit to show menu"
os.system("tput setaf 0")
os.system("tput setaf 2")
print "]#mkdir /"+fol
os.system("tput setaf 0")
hexit=raw_input()
while(hexit!="mkdir /"+fol):
	print "command not found\n re-enter the command"
	hexit1=raw_input()			
	if(hexit1=="mkdir /"+fol):
		print "command ok"
				
		break
os.system("mkdir /"+fol)




os.system("tput setaf 1")
print "\nnow we will make file to upload on hadoop cluster"
file1=raw_input("enter file name:-")

format1=raw_input("enter the file format in . format like .txt:-")






print "\nto make file enter the commmand\n"
#print "\n\nAnd after exit again type exit to show menu"
os.system("tput setaf 0")
os.system("tput setaf 2")
print "]#touch /"+fol+"/"+file1+format1
os.system("tput setaf 0")
hexit1=raw_input()
while(hexit1!="touch /"+fol+"/"+file1+format1):
	print "command not found\n re-enter the command"
	hexit2=raw_input()			
	if(hexit2=="touch /"+fol+"/"+file1+format1):
		print "command ok"
				
		break
os.system("touch /"+fol+"/"+file1+format1)


print "\nto write some thing in file enter the command"
print "\n]#gedit /"+fol+"/"+file1
hexit1=raw_input()
while(hexit1!="gedit /"+fol+"/"+file1):
	print "command not found\n re-enter the command"
	hexit2=raw_input()			
	if(hexit2=="gedit /"+fol+"/"+file1):
		print "command ok"
				
		break


os.system("gedit /"+fol+file1)



os.system("tput setaf 1")
print "\nnow we will  upload file on hadoop cluster"
file1=raw_input("enter file name:-")
print "\nto upload the file enter the commmand\n"
#print "\n\nAnd after exit again type exit to show menu"
os.system("tput setaf 0")
os.system("tput setaf 2")
print "]#hadoop fs -put /"+fol+"/"+file1+" /"
os.system("tput setaf 0")
hexit1=raw_input()
while(hexit1!="hadoop fs -put /"+fol+"/"+file1+" /"):
	print "command not found\n re-enter the command"
	hexit2=raw_input()			
	if(hexit2=="hadoop fs -put /"+fol+"/"+file1+" /"):
		print "command ok"
				
		break
os.system("hadoop fs -put /"+fol+"/"+file1+" /")


os.system("tput setaf 1")
print "\nnow we will see the uploaded file on hadoop cluster"
file1=raw_input("enter file name:-")
print "\nto see the uploaded file enter the commmand\n"
#print "\n\nAnd after exit again type exit to show menu"
os.system("tput setaf 0")
os.system("tput setaf 2")
print "]#hadoop fs -ls /"
os.system("tput setaf 0")
hexit1=raw_input()
while(hexit1!="hadoop fs -ls /"):
	print "command not found\n re-enter the command"
	hexit2=raw_input()			
	if(hexit2=="hadoop fs -ls /"):
		print "command ok"
				
		break
os.system("hadoop fs -ls /")




raw_input()
