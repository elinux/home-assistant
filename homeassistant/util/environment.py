""" Environement helpers. """
import sys


def is_virtual():
    """ Return if we run in a virtual environtment. """
    # Check supports venv && virtualenv
    return sys.base_prefix != sys.prefix or hasattr(sys, 'real_prefix')
