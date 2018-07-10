#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")

form=cgi.FieldStorage()
Fnamenode= form.getvalue('username')
#Fnamenode = "asdfasfddf"

ansible_playbooks = """
- hosts: jobtracker
  tasks:
  - name: \"installing jdk \"
    package:
      name: \"/root/Desktop/java/jdk-8u171-linux-x64.rpm\"
      state: present

  - name: setting up java path
    lineinfile:
       path: \"/root/.bashrc\"
       line: \"export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/\"
       insertafter: EOF

  - lineinfile:
       path: \"/root/.bashrc\"
       line: \"export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH\"
       insertafter: EOF
  - name: \"installing hadoop\"
    package:
      name: \"/root/Desktop/hadoop/hadoop-1.2.1-1.x86_64.rpm\"
      state: present
    ignore_errors: yes
  - name: folder
    file:
      path: /{0}
      state: directory
  - copy:
      dest: \"/etc/hadoop/mapred-site.xml\"
      src: \"/root/Desktop/jobfile\" 
 
  - copy:
      dest: \"/etc/hadoop/core-site.xml\"
      src: \"/root/Desktop/corejob\"

  - command: \"hadoop-daemon.sh stop jobtracker\"
    ignore_errors: yes
  - command: \" hadoop-daemon.sh start jobtracker\"





 """.format(Fnamenode)
print(ansible_playbooks)

shellprogram= open("/var/www/cgi-bin/hadoop.yml", 'w')
shellprogram.write(ansible_playbooks)
shellprogram.close()
print("\n")

var= sp.getstatusoutput("sudo ansible-playbook hadoop.yml")
print(var)
if var[0] == 0:
    print("<h1>hadoop jobtracker setup</h1>")
   
else:
    print("failed")


