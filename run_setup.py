############################################################
# Drakvuf Setup 
#
# Python script to make running drakvuf more convenient.
# Creates a Xen VM and runs gvncviewer
############################################################

import logging
import subprocess
from config import WINDOWS_CONFIG_LOCATION
from config import VM_IP
from xen_utils import start_vm
from xen_utils import get_xen_name
from xen_utils import is_vm_active
from gvncviewer_utils import is_gvncviewer_active
from gvncviewer_utils import start_gvncviewer

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Drakvuf Runner")
    #We need this few times so just save it directly
    xen_name = get_xen_name()
    if not(is_vm_active(xen_name)):
        logging.info("VM not running, booting it now...")
        start_vm(xen_name)
    if not(is_gvncviewer_active()):
        logging.info("gvncviewer not running, starting it now...")
        start_gvncviewer()
    
if __name__ == "__main__":
    main()