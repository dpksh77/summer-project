#!/usr/bin/python2

import os




		
print "so first we will check jdk7 software installed or not"
				

os.system("tput setaf 2")
os.system("java -version")
os.system("tput setaf 0")


print "Now we will check hadoop7 installed or not"

os.system("hadoop version")
print "\nwe recommanded that you enter this command(rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles) whether you already installed or want to install hadoop7"
print "\nbecause if you already installed then it will reinstall this again and no harm will take place"

os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles")

print "Now we will check hadoop7 installed or not"

os.system("hadoop version")








os.system("tput setaf 1")
print "now we will update hdfs file\n"



print "\nwe will make folder for hadoop storage file"
i=65
name=chr(i)
#folder=raw_input("enter folder name to make:-")
statusfolder=os.system("mkdir /"+name)
while(statusfolder!=0):
	print "folder exist so we are making another folder"
	i=i+1
	name=chr(i)
	status4=os.system("mkdir /"+name)
	if status4==0:
		
		break
os.system("tput setaf 1")
print "\n      before update hdfs-site.xml file"
os.system("tput setaf 0")
os.system("cat /etc/hadoop/hdfs-site.xml")
os.system("tput setaf 1")
#ip4=raw_input("to update mapred file enter ip of the jobtracker:-")
print "\n             after updating hdfs-site.xml file"
os.system("tput setaf 0")
fh=open("/etc/hadoop/hdfs-site.xml","w")
fh.write("<?xml version=\"1.0\"?>\n")
fh.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")
fh.write("<!-- Put site-specific property overrides in this file. -->")
fh.write("\n\n<configuration>\n\n<property>")
fh.write("\n<name>dfs.data.dir</name>")
fh.write("\n<value>/"+name+"</value>")
fh.write("\n</property>\n\n</configuration>\n\n\n\n\n")
fh.close()
os.system("cat /etc/hadoop/hdfs-site.xml")
os.system("tput setaf 2")
print "\n\n       Now hdfs file is configured"
os.system("tput setaf 0")


print "\nnow we will update mapred-site.xml file\n" 
os.system("tput setaf 1")
print "\n      before update mapred-site.xml file"
os.system("tput setaf 0")
os.system("cat /etc/hadoop/mapred-site.xml")
os.system("tput setaf 1")
ip4=raw_input("to update mapred file enter ip of the jobtracker:-")
print "\n             after updating mapred-site.xml file"
os.system("tput setaf 0")
fh=open("/etc/hadoop/mapred-site.xml","w")
fh.write("<?xml version=\"1.0\"?>\n")
fh.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")
fh.write("<!-- Put site-specific property overrides in this file. -->")
fh.write("\n\n<configuration>\n\n<property>")
fh.write("\n<name>mapred.job.tracker</name>")
fh.write("\n<value>/"+ip4+":9002</value>")
fh.write("\n</property>\n\n</configuration>")
fh.close()
os.system("cat /etc/hadoop/mapred-site.xml")
os.system("tput setaf 2")
print "\n\n       Now mapred file is configured"
os.system("tput setaf 0")


print "\nnow we will update core-site.xml file.\n"
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

os.system("iptables -F")


print "\nnow we will stop and disable firewalld"

os.system("systemctl stop firewalld")

print "\nnow we will disable firewalld \n"

os.system("systemctl disable firewalld")


print "\nnow we will check service of firewalld \n"

os.system("systemctl status firewalld")



print "\nnow we will start datanode sevice"

os.system("hadoop-daemon.sh start datanode")



print "\nnow we will start tasktracker sevice"
os.system("hadoop-daemon.sh start tasktracker")


print "\nnow we will check service start or not"

os.system("jps")



print "this is end of tasktracker configuration"


os.system("tput setaf 1")
print "\nnow we will exit from tasktracker"
print "\nto exit from tasktracker enter the commmand\n"
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

