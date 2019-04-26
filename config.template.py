#Full path to the created vm config
WINDOWS_CONFIG_LOCATION = ""
#Full path to the drakvuf installation i.e /home/user/drakvuf/src/
DRAKVUF_LOCATION = ""
#IP for gvncviewer
VM_IP = ""
#Full path to the desired rekall profile
REKALL_PROFILE_LOCATION = ""
#Folder for extracted files (-D flag)
DUMP_FOLDER = ""
#Injection method for -m flag (createproc, shellexec, shellcode, doppelganging)
INJECTION_METHOD = ""
#List of Plugins to activate available are: objmon syscall poolmon socketmon exmon filetracer filedelete ssdtmon
ACTIVE_PLUGINS = ['objmon']
#List of Plugins that are deactivated
DEACTIVATED_PLUGINS = ['syscall', 'poolmon', 'socketmon', 'exmon', 'filetracer', 'filedelete', 'ssdtmon']
#The executable to start with injection
INJECT_FILE = ""
#Timeout of execution for -t flag in seconds
TIMEOUT = ""
#Output method (default, csv, kv, or json)
OUTPUT_FORMAT = ""