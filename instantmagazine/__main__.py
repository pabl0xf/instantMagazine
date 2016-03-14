"""The main routine of my_project."""
from gui import InstantMagazineApp
# Copyright (C) 2016 Pablo Frias.
# From: http://hack-it.com.ar
# License: MIT License

import sys

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

if __name__ == "__main__":
    main()