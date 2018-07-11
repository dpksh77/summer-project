#!/usr/bin/python2

import os


	












		
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


print "Now we will check hadoop7 installed or not"
print "\nto check hadoop7 installed enter the command\n"
os.system("tput setaf 2")
print "]#hadoop version\n"
os.system("tput setaf 0")
hadoo=raw_input()
while(hadoo!="hadoop version"):
	print "command not found \nre-enter the command"
	hadoo1=raw_input()
	if(hadoo1=="hadoop version"):
		print "command ok"
			
		break
os.system("hadoop version")
print "\nwe recommanded that you enter this command(rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles) whether you already installed or want to install hadoop7"
print "\nbecause if you already installed then it will reinstall this again and no harm will take place"
print "\nso enter the command\n"
os.system("tput setaf 2")
print "]#rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles"
os.system("tput setaf 0")
hadooinst=raw_input()
while(hadooinst!="rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles"):
	print "command not found\n re-enter the command"
	hadooinst1=raw_input()			
	if(hadooinst1=="rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles"):
		print "command ok"
				
		break
os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles")

print "Now we will check hadoop7 installed or not"
print "\nto check hadoop7 installed enter the command\n"
os.system("tput setaf 2")
print "]#hadoop version\n"
os.system("tput setaf 0")
hadoo=raw_input()
while(hadoo!="hadoop version"):
	print "command not found \nre-enter the command"
	hadoo1=raw_input()
	if(hadoo1=="hadoop version"):
		print "command ok"
			
		break
os.system("hadoop version")








os.system("tput setaf 1")
pause=raw_input("now we will update hdfs file\n to update hdfs file enter the command 'y'")
os.system("tput setaf 0")
while(pause!='y'):
	print "wrong input re-enter y "
	pause1=raw_input()
	if(pause1=='y'):
		print "type correctly"
		break
print "\nwe will make folder for hadoop storage file"
folder=raw_input("enter folder name to make:-")
statusfolder=os.system("mkdir /"+folder)
while(statusfolder!=0):
	print "folder exist so choose another folder name"
	folder=raw_input()
	status4=os.system("mkdir /"+folder)
	if status4==0:
		break
os.system("tput setaf 1")
print "\n      before update hdfs-site.xml file"
os.system("tput setaf 0")
os.system("cat /etc/hadoop/hdfs-site.xml")
os.system("tput setaf 1")
print "\n             after updating hdfs-site.xml file"
os.system("tput setaf 0")
fh=open("/etc/hadoop/hdfs-site.xml","w")
fh.write("<?xml version=\"1.0\"?>\n")
fh.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")
fh.write("<!-- Put site-specific property overrides in this file. -->")
fh.write("\n\n<configuration>\n\n<property>")
fh.write("\n<name>dfs.data.dir</name>")
fh.write("\n<value>/"+folder+"</value>")
fh.write("\n</property>\n\n</configuration>")
fh.close()
os.system("cat /etc/hadoop/hdfs-site.xml")
os.system("tput setaf 2")
print "\n\n       Now hdfs file is configured"
os.system("tput setaf 0")
os.system("tput setaf 1")
pause2=raw_input("now we will work on core file\n to work on core file enter the command 'y'")
os.system("tput setaf 0")
while(pause2!='y'):
	print "wrong input re-enter y "
	pause3=raw_input()
	if(pause3=='y'):
		print "type correctly"
		break

os.system("tput setaf 1")
print "\n\n      before update core-site.xml file"
os.system("tput setaf 0")
os.system("tput setaf 4")
os.system("cat /etc/hadoop/core-site.xml")
os.system("tput setaf 0")
os.system("tput setaf 1")
print "enter the ip address of namenode to configure the core file"
os.system("tput setaf 0")
ip1=raw_input()

os.system("tput setaf 1")
print "\n\n             after updating core-site.xml file"
os.system("tput setaf 0")

fd=open("/etc/hadoop/core-site.xml","w")
fd.write("<?xml version=\"1.0\"?>\n")
fd.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")
fd.write("<!-- Put site-specific property overrides in this file. -->")
fd.write("\n\n<configuration>\n\n<property>")
fd.write("\n<name>fs.default.name</name>")
fd.write("\n<value>hdfs://"+ip1+":9001</value>")
fd.write("\n</property>\n\n</configuration>")
fd.close()
os.system("cat /etc/hadoop/core-site.xml")
os.system("tput setaf 2")
print "\n\n       Now core file is configured"
os.system("tput setaf 0")
os.system("tput setaf 2")
print "\n\n       both files are configured so datanode is configured"
os.system("tput setaf 0")


print "\nbefor start sevice we will flush ip tables"
print "\nto flush ip tables enter the command\n"
os.system("tput setaf 2")
print "]#iptables -F"
os.system("tput setaf 0")
iptables=raw_input()
while(iptables!="iptables -F"):
	print "command not found\n re-enter the command"
	iptables1=raw_input()			
	if(iptables1=="iptables -F"):
		print "command ok"
				
		break
os.system("iptables -F")


print "\nnow we will stop and disable firewalld"
print "\nto stop firewalld enter the command\n"
os.system("tput setaf 2")
print "]#systemctl stop firewalld"
os.system("tput setaf 0")
iptables2=raw_input()
while(iptables2!="systemctl stop firewalld"):
	print "command not found\n re-enter the command"
	iptables3=raw_input()			
	if(iptables3=="systemctl stop firewalld"):
		print "command ok"
				
		break
os.system("systemctl stop firewalld")

print "\nto disable firewalld enter the command\n"
os.system("tput setaf 2")
print "]#systemctl disable firewalld"
os.system("tput setaf 0")
iptables6=raw_input()
while(iptables6!="systemctl disable firewalld"):
	print "command not found\n re-enter the command"
	iptables7=raw_input()			
	if(iptables7=="systemctl disable firewalld"):
		print "command ok"
				
		break
os.system("systemctl disable firewalld")


print "\nto check service of firewalld enter the command\n"
os.system("tput setaf 2")
print "]#systemctl status firewalld"
os.system("tput setaf 0")
iptables8=raw_input()
while(iptables8!="systemctl status firewalld"):
	print "command not found\n re-enter the command"
	iptables9=raw_input()			
	if(iptables9=="systemctl status firewalld"):
		print "command ok"
				
		break
os.system("systemctl status firewalld")


os.system("hadoop-daemon.sh stop datanode")
print "\nnow we will start datanode sevice"
print "\nto start sevice enter the command\n"
os.system("tput setaf 2")
print "]#hadoop-daemon.sh start datanode"
os.system("tput setaf 0")
hadoopser=raw_input()
while(hadoopser!="hadoop-daemon.sh start datanode"):
	print "command not found\n re-enter the command"
	hadoopser1=raw_input()			
	if(hadoopser1=="hadoop-daemon.sh start datanode"):
		print "command ok"
				
		break
os.system("hadoop-daemon.sh start datanode")



print "\nnow we will check service start or not"
print "\nto check sevice enter the command\n"
os.system("tput setaf 2")
print "]#jps"
os.system("tput setaf 0")
hjps=raw_input()
while(hjps!="jps"):
	print "command not found\n re-enter the command"
	hjps1=raw_input()			
	if(hjps1=="jps"):
		print "command ok"
				
		break
os.system("jps")



print "this is end of namenode configuration"


os.system("tput setaf 1")
print "\nnow we will exit from namenode"
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

