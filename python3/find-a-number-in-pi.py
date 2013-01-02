#!/usr/bin/env python
"""
From: http://www.johndcook.com/blog/2013/01/01/finding-2013-in-pi/
To find a sequence of numbers in the digits of pi.

Requirements:
sudo pip3 install mpmath
"""

from mpmath import mp       # Multiprecision math package
mp.dps = 100000             # Set precision to 100000 significant figures
digits = str(mp.pi)[2:]     # Cutoff '3.' part from 3.1415...
digits.find('2013')         # Returns position or -1
