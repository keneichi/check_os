#!/bin/python3
import platform
import sys

if (platform.architecture()[0]) == '32bit':
    print("Architecture is 32 bits. Please upgrade")
    sys.exit(2)
else:
    print("Architecture is 64bits. All OK.")
    sys.exit(0)
