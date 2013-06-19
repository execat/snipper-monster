def getFinalAmount (initialAmount , betResults):
    betResults = betResults.upper()
    amount = initialAmount
    bet = 1
    for f in betResults:
		if amount - bet < 0:
			return amount
		if f == 'W':
			amount = amount + bet
			bet = 1
		if f == 'L':
			amount = amount - bet
			bet = bet * 2
    return amount
