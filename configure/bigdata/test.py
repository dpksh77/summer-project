#!/usr/bin/python2

import os

print "before"
os.system("cat /etc/hadoop/hdfs-site.xml")
fh=open("/etc/hadoop/hdfs-site.xml","a")
fh.write("\n<property>\n<name>dfs.name.dir</name>\n<value>/master</value>\n</property>\n\n")
fh.close()
print "after"
os.system("cat /etc/hadoop/hdfs-site.xml")
raw_input()
