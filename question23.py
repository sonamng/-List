
# # this list in one element repited but it is come in one time

n=[1,1,2,2,3,3,5,7]
i=0
a=[]
while i<len(n):
     b=n[i]
     if b not in a:
        a.append(b)
     i=i+1
print(a)
