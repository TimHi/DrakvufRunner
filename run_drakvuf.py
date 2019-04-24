############################################################
# Drakvuf runner 
#
# Python script to make running drakvuf more convenient.   
############################################################

import sys
import subprocess
from xen_utils import get_xen_domain
from config import DRAKVUF_LOCATION
from config import REKALL_PROFILE_LOCATION

def run_command(drakvuf_command):
    subprocess.run([drakvuf_command], shell=True)


def build_drakvuf_command(program_arguments):
    drakvuf_command = "sudo " + DRAKVUF_LOCATION + "drakvuf -r " + REKALL_PROFILE_LOCATION
    domain = get_xen_domain()
    drakvuf_command += " -d " + domain
    #TODO: Parse arguments

    #We're done building Frankensteins Monster, run it
    run_command(drakvuf_command) 
def main():
    for arg in sys.argv[1:]:
        print(arg)
    build_drakvuf_command(sys.argv[1:])

if __name__ == "__main__":
    main()