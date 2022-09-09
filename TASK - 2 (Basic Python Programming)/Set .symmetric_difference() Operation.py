# Enter your code here. Read input from STDIN. Print output to STDOUT
x,a = input(),set(input().split())
y,b = input(),set(input().split())

print(len(a.symmetric_difference(b)))