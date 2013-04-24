from BeautifulSoup import BeautifulSoup

doc = open("test.nonewline.xml").read()

# Search for the node <table> ... </table>
soup = BeautifulSoup(doc)
table = soup.find("table")

# The first row contains the data headers
firstRow = table.contents[0]
firstCol = firstRow.findAll('td')

numberOfCols = len(firstRow.contents)

col = []           # The list cols[] contains header tags
for f in firstCol:
    col.append(BeautifulSoup(str(f)).getText())

# Returns the string minus first 4 characters and last 5 characters
def stripTd(string):
    return string[5:][:-5]

restOfRows = table.contents[1:]
for row in restOfRows:
    colEntry = BeautifulSoup(str(row)).findAll('td')
    name = BeautifulSoup(str(colEntry[0])).getText()
    print (str(col[0]) + ": " + str(name))
    print (str(col[1]) + ": " + stripTd(str(colEntry[1])))
    print (str(col[2]) + ": " + stripTd(str(colEntry[2])))
    print (str(col[3]) + ": " + ("1" if "Yes" in str(colEntry[3]) else "0"))
    download = BeautifulSoup(str(colEntry[4]))
    print (str(col[4]) + ": " + download.a['href'] + " :: v" + download.getText())
    print (str(col[5]) + ": " + stripTd(str(colEntry[5])))
    print (str(col[6]) + ": " + stripTd(str(colEntry[6])))



"""
    print ("%s: %s" % (col[0], colEntry[0]))
    print ("%s: %s" % (col[1], colEntry[1]))
    print ("%s: %s" % (col[2], colEntry[2]))
    print ("%s: %s" % (col[3], colEntry[3]))
    print ("%s: %s" % (col[4], colEntry[4]))
    print ("%s: %s" % (col[5], colEntry[5]))
    print ("%s: %s" % (col[6], colEntry[6]))
"""
"""
for x in range(0, numberOfCols):
    print ("%s" % firstRow

restOfRows = table.contents[1:]
for row in restOfRows:
    for x in range(0, numberOfCols):
        print ("col data: %s" % row.contents[x].string
"""
