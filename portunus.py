import argparse


class reverse_shell:
    """Creates reverse shell
    """

    def __init__(self):
        """Runs main loop of reverse_shell
        """
        self.parser = self.parse_args()

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
        parser.add_argument(
            '-listener', help='Determines what side of the host/listener relationship current programming is running')
        return parser.parse_args()

    def host(self):
        """Runs main loop for host, beacons back to listener
        """
        pass

    def listener(self):
        pass
