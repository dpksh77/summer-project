#!/usr/bin/python2

import os

	
		print "\nnow we will check jdk7 and hadoop7 on the namenode system"
		
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
		print "\n            Now we will configure hdfs-site.xml file"
		os.system("mkdir /master")
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
		fh.write("\n<name>dfs.name.dir</name>")
		fh.write("\n<value>/master</value>")
		fh.write("\n</property>\n\n</configuration>")
		fh.close()
		os.system("cat /etc/hadoop/hdfs-site.xml")
		os.system("tput setaf 2")
		print "\n\n       Now hdfs file is configured"
		os.system("tput setaf 0")
		os.system("tput setaf 1")
		print "\n\n       Now its time to core file"
		os.system("tput setaf 0")
		os.system("tput setaf 1")
		print "\n\n      before update core-site.xml file"
		os.system("tput setaf 0")
		os.system("cat /etc/hadoop/core-site.xml")
		os.system("tput setaf 1")
		print "\n\n             after updating core-site.xml file"
		os.system("tput setaf 0")
		fd=open("/etc/hadoop/core-site.xml","w")
		fd.write("<?xml version=\"1.0\"?>\n")
		fd.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")
		fd.write("<!-- Put site-specific property overrides in this file. -->")
		fd.write("\n\n<configuration>\n\n<property>")
		fd.write("\n<name>fs.default.name</name>")
		fd.write("\n<value>hdfs://"+ip+":9001</value>")
		fd.write("\n</property>\n\n</configuration>")
		fd.close()
		os.system("cat /etc/hadoop/core-site.xml")
		os.system("tput setaf 2")
		print "\n\n       Now core file is configured"
		os.system("tput setaf 0")
		os.system("tput setaf 2")
		print "\n\n       both files are configured so namenode is configured"
		os.system("tput setaf 0")
		print "\nnow we will format namenode"
		print "\nso to format namenode enter the command\n"
		os.system("tput setaf 2")		
		print "]#hadoop namenode -format"
		os.system("tput setaf 0")
		
		y2=raw_input()
		while(y2!="hadoop namenode -format"):
			print "command not found \nre-enter the format command \n"	
			y3=raw_input()
			if(y3=="hadoop namenode -format"):
				print "command ok we are formating namenode"
				break		
				
		os.system("hadoop namenode -format")
		
		
		
