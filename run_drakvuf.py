############################################################
# Drakvuf runner 
#
# Python script to make running drakvuf more convenient.   
############################################################

import sys
import subprocess
import logging
from xen_utils import get_xen_domain
from config import DRAKVUF_LOCATION
from config import REKALL_PROFILE_LOCATION
from config import DUMP_FOLDER
from config import INJECTION_METHOD
from config import ACTIVE_PLUGINS
from config import DEACTIVATED_PLUGINS
from config import INJECT_FILE

def run_command(drakvuf_command):
    logging.info("Drakvuf command built, run it")
    subprocess.run([drakvuf_command], shell=True)

def get_user_input(user_prompt):
    return input(user_prompt)

def build_drakvuf_command(program_arguments):
    drakvuf_command = "sudo " + DRAKVUF_LOCATION + "drakvuf -r " + REKALL_PROFILE_LOCATION
    domain = get_xen_domain()
    drakvuf_command += " -d " + domain
    #Parse through the passed arguments and build command bit for bit
    for arg in program_arguments:
        if(arg == "-D"):
            if(len(DUMP_FOLDER) == 0):
                logging.error("No dump folder in config specified")
                sys.exit()
            else:
                drakvuf_command += " -D " + DUMP_FOLDER
        elif(arg == "-i"):
            drakvuf_command += " -i " + get_user_input("specify PID to inject into \n")
        elif(arg == "-I"):
            if("-i" in program_arguments):
                drakvuf_command += " - I " + get_user_input("specify threadid for injection \n")
            else:
                logging.error("-i is required for -I")
                sys.exit()
        elif(arg == "-e"):
            if(len(INJECT_FILE) == 0):
                logging.error("No injection file specified in config")
                sys.exit()
            else:
                drakvuf_command += " -e " + INJECT_FILE
        elif(arg == "-m"):
            if(len(INJECTION_METHOD) == 0):
                logging.error("No ")

        "-e": ,
        "-m": ,
        "-b": ,
        "-n": ,
        "-t": ,
        "-o": ,
        "-p": ,

        }
    for arg in program_arguments


    #We're done building Frankensteins Monster, run it
    run_command(drakvuf_command) 
def main():
    for arg in sys.argv[1:]:
        print(arg)
    build_drakvuf_command(sys.argv[1:])

if __name__ == "__main__":
    main()