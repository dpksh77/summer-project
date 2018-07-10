#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")

form=cgi.FieldStorage()

Fdatanode= form.getvalue('userdata')

ansible_playbooks = """
- hosts: datanode
  tasks:
  - name: "installing jdk"
    package:
       name: "/root/Desktop/java/jdk-8u171-linux-x64.rpm"
       state: present

  - name: "setting up java path"
    lineinfile:
       path: "/root/.bashrc"
       line: "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/"
       insertafter: EOF

  - name: "Setting"
    lineinfile:
       path: "/root/.bashrc"
       line: "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH"
       insertafter: EOF
  - name: "installing hadoop"
    package:
       name: \"/root/Desktop/hadoop/hadoop-1.2.1-1.x86_64.rpm\"
       state: present
    ignore_errors: yes
  - name: "folder"
    file:
       path: "/{0}"
       state: directory


  - copy:
      dest: \"/etc/hadoop/hdfs-site.xml\"
      src: \"/root/Desktop/hdfs-site\"
  - copy:
       dest: \"/etc/hadoop/core-site.xml\"
       src: \"/root/Desktop/core-site\"

  - command: \"hadoop-daemon.sh stop datanode\"
    ignore_errors: yes
  - command: \"hadoop-daemon.sh start datanode\"
 """.format(Fdatanode)
print(ansible_playbooks)




shellprogram= open("/var/www/cgi-bin/hadoop.yml", 'w')
shellprogram.write(ansible_playbooks)
shellprogram.close()
print("\n")

var= sp.getstatusoutput("sudo ansible-playbook hadoop.yml")
print(var)
if var[0] == 0:
    print("<h1>hadoop datanode setup</h1>")

else:
    print("failed")

