import os
import subprocess
import math
import re
import time

# Test functions for time module
print "Test time module: sleep 1 second"
time.sleep(0.1)

print "Test time module: time.time()=", time.time()

print "Test time module: time.ctime()=", time.ctime()

def cmd(x):
    return subprocess.Popen(filter(lambda x:x!="", x.split(" ")), stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()[0]

print "Test subprocess module: run 'pwd'=", cmd("pwd")[:-1]

print "Test os module: current dictory = ", os.getcwd()

print "Test os module: change dictory to / "
os.chdir("/")

print "Test os module: current dictory = ", os.getcwd()

print "Test os module: get dictory content(first 3) = ", os.listdir("/")[:3]

print "Test re module:", re.findall("aaa", "111bbbaaacccc")

print "Test math module: math.sin(1) =", math.sin(1)



