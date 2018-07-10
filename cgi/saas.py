#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")

form=cgi.FieldStorage()
username= form.getvalue('username')
cname= form.getvalue('cname')
software= form.getvalue('software')
print("software as a service")
print("login id root and password redhat")
ansible_playbooks = """
- hosts: localhost
  tasks:
  - name: install docker
    pip:
      name: docker-py

  - name: docker service
    service:
      name: docker
      state: started


  - name: make directory
    file:
     path: \"/root/Desktop/{0}\"
     state: directory

  - name: make file
    file:
     path: \"/root/Desktop/{0}/Dockerfile\"
     state: touch


  - name: write in file
    copy:
      content: FROM firefox
      dest: \"/root/Desktop/{0}/Dockerfile\"

  - name: write in file2
    lineinfile:
       path: \"/root/Desktop/{0}/Dockerfile\"
       insertafter: EOF
       line: RUN yum install {1}  -y

                                                 
  - name: docker command
    command: \"docker build -t {0} /root/Desktop/{0}/\"

  - name: container launching
    docker_container:
      name: {0}
      image: {0}
      interactive: true
      hostname: localhost
      volumes:
        - /usr/local/lib64/python3.6/site-packages
      tty: true
      state: started
      privileged: true
      command: /bin/bash
      exposed_ports: 4204
      ports:
       - "4445:4204"
 # - name: start docker
 #   command: \"docker start {0}\"

  - name: shell provide
    shell: \"docker exec {0} /usr/sbin/shellinaboxd -t -s /:SSH:0.0.0.0 -p 4204 &\"  


 """.format(username,software)
#print(ansible_playbooks)

shellprogram= open("/var/www/cgi-bin/shell.yml",'w')
shellprogram.write(ansible_playbooks)
shellprogram.close()
print("\n")
#print("playbook running.....")
var= sp.getstatusoutput("sudo ansible-playbook shell.yml")
#print(var)
if var[0] == 0:
    print("container named {0} launched....".format(username))
    print("<a href='http://192.168.43.247:4445' target='f1'>Click Here</a>")
    print("<iframe name='f1' style='width:100%; height:100%'</iframe>")
else:
    print("container named {0} failed....".format(username))   
 
                    
