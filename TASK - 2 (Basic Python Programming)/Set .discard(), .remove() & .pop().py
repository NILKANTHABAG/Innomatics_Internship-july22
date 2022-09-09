n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    inp= input()
    if inp == "pop":
        s.pop()
    else:
        command , value = inp.split()
        if command == "discard":
            s.discard(int(value))
        else:
            s.remove(int(value))
print(sum(s))