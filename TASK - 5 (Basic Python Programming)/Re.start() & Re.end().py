# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

String, k = input(), input()
matches = re.finditer(r'(?=(' + k + '))', String)

Foundanymatch = False
for match in matches:
    Foundanymatch = True
    print((match.start(1), match.end(1) - 1))

if Foundanymatch == False:
    print((-1, -1))