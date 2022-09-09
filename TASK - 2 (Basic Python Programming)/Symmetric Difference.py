# Enter your code here. Read input from STDIN. Print output to STDOUT
m= int(input())
m_set= set(map(int,input().split()))
n = int(input())
n_set= set(map(int,input().split()))

m_difference_n = m_set.difference(n_set)
n_difference_m = n_set.difference(m_set)

result = list(m_difference_n) + list(n_difference_m)
sorted_result = sorted(result)

print(*sorted_result,sep = '\n')