from BeautifulSoup import BeautifulSoup

doc = open("test.nonewline.xml").read()

soup = BeautifulSoup(doc)
table = soup.find("table")

firstRow = table.contents[0]
firstCol = firstRow.findAll('td')

numberOfCols = len(firstRow.contents)

cols = []
for f in firstCol:
    cols.append(BeautifulSoup(str(f)).getText())



"""
for x in range(0, numberOfCols):
    print "%s" % firstRow

restOfRows = table.contents[1:]
for row in restOfRows:
    for x in range(0, numberOfCols):
        print "col data: %s" % row.contents[x].string
"""
