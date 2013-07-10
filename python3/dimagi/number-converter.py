#!/usr/bin/env python

digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# Could be used as ['eleven', 'twelve', 'thirteen'].append a list of [four - nine] plus teen

places = ['', '', 'hundred', 'thousand', 'million']

str = input("Enter a number: ")
backup = inp = int(str)

ans = []

# For the last two places
if (str[-2] == '1'):
  ans.append(teens[inp % 10])
else
  ans.append(digits(int(str[-1])))
  ans.append(tens(int(str[-2])))

# For rest of the places
inp = inp % 100   # Remove last two places
index = 2         # Start from hundreds place
while inp != 0:
  AAAAAR!