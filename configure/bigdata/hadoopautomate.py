#!/usr/bin/python2

import os
import commands

i=1
output=commands.getoutput('pwd')
while(i<2):
	os.system("tput setaf 1")
	print "                    your options are"
	
		
	print"""
	
	press 1:to configure namenode/master node.
	
	press 2:to configure datanode/slave node.
	
	press 3:to configure client node.

	press 4:to dfsadmin report of namenode
]
	press 5:to exit.
	"""
	os.system("tput setaf 0")
	ch=raw_input("enter your choice:-")








			#           namenode coding
	if int(ch)==1:
		os.system("tput setaf 4")
		os.system("cat "+output+"/configure/bigdata/namenode.txt")
		os.system("tput setaf 0")
		
	#	print "\n \n   there will a pinging process happen to check the ip you provided is right or wrong \n\b To exit from pinging process press ctrl+c."
		#print "press y for continue pinging process"
	#	print "so to start pinging process enter the command\n"
	#	os.system("tput setaf 2")		
	#	print "]#ping "+ip
	#	os.system("tput setaf 0")
	#	print "\n"
	#	y=raw_input()
	#	while(y!="ping "+ip):
	#		print "command not found \nre-enter the ping command with proper ip \n"	
	#		y1=raw_input()
	#		if(y1=="ping "+ip):
	#			print "command ok we are starting pinging process"
	#			break		
				
	#	os.system("ping "+ip)
	#	print "\n pinging process running fine "
	#	print "\n  we will configure namenode now"
		ip=raw_input("enter ip of the namenode:-")
		
		
	#	print "\n  first we will transfer file to this ip "+ip
	#	os.system("scp -r /root/Desktop/namenode  "+ip+":/root/Desktop")
	#	os.system("scp hadoop-1.2.1-1.x86_64.rpm  "+ip+":/root/Desktop/bigdata")
	#	os.system("scp jdk-7u79-linux-x64.rpm  "+ip+":/root/Desktop/bigdata")
		os.system("tput setaf 1")		
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/namenodeautomate  "+ip+":/root/Desktop")
		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/namenodeautomate\n then type the command]#chmod +x hadoop_name_node_java.py\n then enter the command\n]#./hadoop_name_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)
			
		


#                                      data node coding


	elif int(ch)==2:
		ip=raw_input("enter ip of the datanode:-")
		
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/datanodeautomate  "+ip+":/root/Desktop")

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/datanodeautomate\n then type the command]#chmod +x hadoop_data_node_java.py\n then enter the command\n]#./hadoop_data_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)			
		

	elif int(ch)==3:
		ip=raw_input("enter ip of the client:-")
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/clientnodeautomate  "+ip+":/root/Desktop")
		
		

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/clientnodeautomate\n then type the command]#chmod +x hadoop_client_node_java.py\n then enter the command\n]#./hadoop_client_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)		



		
	elif int(ch)==4:
		ip=raw_input("enter ip of the namenode:-")
		
		

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/namenodeautomate\n then type the command]#chmod +x hadoopname_node.py\n then enter the command\n]#./hadoopname_node.py"
		os.system("tput setaf 0")	
		os.system("ssh root@"+ip)		



	elif int(ch)==5:
		exit()

	else:
		print "select correct options"

raw_input()
