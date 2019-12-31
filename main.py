# import system function
import os
# import user dump
import json

# list all scoreboard
def listall():
    print("This is the command: ")
    with open("commands/listallcommand.cmds", 'r') as f_obj:
        cmd = f_obj.read()
        print(cmd)

# user run
print("Adjust you can execute commands: ")
print("1. List all exist scoreboards")

options = input("Option Number: ")

# judge options
if options == "1":
    listall()
