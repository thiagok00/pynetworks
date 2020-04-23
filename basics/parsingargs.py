#!/usr/local/bin/python3
import argparse

parser = argparse.ArgumentParser(description="This is our description")
parser.add_argument('-i', type=str, help="This is the help you get to describe the parameter", required=True)
parser.add_argument('-o', type=str, help="This is optional", required=False)

cmdargs = parser.parse_args()

ivar = cmdargs.i
print(ivar)
print(cmdargs)
