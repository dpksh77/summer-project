#!/usr/bin/python2

import os


	

print "\nnow we will check jdk7 and hadoop7 on the clientnode system"
		
print "so first we will check jdk7 software installed or not"
				
print "\nto check jdk7 installed enter the command\n"
os.system("tput setaf 2")		
print "]#java -version\n"
os.system("tput setaf 0")
javav=raw_input()
while(javav!="java -version"):
	print "command not found\n re-enter the command"
	javav1=raw_input()			
	if(javav1=="java -version"):
		
		break
os.system("tput setaf 2")
os.system("java -version")
os.system("tput setaf 0")
print "\nwe recommanded that you enter this command(rpm -ivh jdk-7u79-linux-x64.rpm) whether you already installed or want to install jdk7" 
print "\nbecause if you already installed then it will reinstall this again and no harm will take place"		
print "\nso enter the command\n"
os.system("tput setaf 2")
	
print "]#rpm -ivh jdk-7u79-linux-x64.rpm"
os.system("tput setaf 0")
javainst=raw_input()
while(javainst!="rpm -ivh jdk-7u79-linux-x64.rpm"):
	print "command not found\n re-enter the command"
	javainst1=raw_input()			
	if(javainst1=="rpm -ivh jdk-7u79-linux-x64.rpm"):
		print "command ok"		
				
				
		break
os.system("tput setaf 2")
os.system("rpm -ivh jdk-7u79-linux-x64.rpm")
os.system("tput setaf 0")

print "\n now we will set the path of the java variable"
os.system("export JAVA_HOME=/usr/java/jdk1.7.0_79")
os.system("export PATH=/usr/java/jdk1.7.0_79/bin/:$PATH")
print "\n And to permanent=> enter these in .bashrc file"

bash=raw_input("now we will update .bashrc file\n to update .bashrc file enter the command 'y'")
os.system("tput setaf 0")
while(bash!='y'):
	print "wrong input re-enter y "
	bash1=raw_input()
	if(bash1=='y'):
		print "type correctly"
		break

os.system("tput setaf 1")
print "\n      before update .bashrc file"
os.system("tput setaf 0")
os.system("cat /root/.bashrc")
os.system("tput setaf 1")
print "\n             after updating .bashrc file"
os.system("tput setaf 0")
fh=open("/root/.bashrc","w")
fh.write("# .bashrc\n\n")
fh.write("# User specific aliases and functions\n\n")
fh.write("alias rm='rm -i'\n")
fh.write("alias cp='cp -i'\n")
fh.write("alias mv='mv -i'\n\n")

fh.write("# Source global definitions\n")
fh.write("if [ -f /etc/bashrc ]; then\n")
fh.write("	. /etc/bashrc\n")
fh.write("fi\n")
fh.write("export JAVA_HOME=/usr/java/jdk1.7.0_79\n")
fh.write("export PATH=/usr/java/jdk1.7.0_79/bin/:$PATH\n")
fh.close()
os.system("cat /root/.bashrc")
os.system("tput setaf 2")
print "\n\n       Now .bashrc file is configured"
os.system("tput setaf 0")
print "enter the command to execute bash file\n]#./hadoop_client.py"
os.system("exec bash")

