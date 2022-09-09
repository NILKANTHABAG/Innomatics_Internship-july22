def split_and_join(line):
    # write your code here
    A = line.split()
    A = "-".join(A)
    return A

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)