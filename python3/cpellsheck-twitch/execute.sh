#!/bin/bash

# 1. Run cpellerror and store the original words (for later comparison) in
# original file. Pass the results (error words) to cpellsheck and redirect the
# results to ans file
python cpellerror.py 2> original | python cpellsheck.py > ans 2> error

# 2. Filter answers from "> " and store that to answer file. Remove ans file.
cat ans | cut -d" " -f2 > answer
rm ans

# Find out the difference between original (created in #1) and answer (created
# in #2)
diff original answer

# Because the process involves taking inverse function of a function
# (correcting an induced spelling error), the answer should have no incorrect
# corrections. But the map being a one to many relation, calculating inverse
# correctly each time is not possible.
echo "False corrections: " `diff original answer | grep '>' | wc -l`
echo "No suggestions: " `diff original answer | grep 'NO' | wc -l`
