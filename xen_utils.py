import logging
import sys
import subprocess
from config import WINDOWS_CONFIG_LOCATION
from config import VM_IP
from file_utils import *

# Reads the name of the VM from the config file 
# return: VM name
def get_xen_name():
    windows_config_file = open_file(WINDOWS_CONFIG_LOCATION)
    for line in windows_config_file:
        words = line.split()
        #look for the name entry
        if "name" in words:
            xen_name = words[len(words)-1].replace('"', '')
            logging.info("VM name found: %s", xen_name)
            return xen_name
    logging.error("VM Name not found in config")
    sys.exit()
    
#Checks if the VM from the specified config is currently running
def is_vm_active(vm_name):
    cmd = "sudo xl list | grep " + vm_name
    output = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE)
    if(len(output.stdout) == 0):
        return False
    else:
        return True

#Starts a xen VM from a given config
def start_vm(xen_name):
    cmd = "sudo xl create " + WINDOWS_CONFIG_LOCATION
    subprocess.run([cmd], shell=True, stdout=subprocess.PIPE)
    #Test if command was run succesfully
    if(is_vm_active(xen_name)):
        logging.info("VM started succesfully")
    else:
        logging.error("Creating VM failed shutting down")
        sys.exit()

def get_xen_domain():
    vm_name = get_xen_name()
    cmd = "sudo xl list | grep " + vm_name
    output = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE)
    if(len(output.stdout) == 0):
        logging.error("VM %s not running", vm_name)
    else:
        #dom is running split string to get the int
        dom_num = output.stdout.split()[1]
        dom_num = str(dom_num).replace('b', '')
        dom_num = str(dom_num).replace("'", "")
        return dom_num