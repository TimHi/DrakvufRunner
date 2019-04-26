############################################################
# Drakvuf runner 
#
# Python script to make running drakvuf more convenient.   
############################################################

import sys
import subprocess
import logging
from xen_utils import get_xen_domain
from config import *

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
        if(arg == "D"):
            if(len(DUMP_FOLDER) == 0):
                logging.error("No dump folder in config specified")
                sys.exit()
            else:
                drakvuf_command += " -D " + DUMP_FOLDER
        elif(arg == "i"):
            drakvuf_command += " -i " + get_user_input("specify PID to inject into \n")
        elif(arg == "I"):
            if("-i" in program_arguments):
                drakvuf_command += " - I " + get_user_input("specify threadid for injection \n")
            else:
                logging.error("-i is required for -I")
                sys.exit()
        elif(arg == "e"):
            if(len(INJECT_FILE) == 0):
                logging.error("No injection file specified in config")
                sys.exit()
            else:
                drakvuf_command += " -e " + INJECT_FILE
        elif(arg == "m"):
            if(len(INJECTION_METHOD) == 0):
                logging.error("No injection method specified in config")
                sys.exit()
            else:
                drakvuf_command += " -m " + INJECTION_METHOD
        elif(arg == "b"):
            drakvuf_command += " -b"
        elif(arg == "n"):
            if not("-D" in program_arguments):
                logging.error("no dump folder specified in config")
                sys.exit()
            else:
                drakvuf_command += " -n"
        elif(arg == "t"):
            if(len(TIMEOUT) == 0):
                logging.error("No timeout specified in config")
                sys.exit()
            else:
                drakvuf_command += " -t " + TIMEOUT
        elif(arg == "o"):
            if(len(OUTPUT_FORMAT) == 0):
                logging.warning("No output formet specified, using default")
            else:
                drakvuf_command += " -o " + OUTPUT_FORMAT
        elif(arg == "p"):
            drakvuf_command += " -p"
        else:
            logging.warning("Unrecognized parameter, skipping")
    for a_plugin in ACTIVE_PLUGINS:
        drakvuf_command += " -a " + a_plugin
    for d_plugin in DEACTIVATED_PLUGINS:
        drakvuf_command += " -x " + d_plugin
    #We're done building Frankensteins Monster, run it
    logging.info("Drakvuf command: %s", drakvuf_command)
    run_command(drakvuf_command) 
def main():
    logging.basicConfig(level=logging.INFO)
    build_drakvuf_command(sys.argv[1:])

if __name__ == "__main__":
    main()