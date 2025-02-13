"""Helpers to install PyPi packages."""
import subprocess

from . import environment as env

# If we are not in a virtual environment, install in user space
INSTALL_USER = not env.is_virtual()


def install_package(package, upgrade=False, user=INSTALL_USER):
    """Install a package on PyPi. Accepts pip compatible package strings.
    Return boolean if install successfull."""
    # Not using 'import pip; pip.main([])' because it breaks the logger
    args = ['python3', '-m', 'pip', 'install', '--quiet', package]
    if upgrade:
        args.append('--upgrade')
    if user:
        args.append('--user')
    return not subprocess.call(args)
