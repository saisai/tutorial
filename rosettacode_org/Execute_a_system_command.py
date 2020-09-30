import os

exit_code = os.system("ls")
output = os.popen("ls").read()
