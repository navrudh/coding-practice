'''
Algorithms > Strings > Mars Exploration

'''
#!/bin/python3

import sys

sos = "SOS"
transmittedMsg = input().strip()

print(sum(transmittedMsg[i] != sos[i%3] for i in range(len(transmittedMsg))))