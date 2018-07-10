#!/usr/bin/python36

import  cgi
import subprocess as sp

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')
#cname =  "os4"
#imgname = "centos:latest"
#print(cname , imgname)

docker_launch_output = sp.getstatusoutput("sudo docker run -dit --name  {c} {i}".format(c=cname, i=imgname))
#print(docker_launch_output)
if docker_launch_output[0]  == 0:
	print("container named {c} launched ..".format(c=cname))
	print("<a href='docker-manage.py'>click here to manage Container</a>")
else:
	
	print("container named {c} failed ..".format(c=cname))






