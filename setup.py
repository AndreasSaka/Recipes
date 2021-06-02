import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'isodate'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-dateutil'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'easygui'])