#!/usr/bin/python2

import os
import commands
output=commands.getoutput('pwd')
i=1

while(i<2):
	os.system("tput setaf 1")
	print "                    your options are"
	
		
	print"""
	
	press 1:to configure namenode/master node.
	
	press 2:to configure jobtracker/master node.
	
	press 3:to configure tasktracker/slave node.
	
	press 4:to configure client node.

	press 5:to dfsadmin report of namenode

	press 6:to exit.
	"""
	os.system("tput setaf 0")
	ch=raw_input("enter your choice:-")





	if int(ch)==1:
		ip=raw_input("enter ip of the namenode:-")
		
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/namenode  "+ip+":/root/Desktop")

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/namenode\n then type the command]#chmod +x hadoop_name_node_java.py\n then enter the command\n]#./hadoop_name_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)		




	if int(ch)==2:
		ip=raw_input("enter ip of the jobtracker:-")
		
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/jobtracker  "+ip+":/root/Desktop")

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/jobtracker\n then type the command]#chmod +x hadoop_name_node_java.py\n then enter the command\n]#./hadoop_name_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)		





#                                      data node coding

	elif int(ch)==3:
		ip=raw_input("enter ip of the tasktracker:-")
		
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/tasktracker  "+ip+":/root/Desktop")

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/tasktracker\n then type the command]#chmod +x hadoop_data_node_java.py\n then enter the command\n]#./hadoop_data_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)		




	elif int(ch)==4:
		ip=raw_input("enter ip of the clientnode:-")
		
		print "\n  first we will transfer file to this ip "+ip
		os.system("scp -r "+output+"/configure/clientmapred  "+ip+":/root/Desktop")

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/clientmapred\n then type the command]#chmod +x hadoop_client_node_java.py\n then enter the command\n]#./hadoop_client_node_java.py"
		os.system("tput setaf 0")	
		os.system("ssh -X root@"+ip)		

		











		
	elif int(ch)==5:
		ip=raw_input("enter ip of the namenode:-")
		
		

		os.system("tput setaf 1")		
		print "\n now we are doing ssh means remote server process"
		
		print "\n after ssh you first type the command ]#cd /root/Desktop/namenode\n then type the command]#chmod +x hadoopname_node.py\n then enter the command\n]#./hadoopname_node.py"
		os.system("tput setaf 0")	
		os.system("ssh root@"+ip)		







	elif int(ch)==6:
		exit()

	else:
		print "select correct options"

raw_input()
