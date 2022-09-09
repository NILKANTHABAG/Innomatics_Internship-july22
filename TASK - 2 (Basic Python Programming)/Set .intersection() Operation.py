# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
roll_eng = set(map(int,input().split()))

french = int(input())
roll_french = set(map(int,input().split()))

print(len(roll_eng.intersection(roll_french)))