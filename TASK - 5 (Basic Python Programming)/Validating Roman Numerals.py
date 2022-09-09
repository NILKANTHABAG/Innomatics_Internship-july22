regex_pattern = r""	# Do not delete 'r'.
Thousands = 'M{0,3}'
Hundreds = '(C[MD]|D?C{0,3})'
Tens = '(X[CL]|L?X{0,3})'
Ones = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (Thousands, Hundreds, Tens, Ones)    

import re
print(str(bool(re.match(regex_pattern, input()))))