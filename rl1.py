import os 
import sys


stream = os.popen('for ((i1;i<1000;i++)); do curl -svo /dev/null "http://localhost/dvwa/"; done')

output = stream.readlines()
