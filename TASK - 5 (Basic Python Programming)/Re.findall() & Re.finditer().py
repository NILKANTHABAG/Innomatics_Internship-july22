# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
String = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if String:
    for i in String:
        print(i)
else:
    print(-1)