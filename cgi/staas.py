#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")

form=cgi.FieldStorage()
username= form.getvalue('username')
lvmsize= form.getvalue('lvmsize')
formattype= form.getvalue('formattype')
datanode1= form.getvalue('datanode1')
datanode2= form.getvalue('datanode2')


ansible_playbook= """
 
- hosts: localhost
  tasks:
  - name: \"create your primary partition \"
    parted:
      device: /dev/sdb
      number: 1
      state: present
 
  - name: \"create a volume group with PE=16MB\"
    lvg:
     vg: myvg1
     pvs: /dev/sdb1/
     pesize: 16
     state: present

  - name: \" create a logical volume\"
    lvol:
      vg: myvg1
      lv: mylv1
      size: "{1}"
      force: yes

  - name: \" format lvm\"
    filesystem:
       fstype: \"{2}\"
       dev: /dev/myvg1/mylv1
       force: yes

  - name: \"create folder to mount\"
    file:
      path: \"{0}\"
      state: directory

  - name: \"mount\"
    command: \"mount /dev/myvg1/mylv1 /root/{0}\"

  - name: \"nfs-protocol setup\"
    copy:
      content: \"/root/{0} 192.168.43.160(rw,no_root_squash)\"
      dest: \"/etc/exports\"

  - name: \"nfs service\"
    service:
       name: nfs
       state: restarted
       enabled: yes

- hosts: client
  tasks:
  - name: \"make directory\"
    file:
      path: \"/media/cloudstorage\"
      state: directory
  - command: \"mount 192.168.43.247:/root/{0} /media/cloudstorage\"

""".format(username,lvmsize,formattype)
#print(ansible_playbook)

shellprogram= open("/var/www/cgi-bin/staas.yml",'w')
shellprogram.write(ansible_playbook)
shellprogram.close()
var= sp.getstatusoutput("sudo ansible-playbook staas.yml")
if var[0] ==0:
    print("<a href='http://192.168.43.247/staas1.html'>click here</a>")
    
else:
    print("storage not provided..........") 
