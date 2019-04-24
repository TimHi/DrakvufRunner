############################################################
# Drakvuf runner 
#
# Python script to make running drakvuf more convenient.   
############################################################

import sys
from xen_utils import get_xen_domain
from config import DRAKVUF_LOCATION
from config import REKALL_PROFILE_LOCATION

def build_drakvuf_command(program_arguments):
    drakvuf_command = DRAKVUF_LOCATION + " -r " + REKALL_PROFILE_LOCATION
    domain = get_xen_domain()
def main():
    for arg in sys.argv[1:]:
        print(arg)
    build_drakvuf_command(sys.argv[1:])

if __name__ == "__main__":
    main()