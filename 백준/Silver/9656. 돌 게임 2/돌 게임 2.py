import sys

def b9545(n:int):
    if n % 2 == 0 :
        return 'SK'
    return 'CY'
if __name__ == '__main__':
    sys.stdout.write(b9545(int(sys.stdin.readline())))