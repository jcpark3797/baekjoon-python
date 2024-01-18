alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
data = input()
cnt = 0
for alp in alpha:
    cnt += data.count(alp)
    data = data.replace(alp, "*")
print(cnt+len(data.replace("*","")))