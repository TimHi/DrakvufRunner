import subprocess
import logging
from config import VM_IP

#Checks if a gvncviewer instance is active
def is_gvncviewer_active():
    cmd = "ps -al | grep gvncviewer"
    output = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE)
    if(len(output.stdout) == 0):
        return False
    else:
        return True

def start_gvncviewer():
    cmd = "gvncviewer " + VM_IP + " > /dev/null &"
    output = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if(len(output.stderr) > 0):
        logging.warning("Error creating gvncviewer instance")
    else:
        logging.info("Succesfully started gvncviewer instance")
