import argparse
import os

parser = argparse.ArgumentParser(prog='portunus',
                                 description="creates a backdoor to install on a system to gain persistence")
connection = parser.add_mutually_exclusive_group()
connection.add_argument(
    "-u", "--udp", help="utilizes udp for shell interation")
connection.add_argument(
    "-t", '--tcp', help="estbalishes tcp connection for shell interation")

# parser.print_help()
while True:
    command = input("> ")
    if 'quit' == command or command == 'exit':
        break
    try:
        os.system(command)
        if command[:3] == 'cd ':
            try:
                os.chdir(command[3:])
            except:
                pass
    except:
        print("failure executing command")
