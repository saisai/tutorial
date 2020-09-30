
"""
http://www.rosettacode.org/wiki/Execute_a_system_command#Python
"""
from subprocess import PIPE, Popen, STDOUT
p = Popen('ls', stdout=PIPE, stderr=STDOUT)
print(p.communicate()[0])
