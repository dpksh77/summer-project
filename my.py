#!/usr/bin/python2

import os
import getpass
import commands
output=commands.getoutput('pwd')
os.system("tput setaf 1")
print "                   this is a big data tutorial.\n"
os.system("tput setaf 0")
os.system("tput setaf 4")
print "  this tutorial includes hadoop cluster designing , use of docker ,devops tools, spark.\n"
print "  we are performing this task by python automated code.\n"
os.system("tput setaf 0")
os.system("tput setaf 9")
username=raw_input("enter username:-")

print "hii "+username+" enter the password"

password=getpass.getpass("hii "+username+" enter password:-")
os.system("tput setaf 0")
while(password!="deepak"):
	print "password incorrect re-enter the password"
	password1=raw_input()
	if password1=="deepak":
		print "password ok"
		break

i=1
while(i<2):
	print"""
		press 1:to open software in tutorial mode.

		press 2:to open software in direct configure mode.
		
		press 3:to exit.		
	"""
	ch1=raw_input("enter your choice:-")

	if int(ch1)==1:


		j=1
		while(j<2):
			os.system("tput setaf 6")
			print"""
			press 1:overview of big data problem and its use.
			press 2:overview of hadoop cluster.
			press 3:to make hadoop cluster.
			press 4:to make hadoop mapreduced cluster.
			press 5:to exit.		
		
			"""
			os.system("tput setaf 0s")	
			ch=raw_input("enter your choice:-")

			if int(ch)==1:
				os.system("cat "+output+"/configure/bigdata/bigdata.txt")

			elif int(ch)==2:
				os.system("cat "+output+"/configure/bigdata/hadoop.txt")	
		
			elif int(ch)==3:
				os.system(output+"/configure/bigdata/./hadoopcluster.py")
	
			elif int(ch)==4:
				os.system(output+"/configure/bigdata/./hadoopmapcluster.py")

			elif int(ch)==5:
				break;
			else :
				print "wrong input"


	elif int(ch1)==2:


		k=1
		while(k<2):
			os.system("tput setaf 6")
			print"""
		
		
			press 1:to make hadoop cluster.
		
			press 2:to make hadoop mapreduced cluster.
		
			press 3:to exit.		
		
			"""
			os.system("tput setaf 0s")	
			ch=raw_input("enter your choice:-")

			if int(ch)==1:
				os.system(output+"/configure/bigdata/./hadoopautomate.py")
	
			elif int(ch)==2:
				os.system(output+"/configure/bigdata/./hadoopmapautomate.py")

			elif int(ch)==3:
				break;
			else :
				print "wrong input"


	elif int(ch1)==3:
		exit()
raw_input()
