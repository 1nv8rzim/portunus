import argparse
import paramiko

"""
portunus makes and managages sshable port on a system in order to gain persistence
**NOTE** this is for educational purposes only **NOTE**
author:     1nv8rZim
language:   python 3.8
"""


def parse_args():
    parser = argparse.ArgumentParser()
    """
    needed args
    ---
    username
    password
    ---
    ssh-key
    ---
    randomization key
    ---
    port-range
    ---
    replication name
    ---
    more to come...
    """
    return parser.parse_args()
