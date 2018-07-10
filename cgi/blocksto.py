#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")

form=cgi.FieldStorage()
username= form.getvalue('username')

#print(pendrive)
ansible_playbook= """
- hosts: localhost
  tasks:
  - name: \"create your primary partition \"
    parted:
      device: /dev/sdc
      number: 1
      state: present

  - name: \"service\"
    package:
      name: \"scsi-target-utils\"
      state: present
  - name: \"write in file\"
    lineinfile:
      path: \"/etc/tgt/targets.conf\"
      line: \"<target {0}>\"
      insertafter: EOF
  - lineinfile:
      path: \"/etc/tgt/targets.conf\"
      line: \"backing-store /dev/sdc1\"
      insertafter: EOF

  - lineinfile:
      path: \"/etc/tgt/targets.conf\"
      line: \"</targets>"
      insertafter: EOF

  - name: \"start service\"
    service:
       name: tgtd
       state: restarted

- hosts: client
  tasks:
  - command: \"iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.247 --discover\"

  - command: \"iscsiadm --mode node --targetname {0} --portal 192.168.43.247:3260 --login\"

""".format(username)
shellprogram= open("/var/www/cgi-bin/blocksto.yml",'w')
shellprogram.write(ansible_playbook)
shellprogram.close()
var= sp.getstatusoutput("sudo ansible-playbook blocksto.yml")
if var[0] ==0:
    print("<a href='http://192.168.43.247/blocksto1.html'>click here</a>")

else:
    print("Device not detected.........")

