# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
SET_N = set(map(int, input().split()))

y = int(input())
SET_B = set(map(int, input().split()))

NEW_SET = SET_N.union(SET_B)
print(len(NEW_SET))