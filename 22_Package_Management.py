# Day 22 - Package management explanation and standard library tools

# Learning concept: 'pip install requests' is run in the terminal to get external libraries.
# Here we use built-in sys module to inspect installed packages/paths.

import sys

print("Python is searching for libraries in these locations:")
for path in sys.path[:3]:
    print(" -", path)

print("Standard package manager tool is 'pip'.")