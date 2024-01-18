import sys
from collections import Counter
data = sys.stdin.readline().strip().upper()
cnt = Counter(data).most_common(2)
if len(cnt) == 1:
    print(cnt[0][0])
else:
    print('?' if (cnt[0][1]==cnt[1][1]) else cnt[0][0])