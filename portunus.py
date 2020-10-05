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

        return parser.parse_args()

    def host(self):
        pass

    def client(self):
        pass
