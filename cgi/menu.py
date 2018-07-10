#!/usr/bin/python36

import cgi
import subprocess

print("content-type: text/html")
print("\n")

print("welcome to my tools")
form=cgi.FieldStorage()
first_name=form.getvalue('x')
#print(data)
last_name=form.getvalue('l')
email_address=form.getvalue('e')
mobile_number=form.getvalue('m')
password=form.getvalue('p')
#user=subprocess.getoutput(data)
print("<pre>")
print(first_name)
print("\n")
print(last_name)
print("\n")
print(email_address)
print("\n")
print(mobile_number)
print("\n")
print(password)
print("</pre>")


