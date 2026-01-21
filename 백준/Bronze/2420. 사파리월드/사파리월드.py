import sys  
N, M= map(int, sys.stdin.readline().split())
sys.stdout.write(str(M-N if M>N else str(N-M)))