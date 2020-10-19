import argparse
import socket


class reverse_shell:
    """Creates reverse shell
    """

    def __init__(self):
        """Runs main loop of reverse_shell
        """
        self.parser = self.parse_args()
        self.main()

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
            '-listener', help='Determines what side of the host/listener relationship current programming is running')
        return parser.parse_args()

    def host(self):
        """Runs main loop for host, beacons back to listener
        """
        pass

    def listener(self):
        """Runs main loop for listener, listens for beacons from host
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', self.parser.lport))
        while True:
            c, addr = self.socket.accept()

    def main(self):
        """Runs main loop for reverse_shell
        """
        if parser.listener:
            self.listener()
        else:
            self.host()


if __name__ == '__main__':
    reverse_shell()
