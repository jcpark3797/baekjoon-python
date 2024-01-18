import sys
a = [1,1,2,2,2,8]
for i, data in enumerate(sys.stdin.readline().strip().split()):
    a[i] = str(a[i]-int(data))
print(' '.join(a))