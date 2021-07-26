#print hello multiple times with out using loop
import sys
num=int(input('Enter number of times you want to print'))
sys.setrecursionlimit(num)

def print_hello():
        print('Hello')
        print_hello()

print_hello()