# coding=utf-8
"""Main entry point"""

import argparse
import sys

import project


def __main__():
    if sys.argv[4] == "project":
        project.Project()
    else:
        print("Unknown module "+sys.argv[4])

if __name__ == "__main__":
    __main__()
