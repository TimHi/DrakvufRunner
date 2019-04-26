# Drakvuf Runner  

This repository contains two main scripts, run_drakvuf.py which takes a few arguments and then runs a drakvuf instance and run_setup.py a script that creates a xen vm and starts a gvncviewer into it based on the values in config.py.

## Arguments for run_drakvuf.py  

Currently these arguments are implemented and used for an easier running of drakvuf:

**D** - Dump Folder, uses the path set in config.py  
**i** - PID of the process to hijack for injection  
**I** - ThreadID in the process to hijack for injection (requires i)  
**e** - executable to start with injection set in config.py  
**m** - Injection method set in config.py  
**b** - Exit from execution as soon as a BSoD is detected  
**n** - Use extraction method based on function injection (requires -D)  
**t** - Timeout of drakvuf in seconds  
**o** - Output format set in config.py  
**p** - Leave domain paused after DRAKVUF exits  

 For example: 
 > python run_drakvuf.py t o p b  
   
To activate/deactivate plugins just add them in the config.py

## Required Software  

* gvncviewer
* xen
* drakvuf
* rekall
* Python > 3.5
See [drakvuf's site](https://drakvuf.com/) on instructions on how to install drakvuf, xen & rekall

### Disclaimer  
This is a pretty specialised script for running drakvuf on my system, use it with caution.
 