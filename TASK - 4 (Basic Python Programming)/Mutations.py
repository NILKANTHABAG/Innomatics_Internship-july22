def mutate_string(string, position, character):
    L = list(string)
    L[position] = character
    string = ''.join(L)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)