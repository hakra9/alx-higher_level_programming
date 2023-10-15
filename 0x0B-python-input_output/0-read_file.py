#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents """
    with open(filename, r) as f:
        print(f.read(), end="")
