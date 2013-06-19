def  getIntegerComplement( n):
	binary_rep = bin(n)[2:]
	binary_rep = binary_rep.replace('1', 't')
	binary_rep = binary_rep.replace('0', '1')
	binary_rep = binary_rep.replace('t', '0')
	return int(binary_rep, 2)


