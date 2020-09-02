import sys
import subprocess

def init_modules():
    libraries = ['sys', 'numpy,' 'PyQt5', 'threading', 'keyboard', 'time', 'tkinter']
    for library in libraries:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])
            print('Installed the Package Successfully!:', library)
        except:
            print('Failed to Install:', library, ' Please Install Manually')
            quit()
        return 0
