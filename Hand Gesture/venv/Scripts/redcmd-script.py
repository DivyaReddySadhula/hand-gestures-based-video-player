#!C:\Users\GVS\PycharmProjects\HandGuster\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'redcmd==1.2.10','console_scripts','redcmd'
__requires__ = 'redcmd==1.2.10'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('redcmd==1.2.10', 'console_scripts', 'redcmd')()
    )
