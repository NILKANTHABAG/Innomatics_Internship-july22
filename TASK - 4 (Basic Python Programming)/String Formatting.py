def print_formatted(number):
    # your code goes here
    Length = len(bin(number)[2:]) 
    for i in range(1 , number + 1): 
        print(str(i).rjust(Length , ' ') , end = " ")
        print(oct(i)[2:].rjust(Length,' ') , end = " ")
        print(((hex(i)[2:]).upper()).rjust(Length , ' ') , end = " ")
        print(bin(i)[2:].rjust(Length , ' ') , end = " ")
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)