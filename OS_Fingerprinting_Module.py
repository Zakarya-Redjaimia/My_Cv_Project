import os
from sys import platform
import time
print(platform)

from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    print(os.system('ifconfig'))
elif platform == "darwin":
    # OS X
    print(os.system('ifconfig'))
elif platform == "win32":
    # Windows...
    print(os.system('ipconfig'))
time.sleep(3)
    
