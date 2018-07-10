#!/usr/bin/python36

import  cgi
import subprocess as sp


print("content-type: text/html")
print("")

form = cgi.FieldStorage()
username = form.getvalue('username')
dname = form.getvalue('dname')
softname = form.getvalue('softname')
print(softname)
if softname == "python":


#username="desdfepaasdsadffk113asdasdff4"
#print(username,dname,softname)
#username = "jklj"
  ansible_playbook = """
---
- hosts: localhost
  tasks:
  - name: install docker
    pip:
      name: docker-py
  - name: start service
    service:
      name: docker
      state: started


  - name: container launching
    docker_container:
      name: {0}
      image: paas_new
      interactive: true
      hostname: localhost
      volumes:
        - /usr/local/lib64/python3.6/site-packages
      tty: true
      state: started
      privileged: true
      command: \"/bin/bash\"     
      exposed_ports: 4203
      ports:
       - "4444:4203"
  - name: shell provide
    shell: \"docker exec {0} /usr/sbin/shellinaboxd -t -s /:SSH:0.0.0.0 -p 4203 &\"
...

""".format(username)
#  print(ansible_playbook)

  shellprogram = open("/var/www/cgi-bin/shell.yml","w")
  shellprogram.write(ansible_playbook)
  shellprogram.close()
  print("\n")
#  print("writed")

  var = sp.getstatusoutput("sudo ansible-playbook shell.yml")
#  print(var)
	#ip= sp.getstatusoutput("sudo docker inspect {0}".format(username))
#print(ip)
	#docker_launch_output = sp.getstatusoutput("sudo docker run -it -v /usr/local/lib64/python3.6/site-packages:/usr/local/lib64/python3.6/site-packages --name {c} {i}".format(c=username, i=dname))
	#print(docker_launch_output)
  if var[0]  == 0:
   print("container named {c} launched ..".format(c=username))
   print("login with deepak user:) and password is redhat")
   print("<a href='http://192.168.43.247:4444' target='f1'>click here</a>")
   print("<iframe name='f1' style='width:100%; height:100%'></iframe>")

  else:
	
   print("container named {c} failed ..".format(c=username))


else:
  print("<a href='http://192.168.43.247/java.html'>click here</a>")







